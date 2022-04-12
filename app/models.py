from django.db import models


class LikeSection(models.Model):
    likes = models.
    dislikes =

class Question(models.Model):
    title = models.CharField(max_length=60)
    like = models.ForeignKey(LikeSection, models.PROTECT)

    # Create your models here.
