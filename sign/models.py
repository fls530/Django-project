from django.db import models


# Create your models here.
# 发布会表
class Event(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField('event time')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 嘉宾表
class Guest(models.Model):
    # 此处查询文件，缺少属性 on_delete=models.DO_NOTHING，只需在后面加上即可
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    class Meta:

        unique_together = ("event", "phone")

    def __str__(self):
        return self.realname
