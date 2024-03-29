from django.shortcuts import render
from django.views import View


class DocsMainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'all_docs/docs.html')


class DocsInstallationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'all_docs/installation.html')


class DocsStartingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'all_docs/starting.html')


class DocsVarsView(View):
    def get(self, request, **kwargs):
        return render(request, 'all_docs/vars.html')


class DocsConditionView(View):
    def get(self, request):
        return render(request, 'all_docs/conditional.html')


class DocsLoopsView(View):
    def get(self, request):
        return render(request, 'all_docs/loops.html')


class DocsFunctionsView(View):
    def get(self, request):
        return render(request, 'all_docs/functions.html')
