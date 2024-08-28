def dist(src, tgt):
    """
    Compute the Levenshtein distance between src and tgt.
    """
    m = len(src)
    n = len(tgt)
    d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize boundary conditions.
    for i in range(m + 1):
        d[i][n] = m - i

    for j in range(n + 1):
        d[m][j] = n - j

    for i in reversed(range(m)):
        for j in reversed(range(n)):
            a = src[i]
            b = tgt[j]
            if a == b:
                d[i][j] = d[i + 1][j + 1]
            else:
                d[i][j] = 1 + min(d[i + 1][j], d[i][j + 1], d[i + 1][j + 1])

    return d[0][0]
