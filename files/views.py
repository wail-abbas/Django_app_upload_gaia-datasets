from astropy.io.votable import parse

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from .models import VotableFiles, VotableContent, Solutions
from .forms import FilesForm



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

                    votable = parse(f"media/{f}")
                    table = votable.get_first_table()
                    data = table.to_table().to_pandas()
                    for index, row in data.iterrows():
                        file = file_id
                        solution_id = Solutions.objects.filter(solution_id=row['solution_id']).values_list('solution_id', flat=True)
                        if solution_id:
                            solution_id = solution_id[0]
                        else:
                            solution_instance = Solutions(solution_id=row['solution_id'])
                            solution_instance.save()
                            solution_id = solution_instance.solution_id
     
                        content_instance = VotableContent(
                                                        healpix_value = row['healpix'],
                                                        lc_value = row['lc'],
                                                        bc_value =row['bc'],
                                                        dc_value =row['dc'],
                                                        lambda_value = row['lambda'],
                                                        flux_value =row['flux'],
                                                        flux_uncertainty_value =row['flux_uncertainty'],
                                        )
                        content_instance.solution_id_id = int(solution_id)
                        content_instance.file_id = int(file)
                        content_instance.save()
                return render(request, 'files/uploaded.html')
            else:
                return render(request, 'files/error.html')
            

def show_data(request):  
    row_data = VotableContent.objects.all().select_related('solution_id')
    return render(request,"data/list_data.html",{'row_data':row_data})