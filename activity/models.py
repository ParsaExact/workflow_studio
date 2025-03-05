from django.db import models

# Create your models here.
class Activity(models.Model):
    TYPE_CHOICES = (
        ('sendEmail', 'Send Email'),
        ('readFile', 'Read File'),
        ('invokeWorkflow', 'Invoke Workflow'),
    )
    
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    parameters = models.JSONField()  # Requires PostgreSQL
    next_activities = models.ManyToManyField('self', symmetrical=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name