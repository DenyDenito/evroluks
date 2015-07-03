from django import template
from django.core.mail import send_mail
from django.contrib import messages
from main.forms import OrderForm

register = template.Library()


@register.inclusion_tag('orderform_tag.html', takes_context=True)
def show_orderform(context):
    request = context['request']
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            date_execution = form.cleaned_data['date_execution']
            address = form.cleaned_data['address']
            message = form.cleaned_data['message']
            form.save()
            recipients = ['testingmy@yandex.ru']
            text_content = 'Имя: {}\n{}\nУдобное время: {}\nТелефон: {}\nПочта: {}\nАдрес: {}'.format(
                message, date_execution.strftime("%d.%m.%Y %H:%M"), name, phone, email, address)
            html_content = '<p>Имя: {}</p><p>{}</p><p>Удобное время: {}</p><p>Телефон: {}</p><p>Почта: {}</p><p>Адрес: {}</p>'.format(
                message, date_execution.strftime("%d.%m.%Y %H:%M"), name, phone, email, address)
            send_mail(u'Тест', text_content, 'testingmy@yandex.ru', recipients, fail_silently=True, auth_user=None,
                      auth_password=None, connection=None, html_message=html_content)
            messages.success(request, 'Поступила новая заявка, номер для связи: ' + phone + '  E-mail: ' + email)
            form = OrderForm()
    else:
        form = OrderForm()
    return {"form": form}
