# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm

SUBJECT = "Регистрация на сайте foodgram"


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         html_message = render_to_string(
    #             "mail.html",
    #             {
    #                 "login": form.cleaned_data["username"],
    #                 "password": form.cleaned_data["password1"],
    #             },
    #         )
    #         message = EmailMessage(
    #             SUBJECT, html_message, to=[form.cleaned_data["email"]]
    #         )
    #         message.content_subtype = "html"
    #         message.send()
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
