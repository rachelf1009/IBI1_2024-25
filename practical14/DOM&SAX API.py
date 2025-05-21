import xml.dom.minidom
from datetime import datetime

start=datetime.now()
DOMTree = xml.dom.minidom.parse("/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical14/go_obo.xml")
collection = DOMTree.documentElement
terms=collection.getElementsByTagName('term')

max_term={"molecular_function": {"name": "", "count":0},
          "biological_process": {"name": "","count": 0},
          "cellular_component": {"name":"","count": 0}}

for term in terms:
    namespace=term.getElementsByTagName("namespace")[0].firstChild.nodeValue

    name=term.getElementsByTagName("name")[0].firstChild.nodeValue

    is_a=term.getElementsByTagName("is_a")
    is_a_count=len(is_a)

    if namespace in max_term:
        if is_a_count> max_term[namespace]["count"]:
            max_term[namespace]={'name': name, "count":is_a_count}
print(max_term)
end=datetime.now()
time1=end-start
print(time1)

import xml.sax
start=datetime.now()

class GOHandler (xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.name = ""
        self.namespace = ""
        self.is_a_count = 0
        
        self.max_counts = {"molecular_function": {"name": "", "count":0},
          "biological_process": {"name": "","count": 0},
          "cellular_component": {"name":"","count": 0}}

    def startElement(self, tag,attributes):
        self.current_element = tag
        if tag == "term":
            self.name=''
            self.namespace=''
            self.is_a_count=0
        if self.current_element=="is_a":
            self.is_a_count+=1 
    
    def characters(self, content):
        if self.current_element =='namespace':
            self.namespace+=content.strip()
        elif self.current_element=='name':
            self.name+=content.strip()
       

        
        
            
    def endElement(self, tag):
        if tag == "term":
            if self.namespace in self.max_counts:
                if self.is_a_count > self.max_counts[self.namespace]["count"]:
                    self.max_counts[self.namespace] = {"name":self.name, "count":self.is_a_count}


parser = xml.sax.make_parser()
Handler = GOHandler()
parser.setContentHandler(Handler)
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
parser.parse('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical14/go_obo.xml')

print(Handler.max_counts)
end=datetime.now()
time2=end-start
print(time2)

if time1 > time2:
    print("the time using SAX API is less than time using DOM.")
else:
    print("the time using SAX API is more than time using DOM.")

