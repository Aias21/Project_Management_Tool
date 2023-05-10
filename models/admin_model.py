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
    def create_admin(f_name, l_name, email, phone, role='Admin', password='admin1234'):
        username = f_name[0].lower() + l_name[0:4].lower()
        conn = BaseModel.connect_db()
        cursor = conn.cursor()
        # Check if the entry already exists
        cursor.execute('''SELECT id FROM users WHERE username = %s''', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            # Entry already exists, handle the case accordingly
            print("Entry already exists.")
            BaseModel.disconnect_db(conn)
            return

        cursor.execute('''
                INSERT into users
                    (first_name, last_name, username, password, email, phone, role)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)''', (f_name, l_name, username, password, email, phone, role))
        BaseModel.disconnect_db(conn)

    @staticmethod
    def create_manager(f_name, l_name, email, phone, role='Manager', password='admin1234'):
        username = f_name[0].lower() + l_name[0:4].lower()
        conn = BaseModel.connect_db()
        cursor = conn.cursor()

        # Check if the entry already exists
        cursor.execute('''SELECT id FROM users WHERE username = %s''', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            # Entry already exists, handle the case accordingly
            print("Entry already exists.")
            BaseModel.disconnect_db(conn)
            return

        # Insert the entry into the users table
        cursor.execute('''
                    INSERT INTO users
                        (first_name, last_name, username, password, email, phone, role)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                       (f_name, l_name, username, password, email, phone, role))
        conn.commit()

        # Insert the entry into the project_managers table
        cursor.execute('''INSERT INTO project_managers (user_id) SELECT id FROM users WHERE username = %s''',
                       (username,))
        conn.commit()

        BaseModel.disconnect_db(conn)

if __name__ == "__main__":
    Admin.log_in('aserb', 'admin1234')
    Admin.create_admin('Tom', 'Soysauce', 't.sauce@email.com', '123-321-0123')
    # Admin.create_manager('Jeff', 'Bengos', 'j.bang@hotmail.com', '176-000-6723')