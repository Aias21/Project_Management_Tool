from django.db import models
from pmt.models.task import Task
from pmt.models.employee import Employee


class TaskUpdate(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_timer = models.TimeField(auto_now_add=True)
    stop_timer = models.TimeField()
    finished_task = models.BooleanField()
