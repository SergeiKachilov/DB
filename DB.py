import sqlite3

def DB(command, name, price, category, menu):
    with sqlite3.connect("t1.db") as conn:
        cursor = conn.cursor()
        k = cursor.execute(command, {"name":name, "price":price, "category":category})

    match(menu):
        case "1":
            for p in k:
                print(f"Название: {p[0]:10}; Цена: {str(p[1]):10}; Категория: {p[2]};")
        case "2":
            for c in k:
                print(c[0])

    
def DB_COMM(menu):
    name = ""
    price = ""
    category = ""
    match(menu):
        case "1":
            command = "SELECT products.name, products.price, categories.name FROM products JOIN categories ON products.category_id=categories.id"

        case "2":
            command = "SELECT name FROM categories"

        case "3":
            name = input("Введите название товара: ").capitalize()
            price = input("Введите цену товара: ")
            category = input("Введите категорию товара: ").capitalize()

            command = "INSERT INTO products(name, price, category_id) SELECT :name,:price,(SELECT id FROM categories WHERE name=:category) WHERE EXISTS(SELECT name FROM categories WHERE name=:category) AND NOT EXISTS (SELECT name, price, category_id FROM products WHERE name=:name AND price=:price AND category_id=(SELECT id FROM categories WHERE name=:category))"

        case "4":
            name = input("Введите название категории: ").capitalize()
            command = "INSERT INTO categories(name) SELECT :name WHERE NOT EXISTS(SELECT name FROM categories WHERE name=:name)"
        
        case "5":
            name = input("Какой продукт удалить? ").capitalize()

            command = "DELETE FROM products WHERE name=:name"
        case _:
            print("Такой команды нет")
            return 0
    
    DB(command, name, price, category, menu)

menu = input("Выберите действие:\n1. Вывести все товары;\n2. Вывести список доступных категорий;\n3. Добавить товар;\n4. Добавить категорию;\n5. Удалить товар.\n\n")

DB_COMM(menu)