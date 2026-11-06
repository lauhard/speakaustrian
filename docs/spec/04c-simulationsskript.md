# 04c – Simulationsskript Phase 4 (reproduzierbar)

> **Stand:** 06.11.2026 · **Zweck:** Bestehens-Simulation zu Entscheidung 1 (Testlänge, Testreife, Bonusleben) und Neuberechnung der Richtplan-Prognose aus `03e2` mit den Phase-4-Regeln. Ergebnisse: `04` Abschn. 2. Ziel in Phase 5: `scripts/plan/` im Repo.
> **Ausführen:** `python3 sim04.py > sim04.out && python3 plan04.py` (Python ≥ 3.10, keine Abhängigkeiten). Zufall nur über feste Seeds (Kurs-Simulation Seed 1, Kapitelwerte für den Richtplan Seed 3, Richtplan Seeds 0–4 wie `03e2`). Kommentare im Code auf Englisch.
> **Verhältnis zu `03e2`:** `plan04.py` ist ein schlanker Nachbau von `model3r.simulate()` mit identischer Logik und RNG-Reihenfolge. **Prüfung:** mit den alten Werten (Test 30 min, Wiederholung 15 %) reproduziert er `03` Abschn. 2.3 exakt bei den Plantagen (234 / 159 / 138 / 123) und auf ±0,3 h bei den Lernstunden (Rundung der Kapitelsummen 8.794 vs. 8.795 min). In Phase 5 wird statt des Nachbaus `model3r.py` mit `chapter_minutes()` aus `sim04` parametrisiert.

## Annahmen (alle `[ANNAHME]`, Kalibrierung im Pilot Phase 7)

| Größe | Wert | Begründung |
|---|---|---|
| Trefferquote am Kapitelende (vor Testreife) | Zentralfall 0,92; Spanne 0,88–0,95; je Kapitel ± 0,04 (Normalverteilung) | Leitner-Modell `03` nutzt 80–93 % je Fach; Kapitelende liegt direkt nach Übung |
| Zuwachs je gescheiterter Testreife-Runde + Zielübung | +0,02 | Abruf + gezielte Übung der Fehler (Retrieval Practice, Q90/Q92); Sensitivität 0,01–0,04 |
| Zuwachs je kompletter Kapitelwiederholung | +0,03 | Wiederholung im Abstand (Spacing, Q91) |
| Trefferquote Zwilling | = Trefferquote Item (Sensitivität −5 / +3 pp) | Feedback direkt davor hilft, Fehler zeigt aber Schwäche beim Lernziel |
| Kosten Wiederholung | 60 % von Input + Üben + neuer Test (wie `03e2`) + 10 min Fehler-Review | R-K4, R-K5 |
| Kosten Korrekturrunde | 1,5 min je Zwilling | inkl. Feedback |
| Kosten Testreife-Wiederholung | 10 min Zielübung + 20 × 0,75 min | erster Block steckt im geplanten Übungsteil |
| Bonusleben | nur nach perfektem **ersten** Versuch, +1 je Serie, max. +2 (I-2) | Entscheidung 2 |

## `sim04.py`

```python
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
```

## `plan04.py`

```python
"""Compact re-implementation of 03e2 model3r.simulate() (same logic, same RNG call order)
to re-run the guide-plan forecast with the Phase-4 chapter-test rules. Verified by reproducing 03 Rev. 3R."""
import random, json, sys
from collections import defaultdict
from sim04 import CHAPTER_MIN

# AGG from 03e2 aggregates.py: (entries, active, passive, sets, units)
AGG = {"A1-01":(45,44,1,0,44),"A1-02":(66,64,2,1,41),"A1-03":(44,41,3,0,41),"A1-04":(45,41,4,0,41),"A1-05":(51,45,6,0,45),
"A1-06":(49,48,1,1,42),"A1-07":(62,51,11,1,45),"A1-08":(48,44,4,0,44),"A1-09":(48,41,7,0,41),"A1-10":(44,41,3,0,41),
"A1-11":(45,41,4,0,41),"A1-12":(42,41,1,0,41),"A1-13":(43,41,2,0,41),"A1-14":(45,41,4,0,41),"A1-15":(58,54,4,2,41),
"A1-16":(46,41,5,0,41),"A1-17":(53,51,2,2,41),"A1-18":(55,43,12,0,43),"A1-19":(45,41,4,0,41),"A1-20":(24,18,6,0,18),
"A2-01":(55,42,13,0,42),"A2-02":(57,42,15,0,42),"A2-03":(54,47,7,1,42),"A2-04":(52,42,10,0,42),"A2-05":(55,42,13,0,42),
"A2-06":(50,42,8,0,42),"A2-07":(46,42,4,0,42),"A2-08":(60,45,15,0,45),"A2-09":(51,42,9,0,42),"A2-10":(56,42,14,0,42),
"A2-11":(68,42,26,0,42),"A2-12":(84,58,26,3,42),"A2-13":(50,42,8,0,42),"A2-14":(50,41,9,0,41),"A2-15":(93,44,49,0,44),
"A2-16":(65,42,23,1,43),"A2-17":(71,40,31,0,40),"A2-18":(50,41,9,0,41),"A2-19":(10,6,4,0,6)}
# (number of grammar topics, number of WOW goals) from 03e chapters.py
GW = {"A1-01":(2,2),"A1-02":(2,1),"A1-03":(2,1),"A1-04":(1,1),"A1-05":(1,2),"A1-06":(2,1),"A1-07":(2,1),"A1-08":(2,1),
"A1-09":(2,4),"A1-10":(2,1),"A1-11":(1,4),"A1-12":(1,1),"A1-13":(1,1),"A1-14":(2,3),"A1-15":(1,2),"A1-16":(1,1),
"A1-17":(1,3),"A1-18":(1,2),"A1-19":(1,3),"A1-20":(1,3),"A2-01":(1,3),"A2-02":(2,2),"A2-03":(2,3),"A2-04":(2,1),
"A2-05":(1,6),"A2-06":(1,3),"A2-07":(1,3),"A2-08":(2,4),"A2-09":(2,2),"A2-10":(1,2),"A2-11":(1,1),"A2-12":(0,2),
"A2-13":(1,6),"A2-14":(1,2),"A2-15":(1,2),"A2-16":(0,1),"A2-17":(1,5),"A2-18":(0,8),"A2-19":(1,1)}
OLD_REPEAT = {"A1-01":20,"A1-02":21,"A1-03":20,"A1-04":17,"A1-05":18,"A1-06":20,"A1-07":21,"A1-08":20,"A1-09":21,"A1-10":21,
"A1-11":19,"A1-12":17,"A1-13":17,"A1-14":21,"A1-15":20,"A1-16":21,"A1-17":20,"A1-18":19,"A1-19":20,"A1-20":22,
"A2-01":19,"A2-02":21,"A2-03":22,"A2-04":22,"A2-05":21,"A2-06":20,"A2-07":20,"A2-08":23,"A2-09":22,"A2-10":21,
"A2-11":19,"A2-12":21,"A2-13":21,"A2-14":20,"A2-15":20,"A2-16":19,"A2-17":21,"A2-18":19,"A2-19":24}
ORDER = list(CHAPTER_MIN); A1C = ORDER[:20]; A2C = ORDER[20:]
SIM_BLOCKS = {"MS-A1":[85,80],"SIM-A2-1":[92,70],"SIM-A2-2":[92,70],"GP-A2":[162],"MT-A2":[160]}
INTERVAL = [1,3,7,14,30]; P_OK = [0.80,0.85,0.88,0.90,0.93]
SEC = {"aktiv":9,"set":40,"grammatik":15,"werte":12,"fehler":25}

def sequence():
    s = [("CH",c) for c in A1C] + [("BUF","")] + [("SIM","MS-A1",i) for i in range(2)] + [("BUF","")]
    s += [("CH",c) for c in A2C[:10]] + [("SIM","SIM-A2-1",i) for i in range(2)] + [("CH",c) for c in A2C[10:]]
    s += [("BUF","")] + [("SIM","SIM-A2-2",i) for i in range(2)] + [("BUF","")] + [("SIM","GP-A2",0)] + [("BUF","")] + [("SIM","MT-A2",0)]
    return s

def card_mix(cid):
    e,a,p,s,u = AGG[cid]; g,w = GW[cid]
    return {"aktiv": u - s, "grammatik": 8*g + 4, "werte": 3*w, "fehler": 6, "set": s}

def totals(test_min, repeat):
    return {c: CHAPTER_MIN[c][0] + CHAPTER_MIN[c][1] + test_min + repeat[c] for c in ORDER}

def simulate(budget, tot, seed, box2=0.75, weekly_min=30):
    rnd = random.Random(seed); seq = sequence(); i = 0
    remaining = dict(tot); total = dict(tot)
    due = defaultdict(list); carry = []; day = 0; marks = {}; cat = defaultdict(float)
    while i < len(seq) and day < 600:
        day += 1; kind = seq[i][0]
        is_sim = kind == "SIM" and day % 7 != 0
        queue = carry + due.pop(day, [])
        if is_sim:
            carry = queue; _, key, b = seq[i]; cat["sim"] += SIM_BLOCKS[key][b]; i += 1
            if b == len(SIM_BLOCKS[key]) - 1: marks[key] = day
            continue
        carry = []; secs = 0
        for typ, box in queue:
            secs += SEC[typ]
            if rnd.random() < P_OK[box]:
                if box < 4: due[day + INTERVAL[box+1]].append((typ, box+1))
            else:
                due[day+1].append((typ, 0))
        L = secs/60; cat["leitner"] += L
        if day % 7 == 0:
            cat["woche"] += max(weekly_min, budget - L); continue
        if kind == "BUF":
            cat["puffer"] += max(0.0, budget - L); i += 1; continue
        left = max(0.0, budget - L)
        while left > 0.5 and i < len(seq) and seq[i][0] == "CH":
            cid = seq[i][1]; take = min(left, remaining[cid])
            if 0 < remaining[cid] - take <= 15: take = remaining[cid]
            for typ, n in card_mix(cid).items():
                x = n*take/total[cid]; x = int(x) + (1 if rnd.random() < (x-int(x)) else 0)
                for _ in range(x):
                    box = 1 if (typ != "fehler" and rnd.random() < box2) else 0
                    due[day + INTERVAL[box]].append((typ, box))
            remaining[cid] -= take; left -= take; cat["kapitel"] += take
            if remaining[cid] <= 0.5: i += 1
    return day, sum(cat.values())/60, marks

def avg(budget, tot, n=5):
    rs = [simulate(budget, tot, s) for s in range(n)]
    return round(sum(r[0] for r in rs)/n), round(sum(r[1] for r in rs)/n, 1), {k: round(sum(r[2][k] for r in rs)/n) for k in ("MS-A1","SIM-A2-2","MT-A2")}

def forecast(p_mean, n=20, gate_k=18):
    """Guide-plan forecast with Phase-4 rules: test n items (+5 min feedback), expected repeat minutes per chapter from sim04.course."""
    from sim04 import course
    c = course(n, gate_k, p_mean, seed=3)
    rep = {k: round(v) for k, v in c["per_chapter"].items()}
    f = c["extra_p90_min"] / sum(c["per_chapter"].values())
    tot = totals(n + 5, rep)
    tot90 = totals(n + 5, {k: round(v * f) for k, v in c["per_chapter"].items()})
    return dict(p=p_mean, repeat_sum=sum(rep.values()), repeat_p90=round(c["extra_p90_min"]), chapter_h=round(sum(tot.values()) / 60, 1),
                rep=rep, res={b: avg(b, tot) for b in (60, 90, 105, 120)}, days_p90={b: avg(b, tot90)[0] for b in (60, 90, 105, 120)})

if __name__ == "__main__":
    old = totals(30, OLD_REPEAT)
    out = dict(old={b: avg(b, old) for b in (60, 90, 105, 120)}, new=[forecast(p) for p in (0.90, 0.92, 0.95)])
    json.dump(out, open("plan04.json", "w"), indent=1, ensure_ascii=False)
    print("OLD", out["old"])
    for r in out["new"]:
        print(r["p"], "repeat", r["repeat_sum"], "p90", r["repeat_p90"], "chapter h", r["chapter_h"])
        for b in (60, 90, 105, 120):
            print("   ", b, r["res"][b], "P90 days", r["days_p90"][b])
    c = out["new"][1]["rep"]; print("central per chapter min/max", min(c.values()), max(c.values()))
```

## Ausgabe (gekürzt)

```text
OLD {60: (234, 240.8, {'MS-A1': 110, 'SIM-A2-2': 229, 'MT-A2': 234}), 90: (159, 240.5, {'MS-A1': 73, 'SIM-A2-2': 155, 'MT-A2': 159}), 105: (138, 239.9, {'MS-A1': 62, 'SIM-A2-2': 134, 'MT-A2': 138}), 120: (123, 241.7, {'MS-A1': 54, 'SIM-A2-2': 118, 'MT-A2': 123})}
0.9 repeat 2918 p90 3786 chapter h 178.8
    60 (273, 279.3, {'MS-A1': 131, 'SIM-A2-2': 269, 'MT-A2': 273}) P90 days 290
    90 (185, 279.9, {'MS-A1': 86, 'SIM-A2-2': 180, 'MT-A2': 185}) P90 days 197
    105 (160, 279.6, {'MS-A1': 74, 'SIM-A2-2': 156, 'MT-A2': 160}) P90 days 170
    120 (142, 280.5, {'MS-A1': 65, 'SIM-A2-2': 137, 'MT-A2': 142}) P90 days 151
0.92 repeat 2002 p90 2699 chapter h 163.5
    60 (254, 260.9, {'MS-A1': 121, 'SIM-A2-2': 249, 'MT-A2': 254}) P90 days 269
    90 (172, 260.3, {'MS-A1': 80, 'SIM-A2-2': 168, 'MT-A2': 172}) P90 days 181
    105 (150, 261.4, {'MS-A1': 68, 'SIM-A2-2': 145, 'MT-A2': 150}) P90 days 158
    120 (132, 260.8, {'MS-A1': 59, 'SIM-A2-2': 128, 'MT-A2': 132}) P90 days 139
0.95 repeat 972 p90 1474 chapter h 146.3
    60 (233, 240.5, {'MS-A1': 110, 'SIM-A2-2': 228, 'MT-A2': 233}) P90 days 244
    90 (159, 240.4, {'MS-A1': 73, 'SIM-A2-2': 155, 'MT-A2': 159}) P90 days 166
    105 (137, 239.3, {'MS-A1': 62, 'SIM-A2-2': 133, 'MT-A2': 137}) P90 days 143
    120 (123, 241.2, {'MS-A1': 54, 'SIM-A2-2': 118, 'MT-A2': 123}) P90 days 126
central per chapter min/max 46 58
```
