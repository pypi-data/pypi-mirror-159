# Htmlwithpy

Htmlwithpy is a package which allows users to generate html code using python

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install htmlwithpy
```

```python
import htmlwithpy

```
## Usage
Available Tags are\
1.body\
2.div\
3.span\
4.p( para)\
5.input\
6.img\
7.a (anchor tag)\
**Note: While using tags makesure first letter is capital refer to Example code snippets**
### Constructor
TagName()\
None of these attributes are mandatory\
Attributes :
- className = String
- id = String
- styleSheet = True or False ( if it is true you will get seperate class for css properties)
```python
import htmlwithpy
inp = htmlwithpy.Input(className="header-img",id = "header-1",styleSheet=True)
```
### Common methods
1.add_content(text : **String**) : adds text to the tags\
2.add_css(property : **String**, value :**String or int** : add css property to the tag\
3.show_css() : prints all current css properties\
4.generate() : Finally generates your tag
### Special Methods 
**1.Input**
- add_placeholder(**String**) : set placeholder of input tag to provided value
- add_value(**String**) : set value of input tag to provided value
- add_type(**String**) : set type of input tag to provided value

**2.Img**
- add_src(**String**) : set src of img tag to provided value
- add_alt(**String**) : set alt of input tag to provided value

**3.A (anchor)**
- add_href(**String**) : set href of a(anchor) tag to provided value
## Examples
```python
import htmlwithpy as hwp
inp = hwp.Input(className="form",styleSheet = True)
inp.add_css("height","100px")
inp.add_css("width","100px")
inp.add_placeholder("placeholder")
inp.generate()
```
### Output :
. form {\
height : 100px ;\
width : 100px ;\
}\
<input class = "form"  placeholder = "placeholder">
```python
import htmlwithpy as hwp
body = hwp.Body()
body.add_css("height","100px")
body.add_css("width","100px")
body.add_content("Test Content")
body.generate()
```
Output : 
<body style= " height :100px; width :100px; ">

Test Content
</body>