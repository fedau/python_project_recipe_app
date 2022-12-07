import psycopg2.extras as ext
import os
import psycopg2

def run_sql(sql, values = None):
    conn = None
    results = []

    
    try:
        # postgres_user = os.getenv('POSTGRESS_USER')
        postgres_password =os.getenv('PASSWORD')
        # postgres_dbname = os.getenv('POSTGRES_DBNAME')
        # postgres_host = os.getenv('POSTGRES_HOST')
        # postgres_port = os.getenv('POSTGRES_PORT')
        # postgres_sslmode = os.getenv('POSTGRESS_SSLMODE')
        conn=psycopg2.connect(
            dbname = 'recipe_app_6011', 
            user = 'recipe_app_6011',
            password = postgres_password,
            host = 'recipe-app-6011.postgresql.a.osc-fr1.scalingo-dbs.com',
            port = 40101,
            sslmode= 'prefer'
        )
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results

# connection string connect met environment 
# use connection string here
# and give it as a  environment variable
# something that doesn't  git commit
# in python you have to acces it somehow
# possible gitignore and say what file needs to be ignored and that might be a .env file 
# scalable scaling
# what is an environment variable how does it work and how can we load it in/q



# ssh-keygen enter 