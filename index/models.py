from django.db import models
from django.utils import timezone


class Story(models.Model):
    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
   

    def __str__(self):
        return self.title


class StoryDetail(models.Model):
    #id = models.AutoField(primary_key=True)
    story = models.ForeignKey(Story,on_delete=models.CASCADE)
    detail = models.CharField(max_length=200)
    fisrt = models.BooleanField()

    def __str__(self):
        return self.detail


class Answers(models.Model):
    #id = models.AutoField(primary_key=True)
    storydetail = models.ForeignKey(StoryDetail,on_delete=models.CASCADE)
    storyid = models.CharField(max_length=200)
    adetail = models.CharField(max_length=200)
    returnSdId= models.CharField(max_length=200)

    def __str__(self):
        return self.adetail
