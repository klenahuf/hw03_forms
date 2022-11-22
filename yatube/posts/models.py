from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True,)
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        related_name='posts',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        TEXT_LIMIT = 15
        return self.text[:TEXT_LIMIT]

    class Meta:
        ordering = ['-pub_date']
