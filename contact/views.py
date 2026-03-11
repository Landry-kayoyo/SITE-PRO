from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from .models import MessageContact

def contact_view(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']

            # ✅ Stocker dans la base
            MessageContact.objects.create(
                nom=nom,
                email=email,
                sujet=sujet,
                message=message
            )

            # ✅ Envoyer par email
            send_mail(
                sujet,
                f"Message de {nom} ({email}) :\n\n{message}",
                "Kayoyolandry@gmail.com",  # expéditeur
                ["Kayoyolandry@gmail.com"],  # destinataire
                fail_silently=False,
            )

            success = True
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form, "success": success})
