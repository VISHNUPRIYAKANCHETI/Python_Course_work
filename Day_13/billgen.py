data={
    'Bag':1000,
    'Bottle':450,
    'Book':50,
    'Box':350,
    'pens':120,
    'pencil':30,
    'Diary':250
}
for i in data:
    print(i.ljust(20),data[i])

product=input("Enter the products: ").split()
bill=0
for i in product:
    print(i.ljust(20),data[i])
    bill+=data[i]
print("Total bill".ljust(20),bill)


