"""

Facebook Challenge: Raise number to Power.

If Even Number:  power( x*x, k // 2)
If ODD Number: power( x*x, (n - 1)/2 )

such an algorithm uses O( log(n) )  squarings and at most O( log(n) )  multiplications.
More precisely, the number of multiplications is one less than the number of ones present in the Binary representation.

"""

import sys
import time

def power_number(number, p):
	# check for power sign

	if p < 0:
		x = 1/number
		return power_number( x, -p)
	if n == 0:
		return 1
	elif n == 1:
		return number
	elif n%2 == 0:
		# even number. 
		return power_number(number * number, n // 2)
	elif n % 2 != 0:
		return power_number( number * number, (n - 1)/2 )
	return 

def main():
	number = 7
	p = 19
	power_number(number, p)


if __name__ == '__main__':
	main()
