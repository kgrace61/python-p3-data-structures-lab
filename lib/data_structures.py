spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        
        heat_emojis = "🌶" * heat_level
        
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
        spiciest_foods = get_spiciest_foods(spicy_foods)
        print_spicy_foods(spiciest_foods)
        
        

def get_average_heat_level(spicy_foods):
        all_heats = sum(food["heat_level"] for food in spicy_foods)
        num_foods = len(spicy_foods)
        return all_heats/num_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods