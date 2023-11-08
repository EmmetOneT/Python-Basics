#inventory = {'Knife':1, 'Health Kit': 3, 'Wood': 5}
##number of Health Kits
#print(inventory['Health Kit'])
#inventory['Knife'] = 2
#print(inventory)
##Adds Gold to end of dictionary
#inventory['Gold'] = 50
#print(inventory)

inventory = {'Knife':1, 'Health Kit': 3, 'Wood': 5}
print(inventory.get('Gold'))
print(inventory.keys())
print(inventory.values())

#Delete from dictionary
inventory.pop('Knife')
print(inventory)