from multiprocessing.sharedctypes import Value


def run():
    pass
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Ruben", "lastname": "Jordan"}

    super_list = [
        {"firstname": "Ruben", "lastname": "Jordan"},
        {"firstname": "Dario", "lastname": "Rivera"},
        {"firstname": "Pachon", "lastname": "coshon"},
        {"firstname": "Jose", "lastname": "roca"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5,],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 4.7]
    }

    for key, Value in super_dict.items():
        print(key, "-", Value)

    for i in super_list:
        print(i.items())


if __name__ == "__main__":
    run()