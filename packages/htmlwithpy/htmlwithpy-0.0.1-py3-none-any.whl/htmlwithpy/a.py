from htmlwithpy.element import Element
class A(Element):
    def __init__(self,className = None,id = None,styleSheet = False):
        super().__init__(className ,id,styleSheet)
        self.name = "a"
    def add_href(self,link):
        self.customAttr = ' href = "'+link+'"'

if __name__ =="__main__":
    a = A()
    a.add_css("h",10)
    a.add_css("width",10)
    a.add_href("google.com")
    a.add_content("some Text")
    a.generate()