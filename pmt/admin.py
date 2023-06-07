from django.contrib import admin
from pmt.models.user import User
from pmt.models.manager import Manager
from pmt.models.admin import Admin
from pmt.models.employee import Employee
from pmt.models.customer import Customer
from pmt.models.project import Project
from pmt.models.task import Task
from pmt.models.task_update import TaskUpdate


# Register your models here.
admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskUpdate)
