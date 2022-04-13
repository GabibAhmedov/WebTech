from django.db import models
from django.contrib.auth.models import User


class QuestionsManager(models.Manager):
    def get_hot(self, like_limit):
        result_query = []
        questions = Question.objects.all()
        for question in questions:
            if Like.objects.count_question_likes(question.pk) >= like_limit:
                result_query.append(question)

        return result_query

    def get_tagged_question(self, tag_name):
        return Tag.objects.filter(tag_name__exact=tag_name)[0].question.all()


class Question(models.Model):
    title = models.CharField(max_length=60)
    text = models.CharField(max_length=3000)
    time = models.DateTimeField(auto_now_add=True)

    objects = QuestionsManager()


class AnswerManager(models.Manager):
    def question_answers(self, question_id):
        return Answer.objects.filter(question__pk=question_id)


class Answer(models.Model):
    text = models.CharField(max_length=3000)
    correct = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    objects = AnswerManager()


class ProfileManager(models.Manager):
    def get_avatar(self, user_id):
        avatar = Profile.objects.filter(user__pk=user_id)
        return avatar[0].avatar.url


class Profile(models.Model):
    email = models.CharField(max_length=40)
    login = models.CharField(max_length=40)
    nickName = models.CharField(max_length=40)
    avatar = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = ProfileManager()


class TagManager(models.Manager):
    def question_tags(self, question_id):
        return Tag.objects.filter(question__pk=question_id)


def get_top_tags(self):
    tag_amount = 10
    tags = Tag.objects \
               .values('name') \
               .annotate(total=models.Count('question')) \
               .order_by('-total')[:tag_amount]
    return tags


class Tag(models.Model):
    name = models.CharField(max_length=14)
    question = models.ManyToManyField(Question)

    objects = TagManager()


class LikeManager(models.Manager):
    def count_likes(self, question_id):
        return Like.objects.filter(question__pk=question_id).count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    objects = LikeManager()


class DislikeManager(models.Manager):
    def count_dislikes(self, question_id):
        return Dislike.objects.filter(question__pk=question_id).count()


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    objects = DislikeManager()

# Create your models here.
