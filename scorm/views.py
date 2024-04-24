from django.shortcuts import render
from django.http import HttpResponse

from scorm.forms import MyScormForm
from scorm.models import MyScormModel
import zipfile  

def scorm_file_reader(request):
    if request.method == 'POST':
        form = MyScormForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        scorm_url = "media/" + str(MyScormModel. objects. last().file)

        # loading the temp.zip and creating a zip object 
        with zipfile.ZipFile(scorm_url, mode="r") as archive:
            archive.extractall(path="static/")

        return render(request, 'result.html',{"scorm_course": "media/unzip/res/index.html"})
    
    else:
        form = MyScormForm()

        return render(request, 'upload.html',  {'form': form})
