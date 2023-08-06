from htmlwithpy.element import Element
class Img(Element):
    def __init__(self,className = None,id = None,styleSheet = False):
        super().__init__(className ,id,styleSheet)
        self.name = "img"
        self.needClosing = False
    def add_alt(self,alt):
       if(self.customAttr != None):
            self.customAttr = self.customAttr +' alt = "'+alt+'"'
       else:
            self.customAttr = ' alt = "'+alt+'"'
    def add_src(self,src):
        if(self.customAttr != None):
            self.customAttr = self.customAttr + ' src = "'+src+'"'
        else:
            self.customAttr = ' src = "'+src+'"'
    def add_content(self, text):
        raise Exception("Cannot add content to image tag , try adding alt")


