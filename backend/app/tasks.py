from celery import shared_task

@shared_task
def send_email_task(email):
    # Логика для отправки email
    print(f"Email sent to {email}")