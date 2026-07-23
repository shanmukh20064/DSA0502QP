import pandas as pd
import xml.etree.ElementTree as ET

# Read CSV
df = pd.read_csv("students.csv")

# CSV to JSON
df.to_json("students.json", orient="records", indent=4)

# CSV to XML
root = ET.Element("Students")

for _, row in df.iterrows():
    student = ET.SubElement(root, "Student")
    for col in df.columns:
        child = ET.SubElement(student, col)
        child.text = str(row[col])

tree = ET.ElementTree(root)
tree.write("students.xml")

# Read JSON
json_df = pd.read_json("students.json")
print(json_df)

# Read XML
xml_df = pd.read_xml("students.xml")
print(xml_df)
