from cgitb import text
from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'ia/ia_index.html')

class Index(View):
    def get(self, request):
        return render(request, "ia/ia_index.html")

    def post(self, request):
        texte = request.POST.get("search", "")
        return render(request, "ia/ia_index.html", {"texte_recherche": texte})