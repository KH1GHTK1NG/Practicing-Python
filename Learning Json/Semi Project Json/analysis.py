import json
from pprint import pprint

with open("Learning Json\Semi Project Json\catalog.json", "r") as file:
    catalog = json.load(file)

#for product in catalog["product"]:
#   print(product.get("sale_price"))
catalog["product"][0].get("size").append("extra large")

with open("Learning Json\Semi Project Json\catalog.json", "w") as file:
    json.dump(catalog, file, indent=2)

#pprint(catalog["product"][0], width=40)
