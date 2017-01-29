#This program uses parameterized SQL statement to manage an SQLite3 database file
#to store chainsaw throwing records.
#The user is able to add, edit, insert, and delete records from the database

import records, choiceProcessor, dbManager
def main():
    #initializes database or reads data from the database file
    dbManager.setup()
    quit = 'q'
    choice = None
    #allow users to loop through choices until they quit
    while choice != quit:
        choice = display_menu_get_choice()
        choiceProcessor.handle_choice(choice)

#displays options to user
def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show records
        2. Add a new record
        3. Update a record
        4. Delete a record
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice
#validates user input data
def getPositiveInt(string):
    #loops until it gets valid user data
    while True:
        #handles common user input errors
        try:
            id = int(string)
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
                string = input()

        except ValueError:
            print('Please enter an integer number')
            string = input()
#allows user to update the catch data for a record
def getUpdateChoice():
    print('''
        Choose a record to update
    ''')
    dbManager.showAll()
    print('Enter the name of the record holder ')
    print('whose catch record has changed: ')
    choice = input()
    #verifize the record exists before trying to update it
    if (dbManager.getRecord(choice)):
        dbManager.updateRec(choice)
    else:
        print('Record not found, please try again')

if __name__ == '__main__':
    main()
