"""
777. Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence
of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end,
return True if and only if there exists a sequence of moves to transform one string to the other.

Example:
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True

Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example:
start = "RXXLRXRXL"
end = "XRLXXRRLX"

Example:
start = "LLR"
end = "RRL"

Example:
start = "X"
end = "L"
"""

# Using Dict
def canTransform(start, end):
    if start.replace('X', '') != end.replace('X', ''):
        return False

    ctr = Counter()
    for s, e in zip(start, end):
        print(s, e)
        ctr[s] += 1
        ctr[e] -= 1
        if ctr['L'] > 0 or ctr['R'] < 0:
            return False
    return True
