from django.db import models
from pmt.models.project import Project
from pmt.models.employee import Employee


class Task(models.Model):
    STATUSES = (
        ('TD', 'To Do'),
        ('IP', 'In Progress'),
        ('F', 'Finalized'),
        ('C', 'Cancelled'),
    )
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUSES)
    time_spent = models.DurationField()

