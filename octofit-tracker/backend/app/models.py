from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # Duration in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.username} on {self.date}"

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    criteria = models.TextField()

    def __str__(self):
        return self.name

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name