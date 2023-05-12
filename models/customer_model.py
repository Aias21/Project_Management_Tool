from base_model import BaseModel
from datetime import datetime


class Customer(BaseModel):

    @staticmethod
    def register(f_name, l_name, username, email, phone, password, role='Project Owner'):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''SELECT id FROM users WHERE username = %s''', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            print("Username already exists!")
            BaseModel.disconnect_db(conn)
            return
        cursor.execute('''
                    INSERT into users
                        (first_name, last_name, username, password, email, phone, role)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                       (f_name, l_name, username, password, email, phone, role))
        cursor.execute('''INSERT INTO project_owners (user_id) SELECT id FROM users WHERE username = %s''',
                       (username,))
        BaseModel.disconnect_db(conn)

    @staticmethod
    def log_in(username, password):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT first_name FROM users WHERE username=%s AND password=%s AND role='Project Owner'",
                       (username, password))
        result = cursor.fetchone()
        BaseModel.disconnect_db(conn)
        if result:
            print(f'Welcome, {result[0]}!')
            return True
        else:
            print('Username or password incorrect!')
            return False

    @staticmethod
    def view_available_managers():
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
                SELECT project_managers.manager_id, users.first_name ,users.last_name 
                    FROM project_managers 
                    JOIN users ON project_managers.manager_id = users.id
                    WHERE project_managers.manager_id NOT IN (SELECT projects.project_manager_id from projects)
                        ''')
        results = cursor.fetchall()
        return results

    @staticmethod
    def create_project(name, project_manager_id, username, start_date=datetime.now(), end_date=None, branch=None):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''SELECT project_owners.owner_id from project_owners, users 
                                WHERE username=%s and users.id=project_owners.user_id''', (username,))
        owner_id = cursor.fetchone()
        cursor.execute('''SELECT * from projects WHERE name=%s AND project_owner_id=%s''', (name, owner_id))
        project_exists = cursor.fetchone()
        if project_exists:
            print('You have already created a project with this name!')
            return
        cursor.execute('''
                INSERT INTO projects (name, start_date, end_date, branch, project_manager_id, project_owner_id)
                    VALUES(%s,%s,%s,%s,%s,%s)''', (name, start_date, end_date, branch, project_manager_id, owner_id))
        BaseModel.disconnect_db(conn)

    @staticmethod
    def display_projects(username):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''SELECT project_owners.owner_id from project_owners, users 
                                        WHERE username=%s and users.id=project_owners.user_id''', (username,))
        owner_id = cursor.fetchone()
        cursor.execute('''
                SELECT projects.name, projects.start_date, projects.end_date, project_managers.manager_id,
                    CONCAT_WS(' ',users.first_name,users.last_name) AS Manager 
                FROM projects
                JOIN project_managers ON projects.project_manager_id = project_managers.manager_id
                JOIN users ON users.id = project_managers.user_id
                WHERE projects.project_owner_id = %s''', (owner_id,))
        results = cursor.fetchall()
        BaseModel.disconnect_db(conn)
        return results



if __name__ == '__main__':
    # Customer.register("Don", "Quixote", "donQ", "la.mancha@hespnica.es", '1234123125', 'windmills')
    # Customer.register("Stevan", "Stelle", "stelle", "stevan.st@apfel.de", '000101001', '1234')
    # Customer.log_in('donQ','windmills')
    # print(Customer.view_available_managers())
    # Customer.create_project(name='Microsoft', project_manager_id=2, username='donQ', branch='Web dev')
    # Customer.create_project(name='Moderna', project_manager_id=1, username='donQ', branch='Bio-chemistry')
    # Customer.create_project(name='Birne', project_manager_id=1, username='stelle', branch='Engineering')

    print(Customer.display_projects('stelle'))