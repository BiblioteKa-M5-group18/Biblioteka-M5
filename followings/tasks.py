import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import Following
from copies.models import Copy
from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task


@shared_task
def check_availability_and_send_emails():
    """
    Verifica a disponibilidade das cópias dos livros seguidos pelos usuários e envia um email
    para cada usuário quando houver uma mudança de disponibilidade.
    """
    # busca todos os objetos Following
    followings = Following.objects.all()

    # itera sobre cada objeto Following
    for following in followings:
        # busca todas as cópias do livro associado ao objeto Following
        copies = Copy.objects.filter(book=following.book)

        # verifica se todas as cópias estão emprestadas
        all_loaned = all(copy.is_loaned for copy in copies)

        # verifica se houve uma mudança de disponibilidade desde a última verificação
        if following.is_loaned != all_loaned:
            # atualiza o campo is_loaned do objeto Following
            following.is_loaned = all_loaned
            following.save()

            # envia um email para o usuário informando sobre a mudança de disponibilidade
            subject = f"O livro {following.book.title} está "
            message_template = "email/unavailable.txt" if all_loaned else "email/available.txt"
            message = render_to_string(message_template, {'book': following.book})
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [following.user.email]
            send_mail(subject, message, from_email, recipient_list)


@periodic_task(run_every=crontab(minute='*/1'))
def schedule_check_availability_and_send_emails():
    check_availability_and_send_emails()
