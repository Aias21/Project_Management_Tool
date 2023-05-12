from base_model import BaseModel


class Employee(BaseModel):

    @staticmethod
    def log_in(username, password):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT first_name FROM users WHERE username=%s AND password=%s AND role='Employee'",
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
    def update_task_work():
        pass

    @staticmethod
    def update_task_status():
        pass

if __name__ == '__main__':
    Employee.log_in('yemast', 'password1234')