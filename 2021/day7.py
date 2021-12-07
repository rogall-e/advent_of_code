from statistics import mean, median

with open("data/day7.txt") as f:
    crab = f.readline()

test_crabs = "16,1,2,0,4,2,7,1,2,14"

crab = [int(x) for x in crab.split(',')]


def calculate_fuel_1(crab):
    horizontal_pos = median(crab)
    crab_fuel = [int(abs(x - horizontal_pos)) for x in crab]
    return sum(crab_fuel)

def calculate_fuel_2(crab):
    horizontal_pos_mean = 478 #round(mean(crab))
    horizontal_pos_median = round(median(crab))
    crab_fuel_mean = [int(abs(x - horizontal_pos_mean)) for x in crab]
    crab_fuel_median = [int(abs(x - horizontal_pos_median)) for x in crab]
    return f"Mean: {sum([(x * (x+1)/2) for x in crab_fuel_mean])}\nMedian: {sum([(x * (x+1)/2) for x in crab_fuel_median])}"



print(calculate_fuel_1(crab))
print(calculate_fuel_2(crab))

