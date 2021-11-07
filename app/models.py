from django.contrib.auth.models import User
from datetime import date
from django.db import models


# Create your models here.
class Tag(models.Model):
    tag_title = models.CharField(max_length=256)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.tag_title


class Profile(models.Model):
    nickname = models.CharField(max_length=256)
    avatar = models.ImageField(blank=True, default='')
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.nickname


class Answer(models.Model):
    text_ans = models.TextField()
    person_ans = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='person_ans', default='')
    que = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='que', default='')

    def __str__(self):
        return ' '.join([self.text_ans[0:10], "..."])


class Question(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=256)
    text_que = models.TextField()
    tag = models.ManyToManyField(Tag, related_name='tag')
    person_que = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='person_que', default='')

    def __str__(self):
        return self.title


class LikeToAns(models.Model):
    like_ans = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='like_ans', default='')

    def __str__(self):
        return str(self.to_ans)


class LikeToQue(models.Model):
    like_que = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='like_que', default='')

    def __str__(self):
        return str(self.to_que)






# class AuthorManager(models.Manager):
#     def young_authors(self):
#         self.filter(birth_date__gt=date(2000, 1, 1))
#
#
# class Author(models.Model):
#     first_name = models.CharField(max_length=256)
#     last_name = models.CharField(max_length=256)
#     birth_date = models.DateField(blank=True, null=True)
#     death_date = models.DateField(blank=True, null=True)
#
#     objects = AuthorManager()
#
#     def __str__(self):
#         return ' '.join([self.first_name, self.last_name])
#
#
# class Book(models.Model):
#     name = models.CharField(max_length=256)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#     published_date = models.DateField(blank=True, null=True)
#     genres = models.ManyToManyField('Genre', related_name='books')
#
#
# class Genre(models.Model):
#     name = models.CharField(max_length=256)
#
#
# class BookInstance(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.PROTECT)
#     STATUS_CHOICE = [
#         ('t', 'Taken'),
#         ('a', 'Available'),
#         ('m', 'Maintenance')
#     ]
#     status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='a')