from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout


class HomePageView(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'homepage.html')