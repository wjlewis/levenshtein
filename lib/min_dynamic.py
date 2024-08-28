def dist(src, tgt):
    """
    Compute the Levenshtein distance between src and tgt.
    """
    m = len(src)
    n = len(tgt)

    v0 = [n - j for j in range(n + 1)]
    v1 = [0 for _ in range(n + 1)]

    for i in reversed(range(m)):
        # Boundary condition.
        v1[n] = m - i
        for j in reversed(range(n)):
            a = src[i]
            b = tgt[j]
            if a == b:
                v1[j] = v0[j + 1]
            else:
                v1[j] = 1 + min(v1[j + 1], v0[j], v0[j + 1])

        v1, v0 = v0, v1

    return v0[0]
