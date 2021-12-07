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
    horizontal_pos_mean = int(mean(crab))
    crab_fuel_mean = [int(abs(x - horizontal_pos_mean)) for x in crab]
    return sum([(x * (x+1)/2) for x in crab_fuel_mean])



print(calculate_fuel_1(crab))
print(calculate_fuel_2(crab))

