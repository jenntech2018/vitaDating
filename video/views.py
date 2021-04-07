from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from video.forms import UploadForm
from video.models import Video
# Create your views here.
class UploadView(View):
    def post(self, request):
        form = UploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            # temp redirect to main, will update to video url after it's working
            return redirect(reverse("main"))
    def get(self, request):
        form = UploadForm()
        return render(request, "video/upload.html", {"form": form})