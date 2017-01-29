import ui, dbManager
import sqlite3
#process choice from user
def handle_choice(choice):
    if choice == '1':
        dbManager.showAll()
    if choice == '2':
        addRecord()
    if choice == '3':
        updateRecord()
    if choice == '4':
        deleteRecord()
    if choice == 'q':
        quit()
#Get new record data
def addRecord():
    name = input('Enter Name of Record Holder: ')
    #enforces uniqueness of primary key
    if (dbManager.getRecord(name)):
        print("This record already exists, choose to update a record")
    else:
        country = input('Enter Country of Record Holder: ')
        stringCatches = input('Enter the recorded number of catches: ')
        catches = ui.getPositiveInt(stringCatches)
        dbManager.addNewRecord(name, country, catches)

def updateRecord():
    ui.getUpdateChoice()

def deleteRecord():
    dbManager.showAll()
    name = input('Enter Name of Record Holder whose Record you want to delete: ')
    #verifies existance of record before trying to delete it/validates input
    if (dbManager.getRecord(name)):
        dbManager.delRecordDB(name)
    else:
        print('Record not found, please try again')
