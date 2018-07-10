from typing import Any


class Domain:
    __tablename__ = 'domain'

    def __init__(self, domain_id, name, url, scrap, encode):
        self.name = name
        self.url = url
        self.scrap = scrap
        self.id = domain_id
        self.encode = encode

    def __str__(self):
        return "begin----------\nNAME:" + self.name + "\nURL:" + self.url

