# Use the modulo operator to confirm which of the values
# shown below are divisible by seven.

def modulo():
    num_1 = 42
    num_2 = 137
    num_3 = 455
    num_4 = 1997

    num1_m = num_1 % 7
    num2_m = num_2 % 7
    num3_m = num_3 % 7
    num4_m = num_4 % 7

    for i,j in ((num1_m,num_1), (num2_m,num_2), (num3_m,num_3), (num4_m,num_4)):
        if i == 0:
            print(f'{j} is divisible by 7')

modulo()
