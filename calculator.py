num1 = float(input("1st number: "))
opp = input("Operator: ")
num2 = float(input("Second number: "))

if opp == "+":
    print(num1 + num2)
elif opp == "-":
    print(num1 - num2)
elif opp == "/":
    print(num1 / num2)
else: 
    print(num1 * num2)

