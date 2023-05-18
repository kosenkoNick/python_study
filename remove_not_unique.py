data = [1,2,1,2,1,2,3]

for val in set(data):
    if data.count(val) == 1:
        data.remove(val)