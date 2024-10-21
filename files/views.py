
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from .models import VotableFiles, VotableContent, Solutions
from .forms import FilesForm
from .tasks import process_file



class experimentfile(View):
    def get(self, request):
        form = FilesForm()
        return render(request, 'files/upload_file.html', context={'form':form})

    def post(self, request):
        if request.method=='POST':
            form = FilesForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            if form.is_valid():
                for f in files:
                    fs = FileSystemStorage()           
                    file_name = fs.save(f.name, f)  
                    file_instance = VotableFiles(file_name = file_name, file=f)
                    file_instance.save()
                    file_id = file_instance.id
                process_file.delay(file_id, file_name)
                    
                return render(request, 'files/uploaded.html')
            else:
                return render(request, 'files/error.html')
            

def show_data(request):  
    row_data = VotableContent.objects.all().select_related('solution_id')
    return render(request,"data/list_data.html",{'row_data':row_data})