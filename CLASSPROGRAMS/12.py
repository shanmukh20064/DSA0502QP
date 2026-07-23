import csv
import json
import xml.etree.ElementTree as ET
# ------------------ Read Farmers.csv ------------------
farmers = []
with open("farmers.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        farmers.append(row)
# ------------------ Read Crops.csv ------------------
crops = []
with open("crops.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        crops.append(row)
# ------------------ Read Crops.json ------------------
with open("crops.json", "r") as file:
    crop_json = json.load(file)
print("\nJSON File Loaded Successfully")
# ------------------ Read Crops.xml ------------------
tree = ET.parse("crops.xml")
root = tree.getroot()
print("XML File Loaded Successfully")
# ------------------ Merge Farmer and Crop Data ------------------
print("\nFarmer Details")
print("-" * 70)
total_yield = 0
highest = 0
top_farmer = ""
district_production = {}
for crop in crops:
    fid = crop["Farmer_ID"]
    for farmer in farmers:
        if farmer["Farmer_ID"] == fid:
            print("Farmer ID :", fid)
            print("Farmer Name :", farmer["Farmer_Name"])
            print("District :", farmer["District"])
            print("Crop :", crop["Crop"])
            print("Yield :", crop["Yield"])
            print("-" * 70)
            y = float(crop["Yield"])
            total_yield += y
            if y > highest:
                highest = y
                top_farmer = farmer["Farmer_Name"]
            district = crop["District"]
            if district not in district_production:
                district_production[district] = 0
            district_production[district] += y
# ------------------ Average Yield ------------------
average = total_yield / len(crops)
print("\nAverage Crop Yield =", average)
# ------------------ Top Performing Farmer ------------------
print("\nTop Performing Farmer")
print(top_farmer, "-", highest)
# ------------------ District-wise Production ------------------
print("\nDistrict-wise Production")
for district, production in district_production.items():
    print(district, ":", production)
# ------------------ Export Processed Dataset ------------------
with open("Processed_Crops.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Farmer_ID",
                     "Farmer_Name",
                     "District",
                     "Crop",
                     "Yield"])
    for crop in crops:
        for farmer in farmers:
            if crop["Farmer_ID"] == farmer["Farmer_ID"]:
                writer.writerow([
                    crop["Farmer_ID"],
                    farmer["Farmer_Name"],
                    farmer["District"],
                    crop["Crop"],
                    crop["Yield"]
                ])
print("\nProcessed_Crops.csv created successfully.")