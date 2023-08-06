

class Element:
    def __init__(self,className = None,id = None,styleSheet = False):
        self.styleSheet = styleSheet
        self.id = id
        self.className = className  
        self.css = {}
        self.name = None
        self.customAttr = None
        self.content = ""
        self.needClosing = True

    def add_content(self,text):
        self.content = text
    def add_css(self,property = None,value = None):
        if property==None or value == None:
            raise Exception("Property, value can't be None")
        elif type(property) == int:
            raise TypeError("Property can't be Integer")
        elif property.isdigit():
            raise TypeError("Property can't be Integer")
        self.css[property] = value
    def show_css(self):
        for i in self.css:
            print(i,":",self.css[i],";")
    def print_class(self):
        print(".",self.className,"{")
        self.show_css()
        print("}")
    def print_style(self):
        cur = ""
        for i in self.css:
            cur  = cur + i +" :"+ str(self.css[i]) + "; "
            # print(cur)
        return cur
    def generate(self):
        result = "<"+self.name # contains id and class
        if self.className != None:
            result = result + ' class = "'+self.className +'" '
        if self.id != None:
            result = result + 'id = '+self.id + '" ' 
        if self.customAttr != None:
            result = result + self.customAttr
        if self.styleSheet == False and len(self.css) != 0:
            result = result + ' style= " '
            result = result + self.print_style() # all css properties
            result = result + '"'
        if self.styleSheet == True:
            self.print_class()
        result = result + ">"
        print(result)
        print(self.content)
        if(self.needClosing == True):
            print("</"+self.name+">")
if __name__ == "__main__":
    ele = Element()
    ele.add_css("height",100)
    ele.add_css("width",200)
    ele.show_css()
