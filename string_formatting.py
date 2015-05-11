num = input()
def dec_to_bin(x):
    return bin(x)[2:]

def dec_to_oct(x):
    return oct(x)[1:]

def dec_to_hex(x):
    return hex(x)[2:].upper()

w = len(dec_to_bin(num))
for m in range (1,num+1):
        print str(m).rjust(w) +' ' + str(dec_to_oct(m)).rjust(w) +' ' +str(dec_to_hex(m)).rjust(w) + ' ' +str(dec_to_bin(m)).rjust(w)