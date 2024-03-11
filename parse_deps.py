import yaml

products_versions_path = 'products.txt'
req_path = 'requrements.yml'


# Обработка списка продуктов
def get_prod_versions_list(filepath):
    pnv_list = []
    with open(filepath, 'r') as file:
        lines = file.readlines()

        for line in lines:
            temp = line.replace(':', '')
            pnv_list.append(temp.splitlines())
    return pnv_list


"""
Обработка словаря продуктов. 
При парсинге yml все размещается в словарях.
Заносим данные в один общий словарь, приходим к виду:
products = { 
        Продукт Версия = ['ЗависимыйПродукт Версия', ..., 'ЗависимыйПродукт Версия'],
        ...
        Продукт Версия = ['ЗависимыйПродукт Версия', ..., 'ЗависимыйПродукт Версия'],
        }
"""


def get_dict_of_dependences(prodnvers_list):
    products = {}
    for prod in prodnvers_list:
        with open(f'{prod[0]}/requirements.yml', 'r') as file:
            data = yaml.safe_load(file)
            products = {**products, **data}
    if products:
        for prod in products.keys():
            if products[prod] is None:                           # если зависимости отсутствуют
                products[prod] = []
            else:
                final_dep = []
                for dep in products[prod].keys():
                    temp = str(dep) + ' ' + products[prod][dep]
                    final_dep.append(temp)
                products[prod] = final_dep

        return products

pv_dict = get_prod_versions_list(products_versions_path)
get_dict_of_dependences(pv_dict)

