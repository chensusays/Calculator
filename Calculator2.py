#!/usr/bin/python

import sys

class Calculator:
	def __init__(self):
		pass
	
	# new way
	# calculate on first pass
	# push results onto the stack
		# if subtraction, push int as negative
	# after first pass pop everything one by one and sum result
	
	def calculate(self, s):
		stack = []
		i = 0
		s = s.split(" ")
		while i < len(s):
			current = s[i]
			#print("current {}".format(current))
			num = 0
			if current == "+":
				i += 1
				continue			
			elif current == "-":
				i +=1
				current = self.multiply(-1, int(s[i]))
			elif current == "*":
				i +=1
				current = self.multiply(stack.pop(), int(s[i]))
			elif current == "/":
				i +=1
				
				current = self.divide(stack.pop(), int(s[i]))				
			stack.append(int(current))
			i +=1
		sum = 0
		while len(stack) > 0:
			num = stack.pop()
			#print("num %d" % num)
			sum += num
			#print("sum %d" % sum)
	
		return sum

	def multiply(self, a, b):
		#print("a %d" % a)
		#print("b %d" % b)
		#print("a * b %d" % (a*b))
		return a*b
	
	def divide(self, a, b):
		return a//b




def main(argv):
	calculator = Calculator()

	#test case add
	print("test case addition")
	print("given 1+2, expect 3")
	result = calculator.calculate("1 + 2")
	print(result)

	#test case sub
	print("test case subtract")
	print("given 4-1, expect 3")
	result = calculator.calculate("4 - 1")
	print(result)

	#test case multiply
	print("test case multiply")
	print("given 2*2, expect 4")
	result = calculator.calculate("2 * 2")
	print(result)

	#test case divide
	print("test case divide")
	print("given 12/3, expect 4")
	result = calculator.calculate("12 / 3")
	print(result)

	#test case 3
	print("test case oop")
	print("given 1 + 2 + 3 * 4 - 1 * 4 / 2, expect 13")
	result = calculator.calculate("1 + 2 + 3 * 4 - 1 * 4 / 2")
	print(result)

if __name__ == "__main__":
	main(sys.argv)	
