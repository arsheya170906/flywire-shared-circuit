import json, time
import pandas as pd

FILES = {
    "BANC": "banc_626_edge_list.csv",
    "FAFB": "fafb_783_edge_list.csv",
    "MANC": "manc_1.2.1_edge_list.csv",
    "MAOL": "maol_1.1_edge_list.csv",
    "MCNS": "mcns_0.9_edge_list.csv",
}
TOP_HUBS = 250

def load(path):
    df = pd.read_csv(path)
    out, inn = {}, {}
    for a, b in zip(df.iloc[:, 0].tolist(), df.iloc[:, 1].tolist()):
        if a == b:
            continue
        out.setdefault(a, set()).add(b)
        inn.setdefault(b, set()).add(a)
    return out, inn

# pick as many leaves as possible with no edges between them (greedy, fewest conflicts first)
def independent(cands, out, inn):
    cset = set(cands)
    conflict = {}
    for u in cands:
        nb = (out.get(u, set()) | inn.get(u, set())) & cset
        nb.discard(u)
        conflict[u] = nb
    chosen, removed = [], set()
    for u in sorted(cands, key=lambda x: len(conflict[x])):
        if u in removed:
            continue
        chosen.append(u)
        removed.add(u)
        removed |= conflict[u]
    return chosen

def best_star(out, inn, kind):
    if kind == "out":
        deg = {h: len(s) for h, s in out.items()}
    elif kind == "in":
        deg = {h: len(s) for h, s in inn.items()}
    else:
        deg = {h: len(out.get(h, set()) & inn.get(h, set())) for h in out}
    best_hub, best_leaves = None, []
    for h in sorted(deg, key=deg.get, reverse=True)[:TOP_HUBS]:
        if kind == "out":
            cand = out.get(h, set()) - inn.get(h, set())
        elif kind == "in":
            cand = inn.get(h, set()) - out.get(h, set())
        else:
            cand = out.get(h, set()) & inn.get(h, set())
        cand = cand - {h}
        if len(cand) <= len(best_leaves):
            continue
        leaves = independent(list(cand), out, inn)
        if len(leaves) > len(best_leaves):
            best_hub, best_leaves = h, leaves
    return best_hub, best_leaves

results = {}
for name, path in FILES.items():
    out, inn = load(path)
    results[name] = {}
    for kind in ("out", "in", "recip"):
        t = time.time()
        h, leaves = best_star(out, inn, kind)
        results[name][kind] = {"hub": h, "leaves": leaves, "size": 1 + len(leaves)}
        print(f"[{name}] {kind:6s} size={1+len(leaves):5d} hub={h} ({time.time()-t:.0f}s)")
    with open("star_results.json", "w") as f:
        json.dump(results, f)

for kind in ("out", "in", "recip"):
    sizes = sorted(((results[n][kind]["size"], n) for n in results), reverse=True)
    print(f"{kind:6s}: " + ", ".join(f"{n}={s}" for s, n in sizes) + f"  -> N={sizes[2][0]}")
