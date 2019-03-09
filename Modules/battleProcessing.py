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
for i in root:
    for j in i:
        # All[j.tag][j.get(name)] = toDictionary(j)
        if j.tag == "ability":
            All[j.tag][j.get("name")] = TacticsClasses.Ability(**toDictionary(j))
        elif j.tag == "race":
            All[j.tag][j.get("name")] = TacticsClasses.Race(**toDictionary(j))
        elif j.tag == "job":
            All[j.tag][j.get("name")] = TacticsClasses.Job(**toDictionary(j))
        elif j.tag == "weapon":
            All[j.tag][j.get("name")] = TacticsClasses.Weapon(**toDictionary(j))
        elif j.tag == "tile":
            All[j.tag][j.get("name")] = TacticsClasses.Tile(**toDictionary(j))
        elif j.tag == "unit":
            All[j.tag] += [TacticsClasses.Person(**toDictionary(j))]
