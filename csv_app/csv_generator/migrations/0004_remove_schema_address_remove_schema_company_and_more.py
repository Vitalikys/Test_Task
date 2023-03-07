# Generated by Django 4.1.7 on 2023-03-05 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0003_rename_age_schema_address_schema_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schema',
            name='address',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='company',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='date_fake',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='domain_name',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='email',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='integer_num',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='job',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='max_value_int',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='min_value_int',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='text',
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=30, null=True)),
                ('job', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('domain_name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('company', models.CharField(blank=True, max_length=20, null=True)),
                ('text', models.CharField(blank=True, max_length=20, null=True)),
                ('integer_num', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
                ('date_fake', models.CharField(blank=True, max_length=20, null=True)),
                ('min_value_int', models.IntegerField(blank=True, null=True)),
                ('max_value_int', models.IntegerField(blank=True, null=True)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='csv_generator.schema')),
            ],
        ),
    ]