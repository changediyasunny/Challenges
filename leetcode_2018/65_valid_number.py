"""
65. Valid Number

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

##########
Rules:

We use three flags: got_dot, got_e, got_digit, mark if we have met ., e or any digit so far.
First we strip the string, then go through each char and make sure:

If char == + or char == -, then prev char (if there is) must be e
. cannot appear twice or after e
e cannot appear twice, and there must be at least one digit before and after e
All other non-digit char is invalid

"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        got_dot = got_digit = got_e = False
        for i, ch in enumerate(s):
            if ch in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    # if + then prev-char has to be 'e' otherwise false
                    return False
            elif ch == '.':
                if got_dot or got_e:
                    # multiple dots & dot after 'e' not allowed
                    return False
                got_dot = True
            elif ch == 'e':
                if got_e or not got_digit:
                    # e9 is invalid
                    # e cannot appear twice, and there must be at least
                    # one digit before and after e
                    return False
                got_e = True
                got_digit = False
            elif ch.isdigit():
                got_digit = True
            else:
                return False
        return got_digit
