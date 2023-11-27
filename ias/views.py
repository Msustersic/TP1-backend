from django.views.generic import TemplateView

class IasPage(TemplateView):
   template_name = "index.html"

class ByFunctionPage(TemplateView):
   template_name = "byFunction.html"

class CommentsPage(TemplateView):
   template_name = "comments.html"

class CommentsForm(TemplateView):
   template_name = "fComments.html"

class LoginForm(TemplateView):
   template_name = "fLogin.html"

