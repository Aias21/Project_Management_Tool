from base_model import BaseModel


class Admin(BaseModel):

    @staticmethod
    def log_in(username, password):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT first_name FROM users WHERE username=%s AND password=%s AND role='Admin'", (username, password))
        result = cursor.fetchone()
        BaseModel.disconnect_db(conn)
        if result:
            print(f'Welcome, {result[0]}!')
            return True
        else:
            print('Username or password incorrect!')
            return False

    @staticmethod
    def create_internal_user(f_name, l_name, email, phone, role, password='password1234'):
        permitted_roles = ['Admin', 'Manager', 'Employee']
        if role not in permitted_roles:
            print('Role can only be "Admin", "Manager" or "Employee"')
            return
        try:
            username = f_name[0:2].lower() + l_name[0:4].lower()
        except IndexError:
            username = f_name[0:2].lower() + l_name.lower()
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''SELECT id,email FROM users WHERE username = %s''', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            print(f'Username "{username}" already exists.')
            BaseModel.disconnect_db(conn)
            return

        cursor.execute('''
                INSERT into users
                    (first_name, last_name, username, password, email, phone, role)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)''', (f_name, l_name, username, password, email, phone, role))

        if role == 'Manager':
            cursor.execute('''INSERT INTO project_managers (user_id) SELECT id FROM users WHERE username = %s''',
                           (username,))
            conn.commit()
        elif role == 'Employee':
            cursor.execute('''INSERT INTO employees (user_id) SELECT id FROM users WHERE username = %s''',
                           (username,))
            conn.commit()
        BaseModel.disconnect_db(conn)

    @staticmethod
    def delete_user(username):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''SELECT id FROM users WHERE username = %s''', (username,))
        user = cursor.fetchone()
        if not user:
            print(f'No user with the username "{username} found!"')
            return
        user_id = user[0]
        cursor.execute('''DELETE FROM users WHERE id = %s''', (user_id,))
        print(f'Username "{username}" has been deleted from the database!')
        BaseModel.disconnect_db(conn)

    @staticmethod
    def reset_user_password(username, new_password):
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        cursor.execute('''UPDATE users SET password = %s WHERE username = %s''', (new_password, username))
        print('Password has been reset!')
        BaseModel.disconnect_db(conn)



