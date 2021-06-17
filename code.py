names = []
phone_numbers = []

def add():
    while True:
        print('enter name')
        name = input("Name: ")
        print('enter phone number')
        phone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
        names.append(name)
        phone_numbers.append(phone_number)
        print('Add another number Y or N')
        s=input()
        if s=='N':
            break
def search():
    search_term = input("\nEnter search term: ")
    print("Search result:")
    if search_term in names:
        index = names.index(search_term)
        phone_number = phone_numbers[index]
        print("Name: {}, Phone Number: {}".format(search_term, phone_number))
    else:
        print("Name Not Found")

def update():
    print('enter name')
    name=input()
    index=names.index(name)
    print("enter new number")
    number=input()
    phone_numbers[index]=number
    print("updated")

def delete():
    print('enter name')
    name=input()
    index=names.index(name)
    if name in names:
        names.remove(name)
        phone_numbers.remove(phone_numbers[index])
    print('deleted')

while True:
    print("choose 1.add ,2.search ,3.update ,4.delete,5.exit")
    choice=int(input())
    if choice==1:
        add()
    elif choice==2:
        search()
    elif choice==3:
        update()
    elif choice==4:
        delete()
    else:
        break
        
