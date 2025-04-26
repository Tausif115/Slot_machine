array = [3,6,8,1,8]
minval = array[0]

for i in range(array):
    if i < minval:
        minval = i
print(minval)