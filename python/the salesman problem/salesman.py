import random
import numpy as np
import matplotlib.pyplot as plt
import time 

def generate_random_cities(num_cities):
    cities = {}
    for i in range(num_cities):
        city_name = chr(65 + i)  
        x = random.uniform(0, 10)  
        y = random.uniform(0, 10)  
        cities[city_name] = (x, y)
    return cities


def plot_route_with_cities(cities, route):
    x = [cities[city][0] for city in route]
    y = [cities[city][1] for city in route]

    plt.clf()
    plt.plot(x, y, marker='o', linestyle='-')
    plt.scatter(x, y, c='red', marker='o', label='Cidades')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Rota Atual')
    plt.grid(True)
    plt.legend()
    #plt.show()
    plt.pause(0.01)


cities = generate_random_cities(10)

population_size = 100
num_generations = 50
mutation_rate = 0.01


def generate_initial_population(cities, population_size):
    city_names = list(cities.keys())
    population = []

    for _ in range(population_size):
        route = random.sample(city_names, len(city_names))
        population.append(route)

    return population


def calculate_fitness(route, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_distance += np.linalg.norm(np.array(cities[city1]) - np.array(cities[city2]))

    return 1 / total_distance


def select_parents(population, cities):
    fitness_scores = [calculate_fitness(route, cities) for route in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]

    parent1 = random.choices(population, probabilities)[0]
    parent2 = random.choices(population, probabilities)[0]

    return parent1, parent2


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    return child1, child2


def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]
    return route


def genetic_algorithm(cities, population_size, num_generations, mutation_rate):
    population = generate_initial_population(cities, population_size)
    best_route = None
    best_fitness = 0

    for generation in range(num_generations):
        new_population = []

        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, cities)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

        generation_best_route = max(population, key=lambda route: calculate_fitness(route, cities))
        generation_best_fitness = calculate_fitness(generation_best_route, cities)

        if generation_best_fitness > best_fitness:
            best_route = generation_best_route
            best_fitness = generation_best_fitness

        plot_route_with_cities(cities,generation_best_route)

        print(f"Geração {generation + 1}, Melhor Aptidão: {best_fitness:.8f}")

    plt.show()

    return best_route, best_fitness


def plot_route(cities, route):
    x = [cities[city][0] for city in route]
    y = [cities[city][1] for city in route]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Melhor Rota Encontrada')
    plt.grid(True)
    plt.show()

best_route, best_fitness = genetic_algorithm(cities, population_size, num_generations, mutation_rate)
print(f"Melhor Rota: {best_route}")
print(f"Melhor Aptidão: {best_fitness:.8f}")
plot_route(cities, best_route)