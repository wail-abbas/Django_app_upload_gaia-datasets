import time
from astropy.io.votable import parse
from celery import shared_task
from .models import VotableFiles, VotableContent, Solutions

@shared_task
def process_file(file_id, file_name):
    time.sleep(10)
    print('start task')
    votable = parse(f"media/{file_name}")
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
    print('start task')