def evenList(no_List):
    result_List=[]
    for number in no_List:
        if number%2==0 :
            result_List.append(number)
    return result_List


n=[1,2,3,4,5,6]
a=evenList(n)
print(a)

#EMI function
import math
def loan_emi(amount, duration, rate, down_payment=0):
    loan_amount = amount - down_payment
    emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    emi = math.ceil(emi)#round up
    return emi

emi1 = loan_emi(
    amount=1260000,
    duration=8*12,
    rate=0.1/12,
    down_payment=3e5
)
emi2 = loan_emi(amount=1260000, duration=10*12, rate=0.08/12)
if emi1 < emi2:
    print("Option 1 has the lower EMI: ${}".format(emi1))
else:
    print("Option 2 has the lower EMI: ${}".format(emi2))

#emi function when rate is zero to avoid divison by zero
def loan_emi(amount, duration, rate, down_payment=0):
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi

