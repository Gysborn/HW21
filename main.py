from exeptions import BaseError
from request import Request
from shop import Shop
from store import Store
import time

shop = Shop(
    name='магазин',
    items={
        "коробка": 10,
        "печенька": 3,

    },
    capacity=20,
    max_unique_items=5
)

store = Store(
    name='склад',
    items={
        "коробка": 10,
        "собачка": 7,
        "печенька": 20,
        "молоко": 17,
        "пиво": 11,
        "креветки": 25,
    },
    capacity=100,
)

company = {
    "склад": store,
    "магазин": shop,
}


def main():
    print("Добрго времени суток")

    for storage_name, storage in company.items(): # Выводит содержимое складов
        storage.revision()
        print(f"В {storage_name} храниться:{storage.get_items}")
    while True:
        str_request = input("Введите запрос\nЧтобы закончить введите 's'\n")
        if str_request == 's':
            break
        try:
            request_inst = Request(str_request, company)# Обработчик запроса
        except BaseError as e:
            print(e.message)
            break
        prod_name, amount, storage_in, storage_to = request_inst.request_handler()#Проверка запроса на валидность
        try:
            storage_in.check_in(prod_name, amount)# Проверка наличия товара на складе
        except BaseError as e:
            print(e.message)
            continue
        print("Нужное колличество есть на складе")
        storage_in.remove(prod_name, amount)
        time.sleep(1)

        try:
            storage_to.check_to(prod_name, amount)# Проверка свободного места на складе
        except BaseError as e:
            print(e.message)
            continue
        print("Курьер получил заказ...")
        time.sleep(3)

        print(f"Курьер забрал {amount} {prod_name} со {storage_in.name}")
        time.sleep(1)
        storage_to.add(prod_name, amount)
        print(f"Курьер везет {amount} {prod_name} со {storage_in.name} в {storage_to.name}...")
        time.sleep(7)

        print(f"Курьер доставил {amount} {prod_name} на {storage_to.name}\n")

        time.sleep(3)

        for storage_name, storage in company.items():
            print(f"В {storage_name} храниться: {storage.get_items}")
        time.sleep(3)
        continue


if __name__ == '__main__':
    main()
