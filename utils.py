import json


class Bank:
    def __init__(self, PATH, last_of_transaction=5):
        self.PATH = PATH
        self.last_of_transaction = last_of_transaction
        self.python_list = None
        self.list_of_last_five = None

    def open_json(self, last_of):
        try:
            with open(self.PATH) as file:
                file = json.loads(file.read())
        except BaseException:
            file = []
        finally:
            self.python_list = file
            return self.sort_collection(self.python_list, last_of)

    def sort_collection(self, python_list, last_of):
        date_list = []
        for dicts in python_list:
            try:
                if dicts["state"] == "EXECUTED":
                    date_list.append(dicts["date"])
            except KeyError:
                continue
        date_list.sort(reverse=True)
        return date_list[:last_of]

    def __repr__(self):
        return (f"{self.date} {self.description} \n"
               f"{self.from_} -> {self.to} \n"
               f"{self.amount} {self.cur_name}\n"
                )

