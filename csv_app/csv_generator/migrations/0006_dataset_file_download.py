# Generated by Django 4.1.7 on 2023-03-06 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0005_dataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='file_download',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]