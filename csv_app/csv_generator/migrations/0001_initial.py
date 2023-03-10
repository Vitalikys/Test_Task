# Generated by Django 4.1.7 on 2023-03-04 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='Schema title')),
                ('separator', models.CharField(choices=[(';', 'Semicolon ;'), (',', 'Comma ,')], default=',', max_length=1)),
                ('modifies', models.DateField(auto_now=True)),
                ('string_character', models.CharField(choices=[("'", "Single-quote '"), ('"', 'Double-quote "')], default='"', max_length=1)),
                ('full_name', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('job', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
