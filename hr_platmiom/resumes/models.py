from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Role(models.TextChoices):
        CANDIDATE = 'CANDIDATE', _('Кандидат')
        HR = 'HR', _('HR-менеджер')
        ADMIN = 'ADMIN', _('Администратор')

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CANDIDATE
    )


class Resume(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='resumes',
        verbose_name=_('Владелец')
    )
    title = models.CharField(max_length=255, verbose_name=_('Название'))
    experience = models.TextField(verbose_name=_('Опыт работы'))
    skills = models.TextField(verbose_name=_('Навыки'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Дата обновления'))

    class Meta:
        verbose_name = _('Резюме')
        verbose_name_plural = _('Резюме')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.owner.username})"