import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 50)
print("{:<50} {:<15} {:<7} {:<7}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    print("{:<50} {:<15} {:<7} {:<7}".format(dn, descr, speed, mtu))