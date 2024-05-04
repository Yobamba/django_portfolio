from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

# class Projects(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name

class Project(models.Model):
    # projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
    # text = models.CharField(max_length=300)

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    img_url = models.CharField(max_length=100, default='default_image_url.jpg')
    

    def __str__(self):
        return self.title



