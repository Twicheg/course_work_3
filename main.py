import utils as ut


def main(PATH):
    operation = ut.Bank(PATH)
    operation.list_of_last_five = operation.open_json(operation.last_of_transaction)
    # z=operation.ready_for_print(operation.python_list,operation.list_of_last_five)
    # print(operation.list_of_last_five,operation.python_list)
    # print(f'{operation.list_of_last_five},\n {operation.python_list}')
    for i in operation.list_of_last_five:
        for j in operation.python_list:
            if not j.keys():
                continue
            if i == j['date']:
                operation.date = j['date']
                operation.description = j['description']
                operation.from_ = j['from'] if 'from' in j.keys() else 'UNKNOW'
                operation.to = j['to']
                operation.amount = j['operationAmount']['amount']
                operation.cur_name = j['operationAmount']['currency']['name']
        print(operation)


if __name__ == '__main__':
    PATH = 'operations.json'
    main(PATH)
