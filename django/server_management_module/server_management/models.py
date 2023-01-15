from django.db import models
from register.models import User

class Server(models.Model):
    server_name = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)

    def __str__(self):
        return self.server_name

class Log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_logged = models.DateTimeField('time logged')
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id.profile_id) + " : " + str(self.time_logged)
