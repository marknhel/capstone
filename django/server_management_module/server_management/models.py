from django.db import models
from register.models import User


class Log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_logged = models.DateTimeField('time logged')

    def __str__(self):
        return str(self.user_id.profile_id) + " : " + str(self.time_logged)
