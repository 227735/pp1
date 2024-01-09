def f(d):
    passengers = 0
    count = 0

    for key, value in d.items():
        passengers += value
        loty = len(d)
        avg = passengers/loty 
        
        if value > avg:
            count += 1
    return count
    
print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))


