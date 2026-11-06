"""Phase 4 – pass-probability simulation for Decision 1 (Variante A) and the readiness gate.

Modelled rules (04a): attempt starts with 3 + bonus lives (bonus 0..2, max 5); each wrong test item costs
one life; 0 lives -> attempt failed (full chapter repeat); test finished with errors -> correction round
with one twin per wrong item; any twin wrong -> attempt failed; zero errors -> passed perfectly.
Bonus for the next chapter only after a perfect FIRST attempt (interpretation I-2).
Readiness gate (proposal V2): last practice block of 20 items, >= GATE_K correct at first try unlocks the test.

Pure functions for exact per-attempt probabilities; seeded Monte Carlo for course totals.
Assumptions [ANNAHME] are calibrated in the Phase-7 pilot (log gate scores and test outcomes).
"""
import json
import math
import random

# Per-chapter minutes (input, practice) from 03-curriculum.md Rev. 3R, table 2.1.
CHAPTER_MIN = {
    "A1-01": (124, 52), "A1-02": (131, 52), "A1-03": (118, 55), "A1-04": (87, 55), "A1-05": (100, 55),
    "A1-06": (112, 55), "A1-07": (122, 58), "A1-08": (116, 58), "A1-09": (118, 61), "A1-10": (126, 58),
    "A1-11": (104, 61), "A1-12": (86, 58), "A1-13": (86, 58), "A1-14": (118, 64), "A1-15": (116, 58),
    "A1-16": (113, 66), "A1-17": (107, 66), "A1-18": (99, 66), "A1-19": (106, 69), "A1-20": (82, 108),
    "A2-01": (106, 60), "A2-02": (118, 63), "A2-03": (128, 66), "A2-04": (136, 63), "A2-05": (118, 66),
    "A2-06": (103, 66), "A2-07": (101, 72), "A2-08": (132, 69), "A2-09": (130, 69), "A2-10": (109, 69),
    "A2-11": (101, 63), "A2-12": (115, 66), "A2-13": (115, 66), "A2-14": (108, 63), "A2-15": (114, 66),
    "A2-16": (94, 63), "A2-17": (114, 66), "A2-18": (98, 60), "A2-19": (94, 120),
}
OLD_REPEAT_TOTAL = 790      # minutes in 03 table 2.1 (15 % assumption)
OLD_TEST_MIN = 30           # 25 items x 1.0 + 5 feedback

RELEARN_SHARE = 0.6         # repeat costs 60 % of input + practice (unchanged from 03e2)
TEST_FEEDBACK = 5
TWIN_MIN = 1.5              # per twin item in the correction round incl. feedback
ERROR_REVIEW_MIN = 10       # mandatory error review before a repeat (rule R-K7)
GATE_ITEMS = 20
GATE_ITEM_MIN = 0.75
GATE_RETRY_PRACTICE = 10    # targeted practice on missed goals before the next gate block
GATE_GAIN = 0.02            # accuracy gain per failed gate + targeted practice [ANNAHME]
REPEAT_GAIN = 0.03          # accuracy gain per full chapter repeat [ANNAHME]
SIGMA = 0.04                # spread of chapter accuracy around the learner mean [ANNAHME]
P_CAP = 0.99


# ------------------------------------------------------------------ exact per-attempt model
def binom_pmf(n: int, k: int, q: float) -> float:
    """P(exactly k errors among n items) with error probability q."""
    return math.comb(n, k) * q ** k * (1 - q) ** (n - k)


def attempt_outcome(n: int, p: float, lives: int = 3, p_twin: float | None = None) -> dict:
    """Outcome classes of one test attempt (no gate). p_twin defaults to p."""
    pt = p if p_twin is None else p_twin
    q = 1 - p
    perfect = binom_pmf(n, 0, q)
    corr = sum(binom_pmf(n, e, q) for e in range(1, lives))
    passed_corr = sum(binom_pmf(n, e, q) * pt ** e for e in range(1, lives))
    return dict(perfect=perfect, passed=perfect + passed_corr, fail_lives=1 - perfect - corr,
                fail_corr=corr - passed_corr)


def expected_attempts(n: int, p: float, lives: int = 3, twin_delta: float = 0.0, max_k: int = 12) -> tuple:
    """E[attempts] and P(>= 3 attempts) with accuracy rising by REPEAT_GAIN per repeat."""
    surv, exp_att, p_ge3 = 1.0, 0.0, 0.0
    for k in range(1, max_k + 1):
        pk = min(P_CAP, p + REPEAT_GAIN * (k - 1))
        o = attempt_outcome(n, pk, lives, min(P_CAP, pk + twin_delta))
        exp_att += surv
        if k == 3:
            p_ge3 = surv
        surv *= 1 - o["passed"]
    return exp_att, p_ge3


def gate_pass_prob(p: float, k: int, n: int = GATE_ITEMS) -> float:
    """P(at least k of n gate items correct)."""
    return sum(binom_pmf(n, j, 1 - p) for j in range(0, n - k + 1))


# ------------------------------------------------------------------ Monte Carlo (seeded)
def run_chapter(rnd: random.Random, p: float, lives: int, n: int, gate_k: int) -> dict:
    """Play one chapter until passed. Returns attempts, perfect_first, gate reruns, extra minutes
    (gate reruns + twins + error reviews; relearn cost is added by the caller)."""
    extra, attempts, gate_reruns = 0.0, 0, 0
    while True:
        if gate_k:
            while sum(rnd.random() < p for _ in range(GATE_ITEMS)) < gate_k and gate_reruns < 40:
                gate_reruns += 1
                extra += GATE_RETRY_PRACTICE + GATE_ITEMS * GATE_ITEM_MIN
                p = min(P_CAP, p + GATE_GAIN)
        attempts += 1
        errs, alive = 0, True
        for _ in range(n):
            if rnd.random() > p:
                errs += 1
                if errs >= lives:
                    alive = False
                    break
        if alive and errs == 0:
            return dict(attempts=attempts, perfect_first=attempts == 1, gate_reruns=gate_reruns, extra=extra)
        if alive:
            extra += errs * TWIN_MIN
            if all(rnd.random() < p for _ in range(errs)):
                return dict(attempts=attempts, perfect_first=False, gate_reruns=gate_reruns, extra=extra)
        extra += ERROR_REVIEW_MIN
        p = min(P_CAP, p + REPEAT_GAIN)
        if attempts >= 15:
            return dict(attempts=attempts, perfect_first=False, gate_reruns=gate_reruns, extra=extra)


def course(n: int, gate_k: int, p_mean: float, runs: int = 4000, seed: int = 1) -> dict:
    """All 39 chapters in order with bonus-life carry-over. Returns course totals and per-chapter means."""
    rnd = random.Random(seed)
    per_ch = {c: 0.0 for c in CHAPTER_MIN}
    tot, reps, failed, ge3, perf, greruns = [], [], [], [], [], []
    for _ in range(runs):
        bonus, t, r_, f_, g3, pf, gr = 0, 0.0, 0, 0, 0, 0, 0
        for cid, (inp, pra) in CHAPTER_MIN.items():
            p = min(P_CAP, max(0.5, rnd.gauss(p_mean, SIGMA)))
            r = run_chapter(rnd, p, 3 + bonus, n, gate_k)
            x = r["extra"] + (r["attempts"] - 1) * (RELEARN_SHARE * (inp + pra) + n + TEST_FEEDBACK)
            per_ch[cid] += x
            t += x; r_ += r["attempts"] - 1; f_ += r["attempts"] > 1; g3 += r["attempts"] >= 3
            pf += r["perfect_first"]; gr += r["gate_reruns"]
            bonus = min(2, bonus + 1) if r["perfect_first"] else 0
        tot.append(t); reps.append(r_); failed.append(f_); ge3.append(g3); perf.append(pf); greruns.append(gr)
    mean = lambda xs: sum(xs) / len(xs)
    p90 = lambda xs: sorted(xs)[int(0.9 * (len(xs) - 1))]
    test_delta = (n + TEST_FEEDBACK - OLD_TEST_MIN) * len(CHAPTER_MIN)
    return dict(n=n, gate=gate_k, p=p_mean, repeats=mean(reps), repeats_p90=p90(reps), failed_chapters=mean(failed),
                chapters_ge3=mean(ge3), perfect_first=mean(perf), gate_reruns=mean(greruns),
                extra_h=mean(tot) / 60, extra_h_p90=p90(tot) / 60,
                delta_h=(mean(tot) - OLD_REPEAT_TOTAL + test_delta) / 60,
                per_chapter={c: v / runs for c, v in per_ch.items()}, extra_p90_min=p90(tot))


if __name__ == "__main__":
    NS, PS = [18, 20, 22, 25, 28, 30], [0.80, 0.85, 0.88, 0.90, 0.92, 0.95, 0.97]
    out = dict(exact=[], sens=[], gate=[], course=[])
    for n in NS:
        for p in PS:
            o = attempt_outcome(n, p)
            ea, ge3 = expected_attempts(n, p)
            out["exact"].append(dict(n=n, p=p, **o, exp_attempts=ea, p_ge3=ge3))
    for label, kw in (("Zwilling -5 pp", dict(twin_delta=-0.05)), ("Zwilling +3 pp", dict(twin_delta=0.03)),
                      ("4 Leben", dict(lives=4)), ("5 Leben", dict(lives=5))):
        for n in (20, 25):
            for p in (0.90, 0.92, 0.95):
                lives = kw.get("lives", 3); td = kw.get("twin_delta", 0.0)
                o = attempt_outcome(n, p, lives, min(P_CAP, p + td))
                out["sens"].append(dict(label=label, n=n, p=p, passed=o["passed"],
                                        exp_attempts=expected_attempts(n, p, lives, td)[0]))
    for p in (0.85, 0.88, 0.90, 0.92, 0.95):
        out["gate"].append(dict(p=p, k17=gate_pass_prob(p, 17), k18=gate_pass_prob(p, 18), k19=gate_pass_prob(p, 19)))
    for p in (0.88, 0.90, 0.92, 0.95):
        for n, g in ((25, 0), (20, 0), (20, 18), (20, 19)):
            out["course"].append(course(n, g, p))
    json.dump(out, open("sim04.json", "w"), indent=1)
    for r in out["exact"]:
        print("exact", {k: round(v, 3) if isinstance(v, float) else v for k, v in r.items()})
    for r in out["sens"]:
        print("sens", r["label"], r["n"], r["p"], round(r["passed"], 3), round(r["exp_attempts"], 2))
    for r in out["gate"]:
        print("gate", {k: round(v, 3) for k, v in r.items()})
    for r in out["course"]:
        print("course", {k: round(v, 2) if isinstance(v, float) else v for k, v in r.items() if k != "per_chapter"})
