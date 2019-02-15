import TacticsClasses
import xml.etree.ElementTree as ET

def toDictionary(element):
    tDict = {}
    for i in element:
        if i.type == "text":
            tDict[i.get("name")] = i.text
        if i.type == "int":
            tDict[i.get("name")] = int(i.text)
        if i.type == "float":
            tDict[i.get("name")] = float(i.text)
        if i.type == "array":
            if i.type2 == "text":
                tDict[i.get("name")] = [j.text for j in i]
            if i.type2 == "int":
                tDict[i.get("name")] = [int(j.text) for j in i]
            if i.type2 == "float":
                tDict[i.get("name")] = [float(j.text) for j in i]
            if i.type2 == "object":
                tDict[i.get("name")] = [All[j.type][j.name] for j in i]

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
        All[j.tag][j.get(name)] = toDictionary(j)
