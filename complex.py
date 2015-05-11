def addition(r1,r2):
    r_res = r1[0] + r2[0]
    c_res = r1[1] + r2[1]

    return r_res,c_res


def subtraction(r1,r2):
    r_res = r1[0] - r2[0]
    c_res = r1[1] - r2[1]
    return r_res,c_res


def print_complex(res):
    if res[0] == 0:
        returnThing = "%.2f" % res[1] + 'i'
    else:
        returnThing  = "%.2f" % res[0] + ('' if res[1] == 0 else (' + ' if res[1] > 0 else ' - ') + "%.2f" % abs(res[1]) + 'i')

    if returnThing == '0.00i':
        return '0.00'
    else:
        return returnThing



def multiply(r1,r2):
    r_res = r1[0] * r2[0] - r1[1] * r2[1]
    c_res = r1[0] * r2[1] + r2[0] * r1[1]
    return r_res,c_res


for x in range(1):
    r1 = list(map(float,raw_input().split(' ')))
    if len(r1) == 1:
        r1.append(float(0))
    r2 = list(map(float,raw_input().split(' ')))
    if len(r2) == 1:
        r2.append(float(0))

    #Addition
    add_result = addition(r1,r2)
    print print_complex(add_result)

    #Subtraction
    sub_result = subtraction(r1,r2)
    print print_complex(sub_result)

    #Multiplication
    mul_result = multiply(r1,r2)
    print print_complex(mul_result)

    #Division
    r3 = [r2[0],-r2[1]]
    div_result = multiply(r1,r3)
    div_resul2 = multiply(r2,r3)[0]
    div_result = [div_result[0]/div_resul2,div_result[1]/div_resul2]
    print print_complex(div_result)

    #Mod of First
    print "%.2f"%(r1[0]**2 + r1[1]**2)**0.5

    #Mod of Second
    print "%.2f"%(r2[0]**2 + r2[1]**2)**0.5