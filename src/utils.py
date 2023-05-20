import json


class Bank:
    def __init__(self, PATH, last_of_transaction=5):
        self.PATH = PATH
        self.last_of_transaction = last_of_transaction
        self.python_list = None
        self.list_of_last_five = None
        self.from_ = None
        self.to = None
        self.date = None
        self.description = None
        self.amount = None
        self.cur_name = None

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
        if not python_list:
            return 'empty python_list'
        if last_of == 0:
            return 'empty python_list'
        for dicts in python_list:
            try:
                if dicts["state"] == "EXECUTED":
                    date_list.append(dicts["date"])
            except KeyError:
                continue
        date_list.sort(reverse=True)
        return date_list[:last_of]

    def __repr__(self):

        self.from_ = (
            f"{' '.join(self.from_.split()[:-1])} "
            f"{self.from_.split()[-1][:4]}"
            f" {self.from_.split()[-1][4:6]}**"
            f" **** {self.from_.split()[-1][-4:]}"
             ) if self.from_ != 'UNKNOW' else 'UNKNOW'

        self.to = f"{self.to[:5]} **{self.to[-4:]}"

        return (f"{self.date[:10].replace('-','.')} {self.description} \n"
                f"{self.from_} -> {self.to} \n"
                f"{self.amount} {self.cur_name}\n"
                )
