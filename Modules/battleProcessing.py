import xml.etree.ElementTree as ET
from Modules import TacticsClasses

def toDictionary(element):
    tDict = {}
    for i in element:
        if i.get("type") == "text":
            tDict[i.tag] = i.text
        if i.get("type") == "int":
            tDict[i.tag] = int(i.text)
        if i.get("type") == "float":
            tDict[i.tag] = float(i.text)
        if i.get("type") == "object":
            tDict[i.tag] = All[i.tag][i.text]
        if i.get("type") == "array":
            if i.get("type2") == "text":
                tDict[i.tag] = [j.text for j in i]
            if i.get("type2") == "int":
                tDict[i.tag] = [int(j.text) for j in i]
            if i.get("type2") == "float":
                tDict[i.tag] = [float(j.text) for j in i]
            if i.get("type2") == "object":
                tDict[i.tag] = [All[j.tag][j.text] for j in i]

    return tDict

All = {
"unit": [],
"ability": {},
"race": {},
"job": {},
"weapon": {},
"tile": {}
}

tree = ET.parse("Base.xml")
root = tree.getroot()
battles = root.getchildren()
for i in battles:
    newBattle = []
    grid = []
    for line in fileinput.input(files=i[0]):
        grid += [line.rstrip("\n").split(",")]
    newBattle[0] = grid
    newBattle[1] = []

    for j in i[1]
    newBattle[1] += [TacticsClasses.Person(**toDictionary(j))]
