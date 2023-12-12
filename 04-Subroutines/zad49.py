def f(dice):
    if not dice:
        return 0

    max_count = 0 
    current_count = 1 
    previous_roll = dice[0] 

    for roll in dice[1:]:
        if roll == previous_roll:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1
            previous_roll = roll

    max_count = max(max_count, current_count)

    return max_count

print(f("5233165554211"))  # Returns 5
print(f("2133"))  # Returns 3