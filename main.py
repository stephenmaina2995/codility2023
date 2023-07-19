# print('Hello world')
# def solution():
#     print('Hello world')
def solution(A, S):
    count = 0  # Initialize the count of recipes that can be prepared

    # Create a dictionary to store the frequency of each ingredient in S
    available_ingredients = {}
    for ingredient in S:
        available_ingredients[ingredient] = available_ingredients.get(ingredient, 0) + 1

    # Check each recipe in A
    for recipe in A:
        recipe_ingredients = {}

        # Count the frequency of each ingredient in the current recipe
        for ingredient in recipe:
            recipe_ingredients[ingredient] = recipe_ingredients.get(ingredient, 0) + 1

        # Check if all the ingredients in the recipe are available
        can_prepare_recipe = True
        for ingredient, count in recipe_ingredients.items():
            if ingredient not in available_ingredients or count > available_ingredients[ingredient]:
                can_prepare_recipe = False
                break

        # If all ingredients are available, increment the count
        if can_prepare_recipe:
            count += 1

    return count

# print(solution(A,S))
A = ["toast", "bread", "breada", "cheese"]
S = "abcdeeehrs"
print(solution(A, S))  # Output: 2

A = ["az", "azz", "zza", "zzz", "zzzz"]
S = "azzz"
print(solution(A, S))  # Output: 4
