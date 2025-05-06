import psycopg2
import csv
import os
import time

def create_tables(cur):
    with open('schema.sql', 'r') as file:
        sql_commands = file.read()
        cur.execute(sql_commands)

def clear_tables(cur):
    print("Clearing existing data...")
    cur.execute("DELETE FROM transactions")
    cur.execute("DELETE FROM products")
    cur.execute("DELETE FROM accounts")

def load_csv_data(cur, conn, filename, table_name):
    with open(os.path.join('data', filename), 'r') as file:
        next(file)
        cur.copy_from(file, table_name, sep=',', null='')

def wait_for_postgres(host, database, user, password, max_retries=5, retry_interval=5):
    """Wait for PostgreSQL to be ready to accept connections."""
    retry_count = 0
    while retry_count < max_retries:
        try:
            print(f"Waiting for PostgreSQL to be ready (attempt {retry_count + 1}/{max_retries})...")
            conn = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                connect_timeout=5,
                options='-c statement_timeout=5000 -c client_encoding=UTF8'
            )
            conn.close()
            print("PostgreSQL is ready!")
            return True
        except psycopg2.OperationalError as e:
            retry_count += 1
            if retry_count == max_retries:
                print(f"Failed to connect to PostgreSQL after maximum retries: {e}")
                return False
            print(f"PostgreSQL is not ready yet. Waiting {retry_interval} seconds...")
            time.sleep(retry_interval)
    return False

def main():
    host = os.getenv('POSTGRES_HOST', 'postgres')
    database = os.getenv('POSTGRES_DB', 'postgres')
    user = os.getenv('POSTGRES_USER', 'postgres')
    password = os.getenv('POSTGRES_PASSWORD', 'postgres')
    
    print(f"Connecting to PostgreSQL at {host}...")
    
    if not wait_for_postgres(host, database, user, password):
        print("Could not connect to PostgreSQL. Exiting...")
        return

    try:
        print("Connecting to PostgreSQL...")
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            connect_timeout=5,
            options='-c statement_timeout=5000 -c client_encoding=UTF8'
        )
        cur = conn.cursor()
        
        print("Creating tables...")
        create_tables(cur)
        
        clear_tables(cur)
        
        print("Loading data from CSV files...")
        load_csv_data(cur, conn, 'accounts.csv', 'accounts')
        load_csv_data(cur, conn, 'products.csv', 'products')
        load_csv_data(cur, conn, 'transactions.csv', 'transactions')
        
        print("Data loaded successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        if 'conn' in locals():
            conn.rollback()
        raise
        
    finally:
        if 'cur' in locals() and cur:
            cur.close()
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    main()
