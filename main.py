import tkinter as tk

#"Iekodētais" grāmatu inventārs
inventory = {
    '1234567890': {
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'ISBN': '1234567890',
        'price': 14.99,
        'quantity': 9
    },
    '7777771111': {
        'title': 'Divergent',
        'author': 'Suzanne Collins',
        'ISBN': '7777771111',
        'price': 12.89,
        'quantity': 4
    },
    '0000000000': {
        'title': 'Twilight',
        'author': 'Stephenie Meyer',
        'ISBN': '0000000000',
        'price': 10.99,
        'quantity': 15
    },
   '98766543210': {
        'title': 'Fifty Shades of Grey',
        'author': 'EL James',
        'ISBN': '98766543210',
        'price': 17.22,
        'quantity': 2
    },
    '1029384756': {
        'title': 'The Lightning Thief',
        'author': 'Rick Riordan',
        'ISBN': '98766543210',
        'price': 14.00,
        'quantity': 20
    }, 
    '1230984576': {
        'title': 'The Giver',
        'author': 'Lois Lowry',
        'ISBN': '1230984576',
        'price': 11.80,
        'quantity': 6
    },
     '2222333345': {
        'title': 'The Giver',
        'author': 'Julie Montegenro',
        'ISBN': '2222333345',
        'price': 6.79,
        'quantity': 22
    }
}
# Pievienot grāmatu funkcionalitāte
def add_book():
    title = input("Book title: ")
    author = input("Author: ")
    
    while True:
        try:
            isbn = input("ISBN: ")
            if isbn in inventory :
                print("This ISBN already exists in inventory.")
            elif  int(isbn) < 0 or not isbn.isdigit():
                print("Enter a valid positive integer for ISBN.")
            else:
                break
        except:
            print("Enter a valid positive integer for ISBN !")
    
    while True:
        try:
            price = float(input("Cena: "))
            if price <=0 :
                print("Price can  not be a negative number or 0!") 
            else:
                break
        except ValueError:
            print("Enter price as decimal")
    
    while True:
        try:
            quantity = int(input("Daudzums: "))
            if quantity <=0 :
                print("Quantity can  not be a negative number or 0!") 
            else:
                break
        except ValueError:
            print("Enter quantity only as number!")

    new_book = {
        'title': title,
        'author': author,
        'ISBN': isbn,
        'price': price,
        'quantity': quantity
    }

    inventory[isbn] = new_book
    print("New book added to inventory.")

# Meklēšana pēc ISBN funkcionalitāte
def search_isbn():
    isbn = input("Book ISBN:")
    if isbn in inventory:
        print("Book found in inventory:")
        print(inventory[isbn])
    else:
        print("Book with ISBN {} not found in inventory.".format(isbn))

#Meklēšana pēc nosaukuma vai autora funkcionalitāte
def search_by_title_author():
    criteria = input("Enter book title or author: ").strip().lower()
    
    matching_books = []

    for isbn, book in inventory.items():
        title = book['title'].lower()
        author = book['author'].lower()

        if criteria in title or criteria in author:
            matching_books.append((isbn, book))

    if matching_books:
        print("Matching books:")
        for isbn, book in matching_books:
            print(f"ISBN: {isbn}")
            print(f"Nosaukums: {book['title']}")
            print(f"Autors: {book['author']}")
            print(f"Cena: {book['price']}")
            print(f"Daudzums: {book['quantity']}")
            print("---------------------")
    else:
        print("No matching books found.")
#Grāmatu saraksts funkcionalitāte

def showAll():
    for book in inventory:
        print(inventory[book])

#Dzēst grāmatu funkcionalitāte
def delete():
    isbn = input("Book ISBN: ")
    if isbn in inventory:
        del inventory[isbn]
        print("Book deleted successfully!")
    else:
        print("Book with ISBN {} not found in inventory.".format(isbn))

