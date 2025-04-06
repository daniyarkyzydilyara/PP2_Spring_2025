import psycopg2
from connect import connect
from config import load_config

# 2
def add_new_contacts(name, phone_num):
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL add_new_contact(%s,%s)', (name, phone_num))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def add_new_contacts_location(name, city, address):
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL add_new_contact_location(%s,%s,%s)', (name, city, address))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# 5
def del_contact(name):
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL delete_contact(%s)', (name,))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
# entering user name, phone from console
name = input("Input name :")
phone_num = input("Input phone number :")
city = input("Input city :")
address = input("Input address :")
  
if __name__ == '__main__':
    add_new_contacts(name,phone_num)
    add_new_contacts_location(name,city, address)
    del_contact('Jamazan')