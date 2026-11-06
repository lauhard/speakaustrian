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
