import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("******movie******")
            title = attributes["title"]
            print("Title:", title)
