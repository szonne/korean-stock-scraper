import json
from pydash import py_


class Company(object):
    def __init__(self, input_dict):
        self.__dict__ = input_dict or {}

    @property
    def name(self):
        return self.corp_name

    @staticmethod
    def list():
        with open('company_list.json', 'r') as reader:
            data = json.load(reader)
        return [Company(input_dict=val) for val in data['list']]

    @staticmethod
    def find_by_name(name):
        corp_list = Company.list()
        return py_.find(corp_list, lambda c: c.name == name)

    @staticmethod
    def find_by_stock_code(stock_code):
        corp_list = Company.list()
        return py_.find(corp_list, lambda c: c.stock_code == stock_code)

