from django.contrib.auth.models import User
from django.db import models

COLUMN_SEPARATOR = (
    (";", 'Semicolon ;'),
    (",", 'Comma ,'),
)
STR_CHARACTER = (
    ("'", "Single-quote '"),
    ("\"", "Double-quote \""),
)


class Schema(models.Model):
    # main data - global info
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="Schema title")
    separator = models.CharField(max_length=1, choices=COLUMN_SEPARATOR, default=",")
    modifies = models.DateField(auto_now=True)
    string_character = models.CharField(max_length=1, choices=STR_CHARACTER, default='"')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Schemas columns, we create only names for columns
    full_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.CharField(max_length=20, blank=True, null=True)
    job = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.name}"

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

# class Column(models.Model):
#     schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
#     title = models.CharField(choices=COLUMNS)
#     full_name = models.CharField(max_length=30, )
#     age = models.PositiveIntegerField(max_length=2)