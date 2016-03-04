Y_str = raw_input("Base")
Y = int(Y_str)

n_str = raw_input("Exponent")
n = int(n_str)
x=0
P = 0
while n >= x:
    P = P + Y**x
    x=x+1
print P
name = raw_input ('')
