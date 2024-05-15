from collections import UserDict

# We create the Field class, which will be the base class for record fields
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# We create the Name class, which will 
# be used to store the name of the contact
class Name(Field):
    pass

# We create the Phone class, 
# which will be responsible for storing the phone number
class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)

# We create a Record class that will store contact information, 
# including name and phone list       
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


#We create the AddressBook class, which will be responsible for storing and managing records   
class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            
# Creating a new address book
book = AddressBook()

# Create record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Adding John to the address book
book.add_record(john_record)

# Create record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Output of all entries in the book
for name, record in book.data.items():
    print(record)

# Find and edit John's phone
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  

# Search for a specific phone in a John record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}") 

# Deleting Jane's record
book.delete("Jane")
