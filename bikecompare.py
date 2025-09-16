from kanren import Relation, facts, run, var

# Define the relation
bike = Relation()

# Add facts: (bike_name, price)
facts(bike,
      ('ktm', 200000),
      ('royal_enfield', 250000),
      ('honda', 150000),
      ('hero', 100000),
      ('bajaj', 120000),
      ('tvs', 100000))

# Query helper to get bike and price
def get_all_bikes():
    x, p = var(), var()
    return run(0, (x, p), bike(x, p))

# Comparison logic outside kanren
def cheaper_than(bike_name):
    # Get price of bike_name
    all_bikes = get_all_bikes()
    target_price = [p for (b, p) in all_bikes if b == bike_name]
    if not target_price:
        return []
    target_price = target_price[0]

    # Return bikes with price < target
    return [b for (b, p) in all_bikes if p < target_price]

def costlier_than(bike_name):
    all_bikes = get_all_bikes()
    target_price = [p for (b, p) in all_bikes if b == bike_name]
    if not target_price:
        return []
    target_price = target_price[0]

    return [b for (b, p) in all_bikes if p > target_price]

def same_price(bike_name):
    all_bikes = get_all_bikes()
    target_price = [p for (b, p) in all_bikes if b == bike_name]
    if not target_price:
        return []
    target_price = target_price[0]

    return [b for (b, p) in all_bikes if p == target_price]

# Usage
print("Bikes cheaper than royal_enfield:", cheaper_than('royal_enfield'))
print("Bikes costlier than tvs:", costlier_than('tvs'))
print("Bikes with same price as hero:", same_price('hero'))
