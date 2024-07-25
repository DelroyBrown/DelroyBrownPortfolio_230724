# DelroyBrownPortfolio_contact/views.py
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .forms import ContactForm
from django.template.loader import render_to_string


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            email_subject = f"New Contact Form Submission: {subject}"
            email_message = render_to_string(
                "contact/email_template.html",
                {
                    "name": name,
                    "email": email,
                    "subject": subject,
                    "message": message,
                },
            )

            email = EmailMultiAlternatives(
                subject=email_subject,
                body=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=["Delroybrown.db@gmail.com"],
            )
            email.attach_alternative(email_message, "text/html")
            email.send()

            return redirect("DelroyBrownPortfolio_contact:success")
        else:
            messages.error(
                request, "There was an error with your submission. Please try again."
            )

    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})


def success(request):
    return render(request, "contact/success.html")
