from django.db import models

class Workflow(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('archived', 'Archived'),
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # activities = models.ManyToManyField(Activity)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
