from sqlalchemy import Table, Column, Integer, Text, MetaData, create_engine, select, delete, update
from pyfiglet import figlet_format
import sys
from termcolor import colored
import warnings

# Making our terminal more clean
warnings.filterwarnings("ignore", category=DeprecationWarning)

#Create a table medicine
engine = create_engine("sqlite:///data.db", echo=False)
conn = engine.connect()

meta = MetaData()
medicines = Table(
    'medicines', meta,
    Column('id', Integer, primary_key=True),
    Column('name', Text, unique=True),
    Column('quantity', Integer),
)
meta.create_all(engine)

def main():
    print(figlet_format("MEDICO  INVENTORY", width = 200 ))
    print(figlet_format("Options:", font = "small", width = 200 ))

    options = ['View', 'Insert', 'Search', 'Quantity', 'Delete']
    for option in options:
        print(f"•{option}")

    choice_prompt = input("Choose Option: ").title()
    choice = showOptions(options, choice_prompt)
    if choice == 2:
        print(Search())
    else:
        eval(funCaller(options, choice))

def showOptions(options, choice_prompt):
    try:
        if choice_prompt in options:
            choice = options.index(choice_prompt)
        elif int(choice_prompt) in range(1, len(options) + 1):
            choice = int(choice_prompt) - 1
    except ValueError:
        sys.exit(colored("Please enter the option or the index of the option correctly", "red"))

    return choice

def funCaller(options, choice):
    return f"{options[choice]}()"

def View():
    s = medicines.select()
    result = conn.execute(s)
    for row in result:
        print(row)

def Search(searchable_item=None):
    if searchable_item == None:
        searchable_item = input("Enter medicene name: ").strip().lower()
    s = medicines.select()
    result = conn.execute(s)

    for row in result:
        if searchable_item == row[1]:
            return(row)
    return(colored("NOT FOUND", "red"))

def Insert():
    try:
        id = int(input("ID: "))
        name = input("Name: ").strip()
        quantity = int(input("Quantity: "))
    except ValueError:
        sys.exit(colored("Please enter data in the correct format", "red"))
    ins = medicines.insert().values(id=id, name=name, quantity=quantity)
    conn.execute(ins)
    print(colored("Data added successfully", "green"))
    print(Search(name))

def Delete(name=None):
    if name == None:
        name = input("Name: ")
    try:
        print(colored("Data deleted successfully", "green"))
        print(Search(name))
        conn.execute(medicines.delete().where(medicines.c.name == name))
    except:
        print(colored("Data doesn't exists", "red"))

def Quantity():
    options = ['Add', 'Subtract', 'Modify']
    for option in options:
        print(f" •{option}")
    choice = input(" Choice: ").title()
    if choice in options:
        choice = options.index(choice)
    else:
        sys.exit(colored(" Please enter correct choice", "red"))
    eval(f"{options[choice]}()")

def Add():
    try:
       name = input(" Name: ").strip()
       add = int(input(" Quantity to add: "))
    except ValueError:
       sys.exit(colored(" Enter quantity in correct format"))
    try:
        quantity = Search(name)
    except:
        sys.exit(colored(" Data not Found", "red"))
    stmt = update(medicines).where(medicines.c.name == name).values(quantity = quantity[2] + add)
    conn.execute(stmt)

def Subtract():
    try:
       name = input(" Name: ").strip()
       subb = int(input(" Quantity to subtract: "))
    except ValueError:
       sys.exit(colored(" Enter quantity in correct format"))
    try:
        quantity = Search(name)
    except:
        sys.exit(colored(" Data not Found", "red"))
    if quantity[2] > subb:
        stmt = update(medicines).where(medicines.c.name == name).values(quantity = quantity[2] - subb)
        conn.execute(stmt)
    elif quantity[2] == subb:
        conf = input(" Qauntity is 0 do you want to delete(y/n)")
        if conf.lower() in ["y", "yes"]:
            Delete(name)
        else:
            stmt = update(medicines).where(medicines.c.name == name).values(quantity = quantity[2] - subb)
            conn.execute(stmt)
    else:
        sys.exit(colored(" Not enough quantity left", "red"))

def Modify():
    try:
       name = input(" Name: ").strip()
       new_data = int(input(" New Quantity: "))
    except ValueError:
       sys.exit(colored(" Enter quantity in correct format"))
    try:
        stmt = update(medicines).where(medicines.c.name == name).values(quantity = new_data)
        conn.execute(stmt)
        print(colored(" Quantity modified", "green"))
        print(Search(name))
    except:
        sys.exit(colored(" Data not Found", "red"))


if __name__ == "__main__":
    main()