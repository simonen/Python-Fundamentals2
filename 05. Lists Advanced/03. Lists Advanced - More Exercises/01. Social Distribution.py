population = list(map(int, input().split(", ")))
min_wealth = int(input())

# for _ in range(len(population)):
#     wealthiest = max(population)
#     poorest = min(population)
#     if poorest >= min_wealth:
#         print(population)
#         break
#     w_ind = population.index(wealthiest)
#     p_ind = population.index(poorest)
#     difference = min_wealth - poorest
#     if (wealthiest - difference) >= min_wealth:
#         population[w_ind] -= difference
#     else:
#         difference = wealthiest - min_wealth
#         population[w_ind] = min_wealth
#
#     population[p_ind] += difference
#
# if min(population) < min_wealth:
#     print("No equal distribution possible")

while min(population) < min_wealth:
    poor = [x for x in population if x < min_wealth]
    wealthy = [x for x in population if x > min_wealth]
    needed_wealth = min_wealth * len(poor) - sum(poor)
    if sum(wealthy) - needed_wealth < len(wealthy) * min_wealth:
        print("No equal distribution possible")
        break
    wealthiest = max(population)
    poorest = min(population)
    w_ind = population.index(wealthiest)
    p_ind = population.index(poorest)
    difference = min_wealth - poorest
    if (wealthiest - difference) >= min_wealth:
        population[w_ind] -= difference
    else:
        difference = wealthiest - min_wealth
        population[w_ind] = min_wealth

    population[p_ind] += difference
else:
    print(population)
