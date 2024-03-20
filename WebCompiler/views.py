from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.http import HttpResponse
from WebCompiler.forms import CompilerForm
from WebCompiler.services import online_compile
from django.http import FileResponse
from WebCompiler.services import tmp_dir
import os
def download_file(request, filename):
    response = FileResponse(open(os.path.join(tmp_dir, filename), 'rb'))
    return response

class HomePageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'homepage.html')


class OnlineCompilerView(FormView):
    template_name = "compiler.html"
    form_class = CompilerForm

    def form_valid(self, form):
        code = form.cleaned_data['input_code']
        result_compile = online_compile(code)
        if 'error' in result_compile:
            return render(self.request,
                          'compiler.html',
                          {'form': form,
                           'output': result_compile['error']})
        return render(self.request,
                      'compiler.html',
                      {'form': form,
                       'output': result_compile['output'],
                       'ast_file': result_compile['ast_file'],
                       'll_file': result_compile['ll_file'],
                       'll_optimize_file': result_compile['ll_opt_file'],
                       'executable_file': result_compile['executable_file']})

    def get_success_url(self):
        return self.request.path
