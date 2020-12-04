from django.core.mail import send_mail
from celery import task
from Bookies.models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"Bookies: Order nr. {order.id}"
    message = f"Dear {order.user.first_name} {order.user.first_name}," \
              f"You have successfully placed an order."
    mail_sent = send_mail(subject,
                          message,
                          'atajner69@gmail.com',
                          {order.user.email})
    return mail_sent