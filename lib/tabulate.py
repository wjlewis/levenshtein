def tabulate(src, tgt):
    """
    Generate an HTML table illustrating the distance array creating while
    computing the Levenshtein distance between src and tgt.
    """
    d = generate_distances(src, tgt)

    return f"{styles}\n\n{render_table(src, tgt, d)}"


def generate_distances(src, tgt):
    m = len(src)
    n = len(tgt)
    d = [[None for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        d[i][n] = (m - i, f"Delete {src[i]}" if i < m else "")

    for j in range(n + 1):
        d[m][j] = (n - j, f"Insert {tgt[j]}" if j < n else "")

    for i in reversed(range(m)):
        for j in reversed(range(n)):
            a = src[i]
            b = tgt[j]

            if a == b:
                d[i][j] = (d[i + 1][j + 1][0], f"Skip {a}")
            else:
                delete_a = (d[i + 1][j][0] + 1, f"Delete {a}")
                insert_b = (d[i][j + 1][0] + 1, f"Insert {b}")
                replace_ab = (
                    d[i + 1][j + 1][0] + 1,
                    f"Replace {a} with {b}",
                )

                d[i][j] = min(delete_a, insert_b, replace_ab, key=lambda t: t[0])

    return d


def render_table(src, tgt, d):
    return f"<table><tbody>{render_top_row(tgt)}{render_rows(src, d)}</tbody></table>"


def render_top_row(tgt):
    return f"<tr><td></td>{''.join(map(render_th, tgt))}<td></td></tr>"


def render_th(c):
    return f"<th>{c}</th>"


def render_rows(src, d):
    return "".join(map(lambda row, i: render_row(src, row, i), d, range(len(d))))


def render_row(src, row, i):
    return f"<tr>{render_th(src[i]) if i < len(src) else '<td></td>'}{render_dists(row)}</tr>"


def render_dists(row):
    return "".join(map(lambda elt: render_elt(elt), row))


def render_elt(elt):
    dist, action = elt
    return f'<td><div title="{action}">{dist}</div></td>'


styles = """<style>
  table {
    border: 1px solid #444;
    border-collapse: collapse;
    font-family: monospace;
    font-size: 16px;
  }

  th,
  td {
    border: 1px solid #444;
  }

  th {
    background-color: #ddd;
    font-weight: bold;
  }

  td {
    cursor: help;
  }

  td:hover {
    background-color: #aae;
  }

  th, td > div {
    padding: 10px;
  }
</style>"""

from pprint import pprint
