population_string = input().split(", ")
min_wealth = int(input())
population = []

for elements in population_string:
    number = int(elements)
    population.append(number)

if sum(population) < len(population) * min_wealth:
    print("No equal distribution possible")
    exit()
else:
    for element in range(len(population)):
        if population[element] < min_wealth:
            diff = min_wealth - population[element]

            wealth_people = max(population)
            wealth_index = population.index(wealth_people)

            population[wealth_index] -= diff
            population[element] += diff

print(population)