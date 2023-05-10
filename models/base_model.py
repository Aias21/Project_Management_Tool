import psycopg2


class BaseModel:

    @staticmethod
    def connect_db():
        try:
            conn = psycopg2.connect(
                database='pmt',
                user='postgres',
                password='postgres1',
                host='127.0.0.1',
                port='5432'
            )
            return conn
        except psycopg2.Error as error:
            exit(error)



    @staticmethod
    def disconnect_db(connection):
        connection.commit()
        connection.close()


class Initialize(BaseModel):

    @staticmethod
    def initialize_tables():
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            
            CREATE TABLE IF NOT EXISTS 
                    users (id SERIAL PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), username VARCHAR(50), 
                    password VARCHAR(50), email VARCHAR(50), phone VARCHAR(50), role VARCHAR(50));
            
            CREATE TABLE IF NOT EXISTS project_managers (manager_id SERIAL PRIMARY KEY, user_id INT REFERENCES users);
            
            CREATE TABLE IF NOT EXISTS project_owners (owner_id SERIAL PRIMARY KEY, user_id INT REFERENCES users);
            
            CREATE TABLE IF NOT EXISTS employees (employee_id SERIAL PRIMARY KEY, user_id INT REFERENCES users);
            
            CREATE TABLE IF NOT EXISTS projects (
                project_id SERIAL PRIMARY KEY, name VARCHAR NOT NULL, start_date DATE, end_date DATE, branch VARCHAR(50)
                ,project_manager_id INT REFERENCES project_managers, project_owner_id INT REFERENCES project_owners);
            
            CREATE TABLE IF NOT EXISTS tasks (
                task_id SERIAL PRIMARY KEY, name VARCHAR(50), description TEXT, employee_id INT REFERENCES employees, 
                status VARCHAR(50), project_id INT REFERENCES projects
        );
        """)
        BaseModel.disconnect_db(conn)


if __name__ == "__main__":
    Initialize.initialize_tables()

#     conn = BaseModel.connect_db()
#     cursor = conn.cursor()
#     BaseModel.disconnect_db(conn)
#     cursor.execute('SELECT version();')
#     ver = cursor.fetchone()
#     print(ver)