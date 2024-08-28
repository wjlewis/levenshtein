from graphviz import Digraph


def trace(src, tgt):
    """
    Render the calls to dist made while computing the Levenshtein distance
    between src and tgt.
    """
    traces = build_traces(src, tgt)
    return render_traces(src, tgt, traces)


def build_traces(src, tgt):
    """
    Trace the recursive calls that dist makes while computing the Levenshtein
    distance between src and tgt.

    Returns an array of traces, where a trace is a pair whose first element is
    an action ("insert", "delete", "skip", "replace"), and whose second element is
    a list of traces of subsequent computations.
    """
    if not src:
        return [] if not tgt else [("insert", [])]
    elif not tgt:
        return [("delete", [])]

    a, *src_tail = src
    b, *tgt_tail = tgt

    if a == b:
        return [("skip", build_traces(src_tail, tgt_tail))]

    return [
        ("insert", build_traces(src, tgt_tail)),
        ("delete", build_traces(src_tail, tgt)),
        ("replace", build_traces(src_tail, tgt_tail)),
    ]


def render_traces(src, tgt, traces):
    """
    Render a list of traces as a graphviz Digraph.
    """
    dot = Digraph(
        format="png",
        node_attr={"shape": "box", "fontname": "Fira Mono"},
        edge_attr={"fontname": "Fira Mono"},
    )
    i = 0

    # Attach the computations in traces to dot, and return the ID of the root
    # node of the tree.
    def loop(src, tgt, traces):
        nonlocal i
        root_id = str(i)
        i += 1
        dot.node(root_id, f"dist(\"{''.join(src)}\", \"{''.join(tgt)}\")")

        for child in traces:
            op, children = child

            if op == "insert":
                n = len(tgt) if not src else 1
                child_id = loop(src, tgt[n:], children)
                dot.edge(root_id, child_id, f"insert(\"{''.join(tgt[:n])}\")")
            elif op == "delete":
                n = len(src) if not tgt else 1
                child_id = loop(src[n:], tgt, children)
                dot.edge(root_id, child_id, f"delete(\"{''.join(src[:n])}\")")
            elif op == "skip":
                child_id = loop(src[1:], tgt[1:], children)
                dot.edge(root_id, child_id, f'skip("{src[0]}")')
            elif op == "replace":
                child_id = loop(src[1:], tgt[1:], children)
                dot.edge(root_id, child_id, f'replace("{src[0]}"->"{tgt[0]}")')

        return root_id

    loop(src, tgt, traces)
    return dot
