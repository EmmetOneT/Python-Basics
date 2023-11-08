#List change item
inventory = ['Sword', 'Arrow', 'Bow']
sword = inventory[0]
print(sword)
inventory [1] = 'Heavy Arrow'
print (inventory)

#get list length
print(len(inventory))
#alphabetical value
print(max(inventory))
print(min(inventory))

inventory = ['Sword', 'Arrow', 'Bow']
#add, delete & clear items from list
inventory.append('Helmet')
print(inventory)
#insert at specific index
inventory.insert(0, 'Armour')
print(inventory)

inventory.pop()
print(inventory)

inventory.remove('Sword')
print(inventory)

inventory.clear()