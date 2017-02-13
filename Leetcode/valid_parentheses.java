
/*

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

*/

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        int n = s.length();
        for(int i=0; i< n; i++)
        {
            char c = s.charAt(i);
            if (c == '(')
			    stack.push(')');
		    else if (c == '{')
			    stack.push('}');
		    else if (c == '[')
			    stack.push(']');
		    else if (stack.isEmpty() || stack.pop() != c)
			    return false;
        }
        return stack.isEmpty();
    }
}