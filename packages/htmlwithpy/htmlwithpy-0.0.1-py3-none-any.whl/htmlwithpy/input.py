from htmlwithpy.element import Element
class Input(Element):
    def __init__(self,className = None,id = None,styleSheet = False):
        super().__init__(className ,id,styleSheet)
        self.name = "input"
        self.needClosing = False
    def add_type(self,typeOf):
       if(self.customAttr != None):
            self.customAttr = self.customAttr +' type = "'+typeOf+'"'
       else:
            self.customAttr = ' type = "'+typeOf+'"'
    def add_placeholder(self,placeholder):
        if(self.customAttr != None):
            self.customAttr = self.customAttr + ' placeholder = "'+placeholder+'"'
        else:
            self.customAttr = ' placeholder = "'+placeholder+'"'
    def add_value(self,value):
        value = str(value)
        if(self.customAttr != None):
            self.customAttr = self.customAttr + ' value = "'+value+'"'
        else:
            self.customAttr =' value = "'+value+'"'
    def add_content(self, text):
        raise Exception("Cannot add content to input tag , try adding value or placeholder")
