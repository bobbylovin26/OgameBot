__author__ = 'adamhammes'

from BeautifulSoup import BeautifulSoup

class World:
    def __init__(self, url = None, fileName = None):
        if fileName:
            f = open(fileName, 'w')
            self.soup = BeautifulSoup(f)
        elif url:
            self.soup = BeautifulSoup(url)

        setData()

    def setData(self):
        self.resources =
