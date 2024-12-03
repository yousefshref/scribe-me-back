from django.db import models



class History(models.Model):
    user = models.CharField(max_length=100)
    used_file = models.FileField(upload_to="history")
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


