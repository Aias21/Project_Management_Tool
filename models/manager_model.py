from base_model import BaseModel
from datetime import timedelta

class Manager(BaseModel):

    @staticmethod
    def log_in(username, password):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT first_name FROM users WHERE username=%s AND password=%s AND role='Manager'",
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
    def display_assigned_projects(manager_id):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM projects WHERE project_manager_id=%s''', (manager_id,))
        results = cursor.fetchall()
        if not results:
            return 'No projects have been assigned to you!'
        return results

    @staticmethod
    def estimate_project(project_id, estimation_in_days):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''SELECT start_date FROM projects WHERE project_id=%s''', (project_id,))
        try:
            start_date = cursor.fetchone()[0]
        except TypeError:
            BaseModel.disconnect_db(conn)
            return 'No project with this id!'
        end_date = start_date + timedelta(days=estimation_in_days)
        cursor.execute('''UPDATE projects SET end_date=%s WHERE project_id=%s''', (end_date, project_id))
        BaseModel.disconnect_db(conn)

    @staticmethod
    def view_employees():
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT employees.employee_id, CONCAT_WS(' ',users.first_name,users.last_name) AS name , users.username ,
                users.email, users.phone 
                FROM employees
                JOIN users on employees.user_id=users.id''')
        employees = cursor.fetchall()
        return employees

    @staticmethod
    def create_task(manager_id, name, project_id, employee_id, description='', status='To do'):
        statuses = ['to do', 'in progress', 'done', 'cancelled']
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''SELECT project_id FROM projects WHERE project_manager_id=%s''', (manager_id,))
        available_projects = cursor.fetchall()[0]
        if project_id in available_projects and status.lower() in statuses:
            cursor.execute("SELECT 1 FROM tasks WHERE name = %s AND project_id = %s AND employee_id = %s",
                           (name, project_id, employee_id))
            exists = cursor.fetchone()
            if exists:
                print("Entry already exists")
            else:
                cursor.execute(
                    "INSERT INTO tasks (name, description, employee_id, status, project_id) VALUES (%s, %s, %s, %s, %s)",
                    (name, description, employee_id, status, project_id)
                )
                BaseModel.disconnect_db(conn)
        else:
            print('Project not found')
            return



    @staticmethod
    def reassign_task():
        pass

if __name__ == '__main__':
#     Manager.log_in('losmit', 'password1234')
#     print(Manager.display_assigned_projects(1))
#     print(Manager.display_projects_to_estimate(1))
#     Manager.estimate_project(6, 13)
#     print(Manager.view_employees())
    Manager.create_task(manager_id=1, name='Task1',description='do somthing about that', project_id=7, employee_id=2)