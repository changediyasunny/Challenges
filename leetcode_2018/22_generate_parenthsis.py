"""

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


Our complexity analysis rests on understanding how many elements there are in generateParenthesis(n). This analysis is outside the scope of this article, but it
turns out this is the n-th Catalan number 4^n/n * sqrt(n), which is bounded asymptotically by 4^n

Time Complexity : 4^n

Each valid sequence has at most n steps during the backtracking procedure.

Space Complexity : 4^n

as described above, and using O(n) space to store the sequence

"""

def generateParenthesis(N):
    ans = []
    def backtrack(S = '', left = 0, right = 0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if left < N:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)

    backtrack()
    return ans

print(generateParenthesis(3))
