from django.shortcuts import render
from django.views import View


class IndexView(View):
    """
    网站首页
    """
    def get(self, request):

        return render(request, 'index.html')
