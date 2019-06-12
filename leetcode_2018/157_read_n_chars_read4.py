"""
157. Read N Characters Given Read4

see definition on 158.
"""

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        ind = 0
        while n:
            buf4 = [''] * 4
            l = read4(buf4)
            if not l:
                return ind

            for i in range(min(l, n)):
                buf[ind] = buf4[i]
                ind += 1
                n -= 1
        return ind
