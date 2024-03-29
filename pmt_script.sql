--CREATE DATABASE project_management_tool;
--\c project_management_tool

--CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, first_name VARCHAR(20), last_name VARCHAR(20), email VARCHAR(50), phone VARCHAR(20), position VARCHAR(50));
--INSERT INTO users (first_name, last_name, email, phone, position) VALUES
--    ('Bill', 'Gates', 'b.gates@microsoft.com', '+122-(123123) 432', 'Client'),
--    ('Elon', 'Musk', 'e.msuk@tesla.com', '02 2361 123123', 'Client'),
--    ('John', 'Moe', 'j.moe@gmail.com', '04215 125 143', 'Manager'),
--    ('Jane', 'Jill', 'j.j34@hotmail.com', '01051351562', 'Manager'),
--    ('Nathaniel', 'Doe', 'nat.doe27@yahoo.com', '0112351312', 'Employee'),
--    ('Mark', 'Sugarmountain', 'mark.s_tain@gmail.com', '12445115', 'Employee'),
--    ('Marry', 'Virginia', 'virg.marry@outlook.com', '04238 39129', 'Employee'),
--    ('Noah', 'Ark', 'n.ark@boats.com', '010101 0122', 'Employee');

--CREATE TABLE IF NOT EXISTS project_managers (manager_id SERIAL PRIMARY KEY, user_id INT REFERENCES users);
--INSERT INTO project_managers (user_id) VALUES(3),(4);

--CREATE TABLE IF NOT EXISTS project_owners (owner_id SERIAL PRIMARY KEY, user_id INT REFERENCES users);
--INSERT INTO project_owners (user_id) VALUES(1),(2);

--CREATE TABLE IF NOT EXISTS employees (employee_id SERIAL PRIMARY KEY, user_id INT REFERENCES users);
--INSERT INTO employees (user_id) VALUES (5),(6),(7),(8);

--CREATE TABLE IF NOT EXISTS projects (project_id SERIAL PRIMARY KEY, name VARCHAR NOT NULL, start_date DATE, end_date DATE, branch VARCHAR(50), project_manager_id INT REFERENCES project_managers, project_owner_id INT REFERENCES project_owners);
--INSERT INTO projects (name, start_date, end_date, branch, project_manager_id, project_owner_id) VALUES
--    ('Xbox','9 December 2023', '16 November 2024', 'Web development', 1,1),
--    ('FalconX','16 July 2023', '02 February 2025', 'Engineering', 2,2);

--CREATE TYPE status_type AS ENUM('To do','In Progress','Done','Cancelled');
--CREATE TABLE IF NOT EXISTS tasks (task_id SERIAL PRIMARY KEY, name VARCHAR(50), description TEXT, employee_id INT REFERENCES employees, status status_type, project_id INT REFERENCES projects);
--INSERT INTO tasks (name, description, employee_id, status, project_id) VALUES
--    ('Creating web browser for XBox', 'A new widget should be created that allows users to browse the internet freely using one of the installed browsers.', 1, 'To do',1),
--    ('Reverse engineer current fuel system for', 'Maybe the current system could be optimized, consumption data should be split for each phase of consumption.',3, 'In Progress',2),
--    ('Create new software for fuel consumption', 'We will need to analyze the data and see in which phase of we could improve fuel consumption', 2,'To do',2);

--CREATE VIEW view_task_assignments AS SELECT  users.first_name AS Name, users.last_name AS "Family Name", employees.employee_id, projects.name AS Project , tasks.name as Task
--    FROM users, employees, projects, tasks
--    WHERE tasks.employee_id = employees.employee_id AND users.id = employees.user_id AND tasks.project_id = projects.project_id;
--
--CREATE VIEW view_project_executives AS
--SELECT
--  projects.name AS "Project",
--  projects.project_owner_id AS "Owner ID",
--  CONCAT(owners.first_name, ' ', owners.last_name) AS "Project Owner",
--  projects.project_manager_id AS "Manager ID",
--  CONCAT(managers.first_name, ' ', managers.last_name) AS "Project Manager"
--FROM
--  projects
--  JOIN project_owners ON projects.project_owner_id = project_owners.owner_id
--  JOIN users AS owners ON project_owners.user_id = owners.id
--  JOIN project_managers ON projects.project_manager_id = project_managers.manager_id
--  JOIN users AS managers ON project_managers.user_id = managers.id;