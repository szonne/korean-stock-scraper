from pydash import py_
import requests
from zipfile import ZipFile
from xml.etree.ElementTree import parse
from io import BytesIO


class Company:
    def __init__(self, input_dict):
        if "crtfc_key" not in input_dict:
            raise ValueError("required API key as crtfc_key")

        self.__dict__ = input_dict or {}

    @property
    def name(self):
        return self.corp_name

    def list(self):
        target_url = "https://opendart.fss.or.kr/api/corpCode.xml"
        res = requests.get(target_url, params={"crtfc_key": self.crtfc_key})
        with ZipFile(BytesIO(res.content)) as zipfile:
            zipfile.extractall("corpCode")

        xmlTree = parse("corpCode/CORPCODE.xml")
        root = xmlTree.getroot()
        corp_list = []
        for item in root.findall("list"):
            corp_list.append(
                Company(
                    {
                        "corp_code": item.findtext("corp_code"),
                        "corp_name": item.findtext("corp_name"),
                        "stock_code": item.findtext("stock_code"),
                        "modify_date": item.findtext("modify_date"),
                        **self.__dict__,
                    }
                )
            )

        return corp_list

    def find_by_name(self, name):
        corp_list = self.list()
        return py_.find(corp_list, lambda c: c.name == name)

    def find_by_stock_code(self, stock_code):
        corp_list = self.list()
        return py_.find(corp_list, lambda c: c.stock_code == stock_code)
