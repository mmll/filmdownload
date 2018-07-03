class Film:
    __tablename__ = 'film'

    def __init__(self, domain, title, link, description):
        self.title = title
        self.description = description
        self.domain = domain
        self.link = link

    def serialize(self):
        return {
            'title': self.title,
            'description': self.description,
            'domain': self.domain,
            'link': self.link
        }

    def __str__(self):
        return "begin----------\nTITLE:" + self.title + "\nDESCRIPTION:" + self.description + "\nDOMAIN:" + self.domain + "\nLINK:" + self.link + "\n---------end\n"
