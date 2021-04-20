from Vector import Vector
import random

def testCase(expected, actual, num):
	print("Test case " + str(num) + ":" , end = " ")
	try:
		if not(isinstance(expected, Vector)) and expected == actual or expected.v == actual.v:
			print("passed")
		else:
			print("failed! Expected: ", end = "")
			print(expected)
			print("Your result: " , end = "")
			print(actual)
	except AttributeError:
		print("Failed- You're not returning the right type")
		print("Expected: ", expected)
		print("Your result: ", actual)
	except:
		print("Unknown error- please check your Vector.py file")
		print("Expected: ", expected)
		print("Your result: ", actual)
	print("="*40)


for i in range(1, 31):
	r = random.randint(0, 2)
	s1 = random.randint(1, 100)
	s2 = s1 if r>0 else random.randint(1, 100)
	l1 = [random.randint(-100, 100) for i in range(s1)]
	l2 = [random.randint(-100, 100) for i in range(s2)]
	v1 = Vector(l1)
	v2 = Vector(l2)

	if i <= 10:
		print("VECTOR ADDITION!!!!")
		ans = Vector([x+y for x,y in zip(v1.v,v2.v)]) if len(v1.v) == len(v2.v) else None
		testCase(ans, v1 + v2, i)
	elif i <=20:
		print("VECTOR SUBTRACTION!!!!")
		ans = Vector([x-y for x,y in zip(v1.v,v2.v)]) if len(v1.v) == len(v2.v) else None
		testCase(ans, v1 - v2, i)
	else:
		print("DOT PRODUCT!!!!")
		if len(v1.v) == len(v2.v):
			ans = sum(v1.v[i]*v2.v[i] for i in range(len(v1.v))) 
		else: ans = None
		testCase(ans, v1 * v2, i)






