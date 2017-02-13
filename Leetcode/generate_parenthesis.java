/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/


public static List<String> generateParenthesis(int n)
    {
		/*
		 * Generate all valid parenthesis for given Integer Number
		 * */
        List<List<String>> lists = new ArrayList<>();
        lists.add(Collections.singletonList(""));
        System.out.println("List at the very start"+ " "+ lists);
        for (int i = 1; i <= n; ++i)
        {
            final List<String> list = new ArrayList<>();
            for (int j = 0; j < i; ++j)
            {
                for (final String first : lists.get(j))
                {
                	System.out.println("FIrst is = "+ " "+ first);
                    for (final String second : lists.get(i - 1 - j))
                    {
                    	System.out.println("Second is = "+ " "+ second);
                        list.add("(" + first + ")" + second);
                    }
                }
            }
            lists.add(list);
            System.out.println("After adding Lists are = "+ " "+ lists);
        }
        return lists.get(lists.size() - 1);
    }

//================================Solution=================

/*
List at the very start [[]]
FIrst is =  
Second is =  
After adding Lists are =  [[], [()]]
FIrst is =  
Second is =  ()
FIrst is =  ()
Second is =  
After adding Lists are =  [[], [()], [()(), (())]]
FIrst is =  
Second is =  ()()
Second is =  (())
FIrst is =  ()
Second is =  ()
FIrst is =  ()()
Second is =  
FIrst is =  (())
Second is =  
After adding Lists are =  [[], [()], [()(), (())], [()()(), ()(()), (())(), (()()), ((()))]]
reached end now.......
[()()(), ()(()), (())(), (()()), ((()))]

*/