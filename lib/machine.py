from lib.gen_insts import Insert, Delete, Replace, Skip


def run(src, insts):
    """
    Apply insts to src.
    """
    cs = []
    j = 0
    for i in insts:
        if isinstance(i, Insert):
            cs.append(i.elt)
        elif isinstance(i, Delete):
            if src[j] != i.elt:
                raise ValueError(f"Expected {i.elt}")
            j += 1
        elif isinstance(i, Replace):
            if src[j] != i.src:
                raise ValueError(f"Expected {i.src}")
            cs.append(i.dst)
            j += 1
        elif isinstance(i, Skip):
            cs.append(src[j])
            j += 1

    return "".join(cs)
