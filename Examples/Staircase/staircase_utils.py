def staircase(n: int, ch: str) -> str:
    if not (0 < n <= 30):
        raise ValueError("n must be between 1 and 30")

    if len(ch) != 1:
        raise ValueError("display must be a single character")

    lines = []
    for i in range(1, n + 1, 1):
        lines.append(" " * (n - i) + ch * i)

    return "\n".join(lines)

