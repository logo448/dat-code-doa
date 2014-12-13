import math
n = 1000
trips = []
for a in range(1,n):
    for b in range(a+1,n):
        c = (a*a) + (b*b)
        if math.sqrt(c) % 1 == 0:
            print a,b,math.sqrt(c)
            trips.append([a,b,math.sqrt(c)])
for trip in trips:
    if sum(trip) == n:
        print '-' * 50
        print trip
        boofar = 1
        for num in trip:
            boofar *= num
        print boofar
