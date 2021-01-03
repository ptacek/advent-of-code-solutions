import sys

# Parses input into dictionary in form of: allergen => possible ingredients
# Also counts occurences of all ingredients
# Returns dictionary and counts
def parseInput(lines):
    allAllergens = {}
    ingredientCounts = {}

    for line in lines:
        tmp = line.strip().replace(')', '').split(" (contains ")
        allergens = tmp[1].split(", ")
        ingredients = set(tmp[0].split(" "))

        for alrg in allergens:
            if alrg not in allAllergens:
                allAllergens[alrg] = ingredients
            else:
                allAllergens[alrg] = allAllergens[alrg].intersection(ingredients)

        for ing in ingredients:
            if ing in ingredientCounts:
                ingredientCounts[ing] += 1
            else:
                ingredientCounts[ing] = 1

    return (allAllergens, ingredientCounts)

# Iterates over allergens and uses set difference until there is exactly
# one ingredient for one allergen
def excludeIngredients(input):
    complete = False
    
    while complete is False:
        complete = True

        for allergen in input:
            if len(input[allergen]) > 1:
                complete = False
                continue

            for other in input:
                if other == allergen:
                    continue
                else:
                    input[other] = input[other] - input[allergen]
        
# Sums counts of occurences of ingredients that don't contain any allergen
def countWithoutAllergens(allergens, counts):
    for allergen in allergens:
        for ingredient in allergens[allergen]:
            counts.pop(ingredient, None)

    total = 0

    for ingredient in counts:
        total += counts[ingredient]

    return total

# Transforms dictionary of allergens and ingredients into list of ingredients
# sorted alphabetically by their allergens
def getDagerousIngredientSorted(allergens):
    sorted = list(allergens.keys())
    sorted.sort()

    ingredients = []

    for allergen in sorted:
        ingredient = next(iter(allergens[allergen]))
        ingredients.append(ingredient)

    return ingredients

file = open(sys.argv[1], 'r')
lines = file.readlines()

allergens, counts = parseInput(lines)
excludeIngredients(allergens)

withoutAllergens = countWithoutAllergens(allergens, counts)
print("Part I: There are {} occurrences of allergen free ingredients".format(withoutAllergens))

dangerousList = getDagerousIngredientSorted(allergens)
print("Part II: canonical dangerous ingredient list is:")
print(",".join(dangerousList))

file.close()