from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    account = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    roles = models.ManyToManyField(to='Role', through='UserRole')
    scheduling = models.ManyToManyField(to='Scheduling', through='UserScheduling')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'tb_user'


class UserRole(models.Model):
    ur_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, db_column='user_id')
    role = models.ForeignKey(to='Role', on_delete=models.PROTECT, db_column='role_id')

    class Meta:
        db_table = 'tb_user_role'
        unique_together = (('user', 'role'),)


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=20,unique=True)

    class Meta:
        db_table = 'tb_role'


class UserScheduling(models.Model):
    us_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, db_column='user_id')
    scheduling = models.ForeignKey(to='Scheduling', on_delete=models.PROTECT, db_column='scheduling_id')
    is_on = models.BooleanField(default=False)

    class Meta:
        db_table = 'tb_user_scheduling'
        unique_together = (('user', 'scheduling'),)


class Scheduling(models.Model):
    scheduling_id = models.AutoField(primary_key=True)
    scheduling_name = models.CharField(max_length=20,unique=True)
    scheduling_time = models.CharField(unique=True, max_length=10)

    class Meta:
        db_table = 'tb_scheduling'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=20)
    event_type = models.ForeignKey(to='EventType', on_delete=models.PROTECT, db_column='type_id')
    event_detail = models.CharField(max_length=255)
    event_applicant = models.CharField(max_length=10)
    applicant_tel = models.CharField(max_length=12)
    event_addr = models.CharField(max_length=50)
    event_adder = models.ForeignKey(to='User', on_delete=models.PROTECT, db_column='adder_user_id',
                                    related_name='adder_user')
    event_solve = models.ForeignKey(to='User', on_delete=models.PROTECT, db_column='solver_user_id',
                                    related_name='solver_user')
    event_main_deal = models.ForeignKey(to='User', on_delete=models.PROTECT, db_column='main_deal_user_id',
                                        related_name='main_deal')
    event_auxiliary_deal = models.ForeignKey(to='User', on_delete=models.PROTECT, db_column='auxiliary_deal_user_id',
                                             related_name='auxiliary_deal', null=True)
    event_start_time = models.DateTimeField(auto_now_add=True)
    event_end_time = models.DateTimeField(null=True)
    is_deal = models.BooleanField(default=False)

    class Meta:
        db_table = 'tb_event'


class EventType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)
    type_score = models.IntegerField()

    class Meta:
        db_table = 'tb_event_type'


class Leave(models.Model):
    leave_id = models.AutoField(primary_key=True)
    leave_user = models.ForeignKey(to='User',on_delete=models.PROTECT, db_column='user_id')
    leave_time = models.DateField()
    leave_reason = models.CharField(max_length=255)
    is_permit = models.BooleanField(default=False)

    class Meta:
        db_table = 'tb_leave'

