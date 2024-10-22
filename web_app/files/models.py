from django.db import models

class VotableFiles(models.Model):
    file_name = models.TextField(max_length=200, blank = True)
    file = models.FileField(max_length=300, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return str(self.file_name)


class Solutions(models.Model):
    solution_id = models.DecimalField(primary_key=True, decimal_places=2, max_digits=100)
    def __str__(self):
       return str(self.solution_id)

class VotableContent(models.Model):
    solution_id = models.ForeignKey(Solutions, related_name='contents', on_delete=models.CASCADE)
    healpix_value = models.DecimalField(decimal_places=2, max_digits=50, blank=True, null=True)
    lc_value = models.DecimalField(decimal_places=2, max_digits=50, blank=True, null=True)
    bc_value = models.DecimalField(decimal_places=2, max_digits=50, blank=True, null=True)
    dc_value = models.DecimalField(decimal_places=2, max_digits=50, blank=True, null=True)
    lambda_value = models.DecimalField(decimal_places=2, max_digits=50, blank=True, null=True)
    flux_value = models.DecimalField(decimal_places=2, max_digits=50, blank=True, null=True)
    flux_uncertainty_value = models.DecimalField(decimal_places=2, max_digits=50, blank=True, null=True)
    file = models.ForeignKey(VotableFiles, related_name='contents', on_delete=models.CASCADE)
