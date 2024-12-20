# Generated by Django 4.2.16 on 2024-10-21 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Solutions",
            fields=[
                ("solution_id", models.IntegerField(primary_key=True, serialize=False))
            ],
        ),
        migrations.CreateModel(
            name="VotableFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file_name", models.TextField(blank=True, max_length=200)),
                (
                    "file",
                    models.FileField(
                        blank=True, max_length=300, null=True, upload_to=""
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="VotableContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "healpix_value",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=50, null=True
                    ),
                ),
                (
                    "lc_value",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=50, null=True
                    ),
                ),
                (
                    "bc_value",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=50, null=True
                    ),
                ),
                (
                    "dc_value",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=50, null=True
                    ),
                ),
                (
                    "lambda_value",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=50, null=True
                    ),
                ),
                (
                    "flux_value",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=50, null=True
                    ),
                ),
                (
                    "flux_uncertainty_value",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=50, null=True
                    ),
                ),
                (
                    "file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contents",
                        to="files.votablefiles",
                    ),
                ),
                (
                    "solution_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contents",
                        to="files.solutions",
                    ),
                ),
            ],
        ),
    ]
