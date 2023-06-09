from src import utils as ut


def main(PATH):
    """Главная функция"""
    if not PATH or PATH==None:
        return 'zero-PATH incoming'
    operation = ut.Bank(PATH)
    operation.list_of_last_five = operation.open_json(operation.last_of_transaction)
    for date in operation.list_of_last_five:
        for dicts in operation.python_list:
            if not dicts.keys(): #нашелся пустой словарь
                continue
            if date == dicts['date']:
                operation.date = dicts['date']
                operation.description = dicts['description']
                #не у всех словарей есть ключ from
                operation.from_ = dicts['from'] if 'from' in dicts.keys() else 'UNKNOW'
                operation.to = dicts['to']
                operation.amount = dicts['operationAmount']['amount']
                operation.cur_name = dicts['operationAmount']['currency']['name']
        print(operation)
    return 'complited'

if __name__ == '__main__':
    PATH = 'operations.json'
    main(PATH)
