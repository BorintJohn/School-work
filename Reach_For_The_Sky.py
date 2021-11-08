import numpy as np
xyDict = {}
TrueDict = {}
first_check = False
second_check = False
final_check = False
a = -50
solutions = 0
# get single x y from dict
def xy_get(get):
    a = str(get)
    w = 0
    length = len(a)
    for i in range(length):
        b = ','
        if b == a[i]:
            w = i
    result = a[1:w]
    result2 = a[w + 2:length - 1]
    return result,result2
# checker
for a in np.arange(-50, 50, 0.01):
    for b in np.arange(-50, 50, 0.01):
        a = round(a,2)
        b = round(b,2)
        # domain & range maker
        for x in range(-100,100):
            y = (-5*x**2)+(a*x)+b
            xyDict[x] = x,y
        #print(xyDict)
        # ab ba maker
        ab = str(a),str(b)
        ba = str(b),str(a)
        # checker
        for check_times in range(-100,100):
            xy = xy_get(xyDict[check_times])
            if ab == xy:
                first_check = True
                print("first check True: ",xy,'==',ab)
            #else:
                #print(ab,'!=', xy)
        for check_times in range(-100,100):
            xy = xy_get(xyDict[check_times])
            if ba == xy:
                second_check = True
                print("Second check True: ",xy,'==',ab)
            #else:
                #print(ab, '!=', xy)
        if first_check == True and second_check == True:
            final_check = True
        if final_check == True:
            print("Final Check True: ",ab)
            solutions = solutions + 1
            TrueDict[solutions] = ab
        print(a,b)
        first_check = False
        second_check = False
        final_check = False
print(TrueDict)
