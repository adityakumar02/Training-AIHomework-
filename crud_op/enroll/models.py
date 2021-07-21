from django.db import models


# class Department(models.Model):
#     title = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title


class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
