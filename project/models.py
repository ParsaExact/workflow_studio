from django.db import models

class Project(models.Model):
    PROJECT_TYPES = models.CharField(choices=[('LIBRARY', 'LIBRARY'), ('PROCESS', 'PROCESS')])
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Inactive', 'Inactive'), ('Active', 'Active'), ('Completed', 'Completed')])

    def __str__(self):
        return self.name
