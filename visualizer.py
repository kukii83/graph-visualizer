import networkx as nx
import matplotlib.pyplot as plt

# ---------- matrix -> (n, edges) ----------
def edges_from_adjacency(M):
    n = len(M)
    edges = [(i + 1, j + 1) for i in range(n) for j in range(i, n) if M[i][j]]
    return n, edges

def edges_from_incidence(M):
    n = len(M)
    edges = []
    for e in range(len(M[0])):
        ends = [v + 1 for v in range(n) if M[v][e] != 0]
        edges.append((ends[0], ends[0]) if len(ends) == 1 else (ends[0], ends[1]))
    return n, edges

# ---------- spanning forest ----------
def spanning_forest(n, edges):
    parent = list(range(n + 1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    tree, chords = [], []
    for i, (u, v) in enumerate(edges):
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            tree.append(i)
        else:
            chords.append(i)
    return tree, chords

def tree_adj(n, edges, tree_idx):
    adj = {v: [] for v in range(1, n + 1)}
    for i in tree_idx:
        u, v = edges[i]
        adj[u].append((v, i))
        adj[v].append((u, i))
    return adj

def tree_path(adj, start, goal):
    stack, seen = [(start, [])], {start}
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        for nxt, ei in adj[node]:
            if nxt not in seen:
                seen.add(nxt)
                stack.append((nxt, path + [ei]))
    return None

# ---------- fundamental cycles ----------
def fundamental_cycles(n, edges, tree, chords):
    adj = tree_adj(n, edges, tree)
    cycles = {}
    for c in chords:
        u, v = edges[c]
        path = [] if u == v else tree_path(adj, u, v)
        cycles[c] = set(path) | {c}
    return cycles

def cycle_matrix(tree, chords, cycles):
    cols = chords + tree
    rows = [[int(j in cycles[c]) for j in cols] for c in chords]
    return rows, cols

# ---------- fundamental cut-sets ----------
def fundamental_cutsets(n, edges, tree):
    cutsets = {}
    for t in tree:
        adj = tree_adj(n, edges, [x for x in tree if x != t])
        side, stack = {edges[t][0]}, [edges[t][0]]
        while stack:
            node = stack.pop()
            for nxt, _ in adj[node]:
                if nxt not in side:
                    side.add(nxt)
                    stack.append(nxt)
        cutsets[t] = {i for i, (u, v) in enumerate(edges) if (u in side) != (v in side)}
    return cutsets

def cutset_matrix(tree, chords, cutsets):
    cols = tree + chords
    rows = [[int(j in cutsets[t]) for j in cols] for t in tree]
    return rows, cols

# ---------- printing ----------
def print_matrix(title, rows, row_labels, cols):
    print(title)
    print("      " + "".join(f"{'e' + str(j + 1):>5}" for j in cols))
    for lab, r in zip(row_labels, rows):
        print(f"{lab:>5} " + "".join(f"{x:>5}" for x in r))
    print()

# ---------- drawing ----------
def draw_graph(ax, n, edges, pos, highlight=(), title=""):
    H = nx.Graph()
    H.add_nodes_from(range(1, n + 1))
    nx.draw_networkx_nodes(H, pos, ax=ax, node_color="lightblue", node_size=500)
    nx.draw_networkx_labels(H, pos, ax=ax)
    seen = {}
    for i, (u, v) in enumerate(edges):
        key = frozenset((u, v))
        k = seen.get(key, 0)
        seen[key] = k + 1
        rad = 0.0 if k == 0 else 0.25 * ((k + 1) // 2) * (1 if k % 2 else -1)
        hot = i in highlight
        nx.draw_networkx_edges(
            H, pos, edgelist=[(u, v)], ax=ax, arrows=True, arrowstyle="-",
            connectionstyle=f"arc3,rad={rad}",
            edge_color="red" if hot else "gray", width=3 if hot else 1.5)
        (x1, y1), (x2, y2) = pos[u], pos[v]
        if u == v:
            lx, ly = x1, y1 + 0.15
        else:
            lx = (x1 + x2) / 2 + 0.5 * rad * (y2 - y1)
            ly = (y1 + y2) / 2 - 0.5 * rad * (x2 - x1)
        ax.text(lx, ly, f"e{i + 1}", fontsize=9, color="red" if hot else "black",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))
    ax.set_title(title)
    ax.axis("off")


# ---------- input ----------
def read_matrix():
    print("Enter the matrix, one row per line (numbers separated by spaces or commas).")
    print("Press Enter on an empty line when done:")
    rows = []
    while True:
        line = input().strip()
        if not line:
            break
        rows.append([int(x) for x in line.replace(",", " ").split()])
    return rows

def validate(M, kind):
    if not M:
        raise ValueError("Matrix is empty.")
    if any(len(r) != len(M[0]) for r in M):
        raise ValueError("All rows must have the same number of columns.")
    if kind == "adjacency":
        if len(M) != len(M[0]):
            raise ValueError("An adjacency matrix must be square (n x n).")
    else:
        for e in range(len(M[0])):
            nonzero = [M[v][e] for v in range(len(M)) if M[v][e] != 0]
            if len(nonzero) not in (1, 2):
                raise ValueError(f"Column {e + 1} must have 1 or 2 non-zero entries.")

def get_graph():
    print("Matrix type:  1) Adjacency   2) Incidence")
    choice = input("Choose 1 or 2: ").strip()
    if choice not in ("1", "2"):
        raise ValueError("Please choose 1 or 2.")
    kind = "adjacency" if choice == "1" else "incidence"
    M = read_matrix()
    validate(M, kind)
    return edges_from_adjacency(M) if kind == "adjacency" else edges_from_incidence(M)

# ---------- show everything ----------
def show_panels(n, edges, pos, groups, names, title):
    """One subplot per cycle / cut-set, with its edges highlighted in red."""
    if not groups:
        return
    cols = min(3, len(groups))
    rows = -(-len(groups) // cols)
    fig, axes = plt.subplots(rows, cols, figsize=(4.5 * cols, 4 * rows), squeeze=False)
    for ax in axes.flat:
        ax.axis("off")
    for ax, grp, name in zip(axes.flat, groups, names):
        draw_graph(ax, n, edges, pos, highlight=grp, title=name)
    fig.suptitle(title)
    fig.tight_layout()

def main():
    try:
        n, edges = get_graph()
    except ValueError as err:
        print("Input error:", err)
        return

    tree, chords = spanning_forest(n, edges)
    cycles = fundamental_cycles(n, edges, tree, chords)
    cutsets = fundamental_cutsets(n, edges, tree)

    print("\nEdges:", ", ".join(f"e{i + 1}=({u},{v})" for i, (u, v) in enumerate(edges)))
    print("Tree edges:", [f"e{i + 1}" for i in tree], " Chords:", [f"e{i + 1}" for i in chords], "\n")

    rows, cols = cycle_matrix(tree, chords, cycles)
    print_matrix("Fundamental cycle matrix", rows, [f"Z{k + 1}" for k in range(len(rows))], cols)
    rows, cols = cutset_matrix(tree, chords, cutsets)
    print_matrix("Fundamental cut-set matrix", rows, [f"c{k + 1}" for k in range(len(rows))], cols)

    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1))
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, seed=42)     # same layout in every figure

    fig, ax = plt.subplots(figsize=(5, 4))
    draw_graph(ax, n, edges, pos, highlight=set(tree), title="Graph (spanning tree in red)")
    show_panels(n, edges, pos, [cycles[c] for c in chords],
                [f"Z{k + 1} (chord e{c + 1})" for k, c in enumerate(chords)], "Fundamental cycles")
    show_panels(n, edges, pos, [cutsets[t] for t in tree],
                [f"c{k + 1} (tree edge e{t + 1})" for k, t in enumerate(tree)], "Fundamental cut-sets")
    plt.show()

if __name__ == "__main__":
    main()
