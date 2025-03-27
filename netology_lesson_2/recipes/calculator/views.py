from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def calculator(request, dish):
    template_name = "index.html"

    servings = int(request.GET.get("servings", 1))
    recipe_data = DATA.get(dish, {})

    new_amount = {}
    if recipe_data:
        for ingredient, amount in recipe_data.items():
           new_amount[ingredient] = amount * servings

    context = {
        "recipe": new_amount,
        "recipe_name": dish,
        "servings": servings
    }
    return render(request, template_name, context)