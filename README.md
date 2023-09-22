# Medico Inventory
#### Video Demo:  https://youtu.be/5ESiNDIMgk8
#### Description:
Medico Inventory is an application that is meant to serve the purpose of managing medicine inventory of hospitals and pharmacies, so that it become easier for the institutions to manage their medicine supplies and also keep track of the demanding medicines if they wanted to do so in the future with ease. It will also lower the amount of paperwork that has to be done to note down the records of medicines.

Technologies Used:

-Python
-Sqlite (accesed via SqlAlchemy a library in python)
-pyfiglet and termcolor for the decorations of the terminal

## How the application works
The application manages a table called medicines in the data.db database to store all it's information about medicines, till now it stores the id, name, and quantity of the medicines it has, in future we can expand the data to also include manufacture date, expiry date and many more information related to medicines.
Then in the terminal the user get access to manipulate the data via giving simple inputs, like view, insert, search, He/She can also give the number of the input he want to perform, eg. 1 for view, 2 for insert and like this
Then via similiar looking instructions the user can perform the tasks he/she wants to do

## Features:
There are a total of five features till now in this application, but as I said this application can be scaled further in the future, so now let's talk about the existing features
### View:
Via this the user will be able to view the whole inventory at a glance, now the view is the the form of tuples, but it can further be decorated in the future via the help of tabulate library

### Search
Using this the user can search any medicine via it's name, if the medicine is present in the inventory, he/she will get the id, name and the quantity of that medicine and if not then a Not Found Message will be printed

### Quantity
Suppose the user want to add, subtract or just modify the amount of a particular medicine in the inventory, then he can do this via the help of this feature, Thisfeature further contains Add, Subtract and Modify so that the user can perform the required task he wants to perform

### Delete
For deleting a record from the inventory, the user can use this feature, this feature will delete that record that the user prompted and show the details of the record before exiting from the program.

## Possible Improvements:
As improvement is the only constant thing in this universe so,
- Addition of expirey date in the table
- Addition of security fetures like login and logout
- etc.