from django.db import models as m 

class Student(m.Model):
    id = m.AutoField(primary_key=True)

    roll_no = m.IntegerField()
    name = m.TextField(max_length = 40)
    student_class = m.IntegerField()
    department = m.TextField()


