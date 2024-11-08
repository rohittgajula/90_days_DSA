# time = (target - position[i]) / speed             use division(/ - this return o/p in decimal places) operation not floor division(//)


# using stack
def car_fleet_using_stack(target, position, speed):
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)         # p[10, 8, 5, 3, 0] - s[2, 4, 1, 3, 1] - [1, 1, 7, 3, 12]
    stack = []
    for p, s in pair:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)



# without using stack
def car_fleet(target, position, speed):
    cars = [(pos, (target - pos) / spd) for pos, spd in zip(position, speed)]
    cars.sort(reverse=True)
    fleets = 0
    current_time = 0

    for pos, time in cars:
        if time > current_time:
            fleets += 1
            current_time = time
    return fleets


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(car_fleet_using_stack(target, position, speed))
print(car_fleet(target, position, speed))

