from django.db import models


class Task(models.Model):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    STATUS_CHOICES = [
        (TODO, 'К выполнению'),
        (IN_PROGRESS, 'В процессе'),
        (DONE, 'Выполнено'),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Введите заголовок задачи'
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Детальное описание задачи'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=TODO,
        verbose_name='Статус',
        help_text='Текущий статус выполнения'
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