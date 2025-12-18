from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import BlogDetail


@receiver(post_save, sender=BlogDetail)
def send_congratulation_on_100_views(sender, instance, **kwargs):
    """Отправляет email при достижении 100 просмотров"""
    if instance.views_counter == 100:
        subject = f'🎉 Статья "{instance.title}" достигла 100 просмотров!'

        message = f"""
        Поздравляем! Статья "{instance.title}" достигла 100 просмотров.

        Детали:
        - ID: {instance.pk}
        - Просмотры: {instance.views_counter}
        - Дата создания: {instance.created_at}
        """

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )