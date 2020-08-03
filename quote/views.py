from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage

from .models import Quote
from .forms import QuoteForm



def sendEmail():
    #Send mail
    obj = Quote.objects.order_by('-id')
    obj = obj[1]
    msg = EmailMessage(
        f'Заказ №{obj.id}',
        f'Заказ от {obj.username}\nОписание: {obj.description}\nDeadline: {obj.deadline}\nТелефон: {obj.phone}\n',
        'kgorodisky@gmail.com',
        ['mooncity007@ukr.net'])
    msg.content_subtype = "html"
    msg.attach_file(f'media/{obj.document}')
    msg.send()

def upload(request):
    if request.method == "POST":
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            Quote.objects.create(**form.cleaned_data)
            messages.success(request, "You quote was successfuly recieved")
            #sendEmail()
            return redirect('index')
    else:
        form = QuoteForm()
        #messages.error(request, "Quote submition error!")
    context = {
        "form": form
    }
    print(form.errors)
    return render(request, "quote/quote.html", context)
