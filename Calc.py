d = None
c2 = 88
a = "angad"
c = 98
b = True
print("type of d is ", type(d))
print("type of d is ", type(c))
print("type of d is ", type(b))
print("type of d is ", type(a))
print(c2 + c)

print(a + str(c))

#create a calculator
print("Enter the first number:")
a = int(input())
print("Enter the second number: ")
b = int(input())
print("Enter the operator:")
c = input()
result = None
if c == "+":
  result = a + b
elif c == "-":
  result = a - b
elif c == "*":
  result = a * b
elif c == "/":
  result = a / b
elif c == "//":
  result = a // b
elif c == "%":
  result = a % b
else:
  print("Operator is not valid")

if result is not None:
  print(result)
