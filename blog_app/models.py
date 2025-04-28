from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):   # внутренний класс Status
        DRAFT = 'DF', 'Draft'   # черновик
        PUBLISHED = 'PB', 'Published'   # черновик

    title = models.CharField(max_length=250)    # Заголовок поста
    slug = models.SlugField(max_length=250, unique_for_date='publish')    # Человеко-понятный URL
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')   # поле Autor
    body = models.TextField()   # Тело поста
    publish = models.DateTimeField(default=timezone.now)    # поле даты публикации
    created = models.DateTimeField(auto_now_add=True)   # поле даты создания
    updated = models.DateTimeField(auto_now=True)   # поле даты изменения
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)   # поле status

    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # пользовательский менеджер

    tags = TaggableManager()

    class Meta:
        ordering = ['-publish'] # сортировка в обратном порядке по полю даты публикации 'publish'
        indexes = [
            models.Index(fields=['-publish']),  # индексирование в обратном порядке
        ]
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def __str__(self):  # Этот метод вызывается, когда нужно получить строковое представление объекта Post
        return self.title   # строковым представлением объекта будет его заголовок

    def get_absolute_url(self):
        return reverse('blog_app:post_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий от {self.name} на {self.post}'

