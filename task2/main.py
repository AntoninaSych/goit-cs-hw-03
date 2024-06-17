from pymongo import MongoClient
from bson.objectid import ObjectId
from faker import Faker

# Підключення до MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['cat_database']
collection = db['cats']

fake = Faker()

# Функція для додавання випадкових записів
def seed_data(n):
    for _ in range(n):
        cat = {
            "name": fake.first_name(),
            "age": fake.random_int(min=1, max=20),
            "features": [fake.word() for _ in range(3)]
        }
        collection.insert_one(cat)

# Читання всіх записів
def read_all():
    for cat in collection.find():
        print(cat)

# Читання запису за ім'ям
def read_by_name(name):
    cat = collection.find_one({"name": name})
    print(cat)

# Оновлення віку кота за ім'ям
def update_age_by_name(name, age):
    collection.update_one({"name": name}, {"$set": {"age": age}})

# Додавання нової характеристики до списку features за ім'ям
def add_feature_by_name(name, feature):
    collection.update_one({"name": name}, {"$push": {"features": feature}})

# Видалення запису за ім'ям
def delete_by_name(name):
    collection.delete_one({"name": name})

# Видалення всіх записів
def delete_all():
    collection.delete_many({})

# Приклад використання функцій
if __name__ == "__main__":
    # Заповнення бази даних випадковими даними
    seed_data(10)

    # Виведення всіх записів
    print("All cats:")
    read_all()

    # Виведення запису за ім'ям
    print("\nCat by name:")
    read_by_name("barsik")

    # Оновлення віку кота
    update_age_by_name("barsik", 5)

    # Додавання нової характеристики
    add_feature_by_name("barsik", "чорний хвіст")

    # Видалення запису за ім'ям
    delete_by_name("barsik")

    # Видалення всіх записів
    delete_all()
