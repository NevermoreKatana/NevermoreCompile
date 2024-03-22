from django.shortcuts import render
from django.views import View
# Create your views here.
class DocsMainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'docs.html')

class DocsInstallationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'installation.html')

class DocsStartingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'starting.html')

class DocsVarsView(View):
    def get(self, request, **kwargs):
        return render(request, 'vars.html')
class DocsConditionView(View):
    def get(self, request):
        return render(request, 'conditional.html')

class DocsLoopsView(View):
    def get(self, request):
        return render(request, 'loops.html')
class DocsFunctionsView(View):
    def get(self, request):
        return render(request, 'functions.html')