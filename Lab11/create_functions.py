import psycopg2
from config import load_config
from connect import connect

def create_func():
    # creating function in PostgreSql database
    commands =(
            # 1 
            """
            CREATE OR REPLACE FUNCTION  get_contLocation_by_name(name_pattern VARCHAR)
            RETURNS TABLE (name VARCHAR, city VARCHAR , address VARCHAR ) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT * FROM contacts_location
            WHERE contacts_location.name LIKE name_pattern;

            END ;$$

            LANGUAGE plpgsql;
            """,
            # 1 
            """
            CREATE OR REPLACE FUNCTION get_all_by_name(name_pattern VARCHAR)
            RETURNS TABLE (name VARCHAR, phone_number VARCHAR) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT * FROM contacts
            WHERE contacts.name LIKE name_pattern;

            END ;$$

            LANGUAGE plpgsql;
            """,
            # 4 
            """
            CREATE OR REPLACE FUNCTION get_with_pagination(lim integer, offst integer)
            RETURNS TABLE (name VARCHAR, phone_number VARCHAR) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT * FROM contacts
            ORDER BY name
            LIMIT lim OFFSET offst;

            END ;$$

            LANGUAGE plpgsql;
            """,
            # 3
            """
            CREATE OR REPLACE FUNCTION insertCorrect_returnIncorrect (contacts VARCHAR[])
            RETURNS TABLE (inc_name VARCHAR, inc_phone_number VARCHAR) AS
            $$
            DECLARE
                contact VARCHAR;
                contact_name VARCHAR;
                phone VARCHAR;
            BEGIN
                FOREACH contact IN ARRAY contacts
                LOOP
                    contact_name := split_part(contact, ',', 1);
                    phone := split_part(contact, ',', 2);
                    IF contact_name!='' AND phone!='' THEN 
                            INSERT INTO contacts(name,phone_number)
                            VALUES (contact_name,phone);
                    ELSE 
                        inc_name = contact_name;
                        inc_phone_number = phone;
                        RETURN NEXT;
                    END IF;
                END LOOP;
            END;
            $$
            LANGUAGE plpgsql;
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
    create_func()