import yaml
import parse_deps as parsedep

# products = {
#     'BILLING 2.3.2': [],
#     'CRM 1.5.5': ['BILLING 2.3.2'],
#     'RATING 2.0.0': ['BILLING 2.3.2'],
#     'QOS 1.2.3': ['RATING 2.0.0'],
#     'MONITORING 1.8.5': ['BILLING 2.3.2', 'CRM 1.5.5', 'QOS 1.2.3', 'RATING 2.0.0']
# }

installation_flags = {
    'BILLING 2.3.2': False,
    'CRM 1.5.5': False,
    'RATING 2.0.0': False,
    'QOS 1.2.3': False,
    'MONITORING 1.8.5': False
}

products_versions_path = 'products.txt'
req_path = 'requrements.yml'

# получение словаря продуктов со списками зависимостей
products_versions_list = parsedep.get_prod_versions_list(products_versions_path)
products = parsedep.get_dict_of_dependences(products_versions_list)

#сразу устанавливаем дочерние продукты, не имеющие зависимостей (помечаем как установленные)
for prod in products.keys():
    if len(products[prod]) == 0:
        installation_flags[prod] = True


def check(req):                     # проверка дочерней зависимости
    if installation_flags[req]:
        return True
    else:
        return False


def check_list(reqs):
    uninstalled = []
    for req in reqs:
        if not check(req):
            uninstalled.append(req)
    return uninstalled


def install(elements):
    for prod in elements:             # prod - каждый продукт
        uninstalled = check_list(products[prod])
        if not uninstalled:
            installation_flags[prod] = True
        else:
            uninstalled.append(prod)
            install(uninstalled)
    print('All dependences installed successfully!')

install(products)

# для просмотра статусов установки:
# print(installation_flags)
