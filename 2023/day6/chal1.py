times = [47, 70, 75, 66]
distances = [282, 1079, 1147, 1062]

wins = {}
for time, distance in zip(times, distances):
    wins[time] = 0
    for i in range(1, time):
        if (time - i) * i > distance:
            wins[time] += 1
product = 1
for value in wins.values():
    product *= value

print(product)