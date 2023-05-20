import utils as ut


def main(PATH):
    operation = ut.Bank(PATH)
    operation.list_of_last_five = operation.open_json(operation.last_of_transaction)
    # operation.final(operation.list_of_last_five, operation.python_list)
    print(operation.list_of_last_five, operation.python_list)


if __name__ == '__main__':
    PATH = 'operations.json'
    main(PATH)
