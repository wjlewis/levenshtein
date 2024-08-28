def dist(src, tgt):
    """
    Compute the Levenshtein distance between src and tgt.
    """
    if not src:
        return len(tgt)
    elif not tgt:
        return len(src)

    a, *src_tail = src
    b, *tgt_tail = tgt

    if a == b:
        return dist(src_tail, tgt_tail)

    return 1 + min(dist(src, tgt_tail), dist(src_tail, tgt), dist(src_tail, tgt_tail))
