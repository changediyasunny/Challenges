"""
301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid.
Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]

"""
# DFS
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.visited = set()
        # get initial count of all extra parentheses
        cnt = self.extra_braces(s)
        self.dfs(s, cnt, res)
        return res

    def dfs(self, s, cnt, res):
        if cnt == 0:
            res.append(s)
            return
        for i in range(len(s)):
            if s[i] in ['(', ')']:
                new_strs = s[:i] + s[i+1:]
                new_cnt = self.extra_braces(new_strs)
                # new_cnt < cnt : is very important
                # we need to find minimum removal of parenthesis and not all
                # removing this condition will make () as valid parentheses
                if new_strs not in self.visited and new_cnt < cnt:
                    self.visited.add(new_strs)
                    self.dfs(new_strs, new_cnt, res)

    def extra_braces(self, strs):
        opening = 0
        closing = 0
        maps = {'(': 1, ')': -1}
        for c in strs:
            opening += maps.get(c, 0)
            closing += 1 if opening < 0 else 0
            opening = max(0, opening)
        return opening + closing

# BFS
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid(strs):
            cnt = 0
            for c in strs:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        stack = [s]
        result = []
        while len(stack) and not len(result):
            nextLevel = set([])
            for i in range(len(stack)):
                strs = stack.pop(0)
                if valid(strs):
                    result.append(strs)
                else:
                    for k in range(len(strs)):
                        if strs[k] in ['(', ')']:
                            nextLevel.add(strs[:k]+strs[k+1:])
            stack = list(nextLevel)
        return result if result else [""]
