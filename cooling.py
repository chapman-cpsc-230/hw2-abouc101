Tea = raw_input("Temperature of Tea")
T = float(Tea)
Room = raw_input("Temperature of Room")
R = float(Room)
Min = raw_input("Number of Minutes")
M = float(Min)
Looping = 0.00
MinPassed = 1.00
print "After 0 minutes, the temperature of the Tea is %d" %T
while M > Looping:
    TempMinus = 0.055 * (T - R)
    T = T - TempMinus
    print "After %d minutes, the temperature of the Tea is %f" % (MinPassed,T)
    MinPassed = MinPassed + 1.00
    Looping=Looping+1.00
name = raw_input ('')
