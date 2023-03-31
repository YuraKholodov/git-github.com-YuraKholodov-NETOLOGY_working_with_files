from pprint import pprint

with open("recipes.txt", "rt", encoding="utf-8") as file:
    cook_book = {}
    for string in file:
        dish = string.strip()
        positions = int(file.readline().strip())
        lst = []
        for _ in range(positions):
            ingredient_name, quantity, measure = file.readline().strip().split(" | ")
            lst.append(
                {
                    "ingredient_name": ingredient_name,
                    "quantity": int(quantity),
                    "measure": measure,
                }
            )
        cook_book[dish] = lst
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    quantity_of_ingredients = {}
    for dish in dishes:
        for element in cook_book[dish]:
            ingredient_name, quantity, measure = (
                element["ingredient_name"],
                element["quantity"],
                element["measure"],
            )
            if ingredient_name not in quantity_of_ingredients:
                quantity_of_ingredients[ingredient_name] = {
                    "measure": measure,
                    "quantity": quantity * person_count,
                    "measure": measure,
                }
            else:
                quantity_of_ingredients[ingredient_name]["quantity"] += (
                    quantity * person_count
                )
    pprint(quantity_of_ingredients)


get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)


with open("1.txt", "rt", encoding="utf-8") as f1:
    size_f1 = 0
    for i in f1:
        size_f1 += 1

with open("2.txt", "rt", encoding="utf-8") as f2:
    size_f2 = 0
    for i in f2:
        size_f2 += 1


with open("3.txt", "rt", encoding="utf-8") as f3:
    size_f3 = 0
    for i in f3:
        size_f3 += 1


dict_txt = {"1.txt": size_f1, "2.txt": size_f2, "3.txt": size_f3}
sorted_dict_txt = dict(sorted(dict_txt.items(), key=lambda x: x[1]))

print(sorted_dict_txt)

with open("union.txt", "w", encoding="utf-8") as union:
    for key, value in sorted_dict_txt.items():
        union.write(key + "\n")
        union.write(str(value) + "\n")
        union.write('')
        with open(key, "rt", encoding="utf-8") as text:
            for string in text:
                union.write(string)
            union.write('\n')
