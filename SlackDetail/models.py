from django.db import models

class SlackDetail(models.Model):
    slackUsername = models.CharField(max_length = 50)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField(max_length = 200)

    def __str__(self):
        return self.slackUsername
