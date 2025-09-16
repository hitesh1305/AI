from kanren import Relation, facts, run, var

bike = Relation()

facts(bike,
      ('ktm', 200000),
      ('royal_enfield', 250000),
      ('honda', 150000),
      ('hero', 100000),
      ('bajaj', 120000),
      ('tvs', 100000))

def get_all_bikes():
    x, p = var(), var()
    return run(0, (x, p), bike(x, p))

def _compare_price(bike_name, comparison_logic):
    price = var()
    target_price_result = run(1, price, bike(bike_name, price))
    if not target_price_result:
        return []
    target_price = target_price_result[0]
    
    all_bikes_list = get_all_bikes()
    return [b for b, p in all_bikes_list if comparison_logic(p, target_price)]

def cheaper_than(bike_name):
    return _compare_price(bike_name, lambda p, target: p < target)

def costlier_than(bike_name):
    return _compare_price(bike_name, lambda p, target: p > target)

def same_price(bike_name):
    return _compare_price(bike_name, lambda p, target: p == target)

print("Bikes cheaper than royal_enfield:", cheaper_than('royal_enfield'))
print("Bikes costlier than tvs:", costlier_than('tvs'))
print("Bikes with same price as hero:", same_price('hero'))