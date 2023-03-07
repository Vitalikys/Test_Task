# Generated by Django 4.1.7 on 2023-03-06 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0004_remove_schema_address_remove_schema_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.PositiveIntegerField(default=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Processing'), (1, 'Ready')], default=0)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='csv_generator.schema')),
            ],
        ),
    ]
