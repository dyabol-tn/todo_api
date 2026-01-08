from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    STATUS_CHOICES = [
        (TODO, 'К выполнению'),
        (IN_PROGRESS, 'В процессе'),
        (DONE, 'Выполнено'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Пользователь'
    )

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=TODO,
        verbose_name='Статус'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id}: {self.title} ({self.status})"