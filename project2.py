def get_number (number):
    while True:
        operand = input("Number " + str(number) + ": " )
        try:
            return float(operand)
            
        except:
            print("invalid number, try again ")

            return operand

operand = get_number(1)
operand2 = get_number(2)            

sign = input("sign:")



result = 0
if sign == "+":
        result = operand + operand2
elif sign == "-":
        result = operand - operand2
elif sign == "/":
    if operand2 != 0:
        result = operand / operand2
    else:
        print("Division by Zero. ")

elif sign == "*":
        result = operand * operand2
else:
    print("invalid sign ")        

print(result)


