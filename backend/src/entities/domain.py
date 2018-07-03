from typing import Any


class Domain:
    __tablename__ = 'domain'

    def __init__(self, name, url, scrap):
        self.name = name
        self.url = url
        self.scrap = scrap

    def __str__(self):
        return "begin----------\nNAME:" + self.name + "\nURL:" + self.url
