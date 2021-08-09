import datetime

from django.db import models
from users.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
import pusher
from django.utils.timezone import now
pusher_client = pusher.Pusher(
  app_id='1225636',
  key='6eec2d039c51e6fbc58b',
  secret='dac56db940e3d75ecd01',
  cluster='eu',
  ssl=True
)


class Challanges(models.Model):
    Teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='teacher_challanges')
    Title = models.TextField(default='')
    Social = models.IntegerField(default=0)
    Emotional = models.IntegerField(default=0)
    Study = models.IntegerField(default=0)
    Personal = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    Assigned_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    last_date = models.DateField(null=True, blank=True)
    students = models.ManyToManyField(CustomUser, related_name="student_challanges")
    def __str__(self):
        return self.Title

class Completed_Challange(models.Model):
    challenge = models.ForeignKey(Challanges, on_delete=models.CASCADE)
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)


# Send notification when challenge is created
@receiver(m2m_changed, sender=Challanges.students.through)
def send_notification(sender, instance, **kwargs):
    action = kwargs.pop('action', None)

    if action == "post_add":
        for student in instance.students.all():
            pusher_client.trigger(f'my-channel-{student.id}', 'my-event', {'message': 'New challange added'})


class DueChallenge(models.Model):
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    msg = models.TextField(default='',null=True,blank=True)

    def __str__(self):
        return self.msg

class Issue_Challange(models.Model):
        challenge = models.ForeignKey(Challanges, on_delete=models.CASCADE)
        student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

        def __str__(self):
            return str(self.id)

class Forget_password(models.Model):
        student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

        def __str__(self):
            return str(self.student)