# Dictionary - Mutable collection of key-value pairs

dt = {"Name": "Ramakant", 
      "City": "Pune", 
      "Resident": "India", 
      "Tech": [
          "C", 
          "C++", 
          "Python"
          ]}

for data in dt.values():
    print(data)

for key in dt.keys():
    print(key)

for key, value in dt.items():
    print(key, " --> ", value)

print(len(dt))
dt['Name'] = "Rakesh"
dt['Tech'].append("DotNet")

print(dt)

if 'laptop' in dt:
    print(dt['laptop'])
else:
    print("What laptop?")

print(dt.get('laptop'))

print(dt.pop('Name'))
print(dt)

print(dt.popitem())
print(dt)

dt['LaptopOS'] = "Windows"
print(dt)

# Try out iter with sentinel