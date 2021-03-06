from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm

SUBJECT = "Регистрация на сайте foodgram"


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        html_message = render_to_string(
            "mail.html",
            {
                "login": form.cleaned_data["username"],
                "password": form.cleaned_data["password1"],
            },
        )
        message = EmailMessage(
            SUBJECT,
            html_message,
            from_email=EMAIL_HOST_USER,
            to=[form.cleaned_data["email"]],
        )
        message.content_subtype = "html"
        message.send()
        return super().form_valid(form)
