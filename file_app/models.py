from django.db import models

class FileUpload(models.Model):
    upload_time = models.DateTimeField(auto_now_add=True)
    row_count = models.IntegerField()
    unique_identifier = models.CharField(max_length=50, unique=True)

class UserData(models.Model):
    sno = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    date_of_birth = models.DateField()
    file = models.ForeignKey(FileUpload, on_delete=models.CASCADE, related_name='user_data')