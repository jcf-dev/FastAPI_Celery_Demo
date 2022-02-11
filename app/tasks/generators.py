from .worker import celery


@celery.task(name="generate_email_address")
def generate_email_addresses(count: int):
    email = []
    for i in range(count):
        email.append(f'Email {i} here!')
    return email
