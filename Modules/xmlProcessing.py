import TacticsClasses
import xml.etree.ElementTree as ET

def toDictionary(element):
    tDict = {}
    for i in element:
        if i.type == "text":
            tDict[i.name] = i.text
        if i.type == "int":
            tDict[i.name] = int(i.text)
        if i.type == "float":
            tDict[i.name] = float(i.text)
        if i.type == "array":
            if i.type2 == "text":
                tDict[i.name] = [j.text for j in i]
            if i.type2 == "int":
                tDict[i.name] = [int(j.text) for j in i]
            if i.type2 == "float":
                tDict[i.name] = [float(j.text) for j in i]
            if i.type2 == "object":
                tDict[i.name] = [All[j.type][j.name] for j in i]

    return tDict

All = {
"unit": [],
"enemy": [],
"ability": {},
"race": {},
"job": {},
"weapon": {},
"tile": {}
}

tree = ET.parse()
root = tree.getroot()
for i in root:
    for j in i:
        All[j.tag]
