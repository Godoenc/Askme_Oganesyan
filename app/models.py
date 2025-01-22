from django.contrib.auth.models import User
from django.db import models


class TagManager(models.Manager):
  def get_question_count(self, tag_name):
    """
    Возвращает количество вопросов, связанных с указанным тегом.

    :param tag_name: Название тега (str).
    :return: Количество вопросов (int).
    """
    try:
      tag = self.get(name=tag_name)
      return tag.question_set.count()
    except Tag.DoesNotExist:
      return 0








class UserMan(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  avatar = models.ImageField(null = True, blank = True)
  def __str__(self):
    return self.user.username



class Profile(models.Model):
  user = models.OneToOneField(UserMan, on_delete=models.CASCADE, default=1)
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  registration_at = models.DateField()
  about_me = models.TextField(blank=True)
  #count_of_answers = models.IntegerField(null=True, blank=True)
  #count_of_questions = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return self.name



class Tag(models.Model):
  name = models.CharField(max_length=255)
  #count_of_mentions = models.IntegerField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name



class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  author = models.ForeignKey(Profile, on_delete=models.CASCADE)
  tag = models.ManyToManyField(Tag)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title



class Answer(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  author = models.ForeignKey(Profile, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)



class Likes_Of_Question(models.Model):
  title = models.CharField(max_length=255)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  count_of_goods = models.IntegerField(null=True, blank=True)
  count_of_bads = models.IntegerField(null=True, blank=True)

  class Meta:
    unique_together = (('profile', 'question'),)

  def __str__(self):
    return self.title


class Likes_Of_Answers(models.Model):
  title = models.CharField(max_length=255)
  answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  count_of_goods = models.IntegerField(null=True, blank=True)
  count_of_bads = models.IntegerField(null=True, blank=True)

  class Meta:
    unique_together = (('profile', 'answer'),)

  def __str__(self):
    return self.title

