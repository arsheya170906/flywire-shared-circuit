import json
import pandas as pd
import networkx as nx

FILES = {
    "BANC": "banc_626_edge_list.csv", "FAFB": "fafb_783_edge_list.csv",
    "MANC": "manc_1.2.1_edge_list.csv", "MAOL": "maol_1.1_edge_list.csv",
    "MCNS": "mcns_0.9_edge_list.csv",
}
results = json.load(open("star_results.json"))

KIND = "out"
sizes = sorted(((results[n][KIND]["size"], n) for n in results), reverse=True)
chosen = [n for _, n in sizes[:3]]
N = sizes[2][0]
print("motif:", KIND, "| datasets:", chosen, "| N =", N)

# rebuild the induced subgraph straight from the raw edge list, not from the search adjacency
def induced(path, nodes):
    nodeset = set(nodes)
    g = nx.DiGraph()
    g.add_nodes_from(nodes)
    for chunk in pd.read_csv(path, chunksize=2_000_000):
        for s, d in zip(chunk.iloc[:, 0].tolist(), chunk.iloc[:, 1].tolist()):
            if s != d and s in nodeset and d in nodeset:
                g.add_edge(s, d)
    return g

columns, graphs = {}, {}
for ds in chosen:
    hub = results[ds][KIND]["hub"]
    nodes = [hub] + results[ds][KIND]["leaves"][: N - 1]
    columns[ds] = nodes
    graphs[ds] = induced(FILES[ds], nodes)
    g = graphs[ds]
    print(f"  [{ds}] nodes={g.number_of_nodes()} edges={g.number_of_edges()} from_hub={len(g.out_edges(hub))}")

ref = chosen[0]
for ds in chosen[1:]:
    gm = nx.algorithms.isomorphism.DiGraphMatcher(graphs[ref], graphs[ds])
    print(f"  VF2 {ref} <-> {ds}: {gm.is_isomorphic()}")

df = pd.DataFrame({ds: columns[ds] for ds in chosen})
df.to_csv("network.csv", index=False)
print("wrote network.csv", df.shape)
