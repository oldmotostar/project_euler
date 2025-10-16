

def is_bouncy(n: int) -> bool:
    """Return True if a number is bouncy (neither increasing nor decreasing"""
    digits = [int(d) for d in str(n)]
    increasing = all(digits[i] <= digits[i+1] for i in range(len(digits) - 1))
    decreasing = all(digits[i] >= digits[i+1] for i in range(len(digits) - 1))
    return not (decreasing or increasing)

def find_number_for_target_proportion(target: float) -> int:
    """Find the smallest number where the proportion of bouncy number >= target."""
    count_bouncy = 0
    n = 99  # no bouncy numbers below 99

    while True:
        n += 1
        if is_bouncy(n):
            count_bouncy += 1
        proportion = count_bouncy / n
        if proportion >= target:
            return n
