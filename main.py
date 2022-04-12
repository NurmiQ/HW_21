from logistics import Store, Shop, Request

if __name__ == '__main__':
    shop = Shop()
    shop.add("печеньки", 4)
    shop.add("шоколад", 5)
    shop.add("лимонад", 2)
    shop.add("бананы", 10)
    store = Store()
    store.add("яблоки", 5)

    user_str = input()
    user_str_list = user_str.split(" ")
    is_error = False

    try:
        user_str_list[1] = int(user_str_list[1])
    except:
        print("Введите число")
        is_error = True

    if ("забрать" or "доставить") not in user_str_list[0].lower():
        print("Введите забрать или доставить")
        is_error = True
    elif ("магазин" or "склад") not in user_str_list[4].lower():
        print("Введите место назначения")
        is_error = True
    if not is_error:
        r = Request(user_str)
        print(r)
        if "магазин" in r.from_:
            print("Доставка возможна только со склада")
        elif "склад" in r.from_:
            if r.product in store.get_items():
                if r.amount <= store.get_items()[r.product]:
                    print("Нужное количество есть на складе")
                    print("Курьер забрал товар со склада")
                    print("Курьер везет товар со склада в магазин")
                    if sum(shop.get_items().values())+int(r.amount) <= shop.capacity:
                        print("Курьер доставил товар в магазин")
                        store.remove(r.product, r.amount)
                        shop.add(r.product, r.amount)
                    else:
                        print("В магазине не достаточно места, попробуйте уменьшить кол-во товара")

                else:
                    print("На складе не достаточно товара, попробуйте заказать меньше")
            else:
                print("Такого товара нет на складе")

        print("На складе хранится:")
        for key, value in store.items.items():
            print(key, value)

        print("В магазине хранится:")
        for key, value in shop.items.items():
            print(key, value)