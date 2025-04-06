import psycopg2
from connect import connect
from config import load_config

# 1
def get_contacts(name):
    contacts = []
    config = load_config()

    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.callproc('get_all_by_name' ,(name, ))

                rows = cur.fetchall()
                for row in rows:
                    contacts.append(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally :
        return contacts
# 1
def get_contacts_locations(name):
    contacts = []
    config = load_config()

    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.callproc('get_contLocation_by_name' , (name,))

                rows = cur.fetchall()
                for row in rows:
                    contacts.append(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally :
        return contacts

# 4 
def get_contacts_with_pagination(limit, offset):
    contacts = []
    config = load_config()

    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.callproc('get_with_pagination' ,(limit,offset))

                rows = cur.fetchall()
                for row in rows:
                    contacts.append(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally :
        return contacts
    
# 3
def insertCorrect_returnIncorrect(contacts):
    incorrect_contacts = []
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.callproc('insertCorrect_returnIncorrect',(contacts,))

                rows = cur.fetchall()
                for row in rows:
                    incorrect_contacts.append(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally :
        return incorrect_contacts
    
if __name__ == '__main__':
    print(get_contacts(f'%r%'))
    print(get_contacts_locations(f'%r%'))
    print(get_contacts_with_pagination(3,0))
    print(insertCorrect_returnIncorrect([',87008908989', 'Marat,87777007070']))