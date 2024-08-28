def gen_insts(src, tgt):
    """
    Generate a minimal sequence of instructions that transforms src into tgt.
    """
    if not src:
        return list(map(lambda y: Insert(y), tgt))
    elif not tgt:
        return list(map(lambda x: Delete(x), src))

    a, *src_tail = src
    b, *tgt_tail = tgt

    if a == b:
        return [Skip(), *gen_insts(src_tail, tgt_tail)]

    insert_b = gen_insts(src, tgt_tail)
    delete_a = gen_insts(src_tail, tgt)
    replace_ab = gen_insts(src_tail, tgt_tail)

    best = min(insert_b, delete_a, replace_ab, key=inst_count)

    if best is insert_b:
        return [Insert(b), *insert_b]
    elif best is delete_a:
        return [Delete(a), *delete_a]
    else:
        return [Replace(a, b), *replace_ab]


def inst_count(insts):
    """
    Counts the number of nontrivial instructions in insts.
    """
    return len(list(filter(lambda i: not isinstance(i, Skip), insts)))


class Insert:
    def __init__(self, elt):
        self.elt = elt

    def __str__(self):
        return f"INSERT {self.elt}"

    def __eq__(self, rhs):
        return self.elt == rhs.elt


class Delete:
    def __init__(self, elt):
        self.elt = elt

    def __str__(self):
        return f"DELETE {self.elt}"

    def __eq__(self, rhs):
        return self.elt == rhs.elt


class Replace:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __str__(self):
        return f"REPLACE {self.src} WITH {self.dst}"

    def __eq__(self, rhs):
        return self.src == rhs.src and self.dst == rhs.dst


class Skip:
    def __str__(self):
        return "SKIP"

    def __eq__(self, rhs):
        return True
