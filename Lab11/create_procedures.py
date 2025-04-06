import psycopg2
from config import load_config
from connect import connect

def create_proc():
    # creating procedure in PostgreSql database
    commands = (
        # 2 
        """
        CREATE OR REPLACE PROCEDURE add_new_contact(
            new_name VARCHAR, 
            new_phone_num VARCHAR
            ) 
        AS $$
        BEGIN 
            INSERT INTO contacts(name, phone_number)
            VALUES(new_name, new_phone_num)
            ON CONFLICT (name)
            DO UPDATE SET  
                name = EXCLUDED.name,
                phone_number = EXCLUDED.phone_number;

        END;
        $$
        LANGUAGE PLPGSQL;
        """,
        """
        CREATE OR REPLACE PROCEDURE add_new_contact_location(
            new_name VARCHAR, 
            new_city VARCHAR,
            new_address VARCHAR
            ) 
        AS $$
        BEGIN 
            INSERT INTO contacts_location(name, city, address)
            VALUES(new_name, new_city, new_address)
            ON CONFLICT (name)
            DO UPDATE SET  
                name = EXCLUDED.name,
                city = EXCLUDED.city,
                address = EXCLUDED.address;

        END;
        $$
        LANGUAGE PLPGSQL;
        """,
        # 5
        """
        CREATE OR REPLACE PROCEDURE delete_contact(name_del VARCHAR) 
        AS $$
        BEGIN 

            DELETE FROM contacts
            WHERE name = name_del;

        END;
        $$
        LANGUAGE PLPGSQL;
        """
    )
    try:
        config = load_config()
        with connect(config) as conn :
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError,Exception ) as error:
        print(error)

if __name__ == "__main__":
    create_proc()