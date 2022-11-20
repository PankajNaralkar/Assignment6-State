import json
dictionary = {
    "Andhra Pradesh": "Hyderabad",
    "Arunachal Pradesh": "Itanagar",
    "Assam ": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
   
}
 
with open("State.json", "w") as outfile:
    json.dump(dictionary, outfile)