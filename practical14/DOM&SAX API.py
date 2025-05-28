import xml.dom.minidom
from datetime import datetime

start=datetime.now()
DOMTree = xml.dom.minidom.parse("/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical14/go_obo.xml")
collection = DOMTree.documentElement
terms=collection.getElementsByTagName('term')

ontology_max = {"molecular_function": [],"biological_process": [],"cellular_component": []}
max_count = {"molecular_function": 0,"biological_process": 0,"cellular_component": 0}

for term in terms:
    namespace=term.getElementsByTagName("namespace")[0].firstChild.nodeValue
    name=term.getElementsByTagName("name")[0].firstChild.nodeValue
    is_a=term.getElementsByTagName("is_a")
    is_a_count=len(is_a)

    if namespace in ontology_max:
        if is_a_count > max_count[namespace]:
            ontology_max[namespace] = [(name, is_a_count)]
            max_count[namespace] = is_a_count
        elif is_a_count == max_count[namespace]:
            ontology_max[namespace].append((name, is_a_count))

print("Results from DOM parser:")
for ns, terms in ontology_max.items():
    print(f"Ontology: {ns}")
    for name, is_a_count in terms:
        print(f"  Name: {name}")
        print(f"  Number of <is_a>: {is_a_count}")
        print()

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
        
        self.max_counts = {"molecular_function": {"terms": [], "count": 0},"biological_process": {"terms": [], "count": 0},"cellular_component": {"terms": [], "count": 0}}
        
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
            current_max = self.max_counts[self.namespace]["count"]
            term = (self.name, self.is_a_count)
        if self.is_a_count > current_max:
            self.max_counts[self.namespace]["terms"] = [term]
            self.max_counts[self.namespace]["count"] = self.is_a_count
        elif self.is_a_count == current_max:
            self.max_counts[self.namespace]["terms"].append(term)

parser = xml.sax.make_parser()
Handler = GOHandler()
parser.setContentHandler(Handler)
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
parser.parse('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical14/go_obo.xml')

print("Results from SAX parser:")
for ns, data in Handler.max_counts.items():
    print(f"Ontology: {ns}")
    for name, is_a_count in data["terms"]:
        print(f"  Name: {name}")
        print(f"  Number of <is_a>: {is_a_count}")
        print()

end=datetime.now()
time2=end-start
print(time2)

if time1 > time2:
    print("the time using SAX API is less than time using DOM.")
else:
    print("the time using SAX API is more than time using DOM.")

