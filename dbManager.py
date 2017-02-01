from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base
from records import Record
import ui
#create and/or connect with the database file
#create table and 3 rows of data if it is the first time the application is run
engine = create_engine('sqlite:///chainsawRecordsDB.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
def setup():
    save_session = Session()
    record1 = Record(name = 'Ian Stewart', country = 'Canada', catches = 94)
    record2 = Record(name = 'Aaron Gregg', country = 'Canada', catches = 88)
    record3 = Record(name = 'Chad Taylor', country = 'USA', catches = 78)
    for record in [record1, record2, record3]:
        if not (getRecord(record.name)):
            save_session.add(record)
    save_session.commit()
    save_session.close()

def showAll():
    search_session = Session()
    # Fetch everything.
    for record in search_session.query(Record).all():
        print(record)
    search_session.close()

def addNewRecord(name, country, catches):
    save_session = Session()
    record = Record(name = name, country = country, catches = catches)
    if not (getRecord(record.name)):
        save_session.add(record)
    save_session.commit()
    save_session.close()
#
def getRecord(aname):
    search_session = Session()
    count = search_session.query(Record).filter_by(name = aname).count()
    if ( count > 0):
        search_session.close()
        return True
    else:
        search_session.close()
        return False

def updateRec(aname):
    update_session = Session()
    record = update_session.query(Record).filter_by(name = aname)
    print ('Enter the new number of catches for '+aname)
    stringCa= input()
    catc = ui.getPositiveInt(stringCa)
    record.catches = catc
    update_session.commit()
    update_session.close()
    print('Record Updated')

def delRecordDB(aname):
    delete_session = Session()

    # Query, and delete
    for record in delete_session.query(Record).filter_by(name = aname):
        delete_session.delete(record)
    delete_session.commit()
    delete_session.close()
    print("Record Deleted")
