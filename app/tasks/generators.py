from faker import Faker
from app.tasks.worker import celery

faker = Faker()


@celery.task(name="generate_email_address")
def generate_email_addresses(count: int):
    emails = []
    for i in range(count):
        emails.append(faker.ascii_company_email())
    return emails
