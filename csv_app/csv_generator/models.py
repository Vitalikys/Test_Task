from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

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
    job = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    domain_name = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=20, blank=True, null=True)
    text = models.CharField(max_length=20, blank=True, null=True)
    integer_num = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    date_fake = models.CharField(max_length=20, blank=True, null=True)

    min_value_int = models.IntegerField(null=True, blank=True)
    max_value_int = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.name}"

    def get_absolute_url(self):
        return reverse('detail_schema', kwargs={'pk': self.pk})

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'


# class Column(models.Model):
#     """ Schemas columns model, we create only names for columns """
#     schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=30, blank=True, null=True)
#     job = models.CharField(max_length=20, blank=True, null=True)
#     email = models.CharField(max_length=20, blank=True, null=True)
#     domain_name = models.CharField(max_length=20, blank=True, null=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     company = models.CharField(max_length=20, blank=True, null=True)
#     text = models.CharField(max_length=20, blank=True, null=True)
#     integer_num = models.CharField(max_length=20, blank=True, null=True)
#     address = models.CharField(max_length=20, blank=True, null=True)
#     date_fake = models.CharField(max_length=20, blank=True, null=True)
#     min_value_int = models.IntegerField(null=True, blank=True)
#     max_value_int = models.IntegerField(null=True, blank=True)