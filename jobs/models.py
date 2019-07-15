from django.db import models


class Job(models.Model):
    SENIORITY_LEVEL_CHOICES = [
        ('JUNIOR', 'Junior'),
        ('MIDDLE', 'Middle'),
        ('SENIOR', 'Senior'),
        ('TECH_MANAGEMENT', 'Tech Management'),
    ]

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    seniority_level = models.CharField(max_length=15, choices=SENIORITY_LEVEL_CHOICES)
    salary = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.title
