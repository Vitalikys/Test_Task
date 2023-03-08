from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseBadRequest
from .forms import SchemaForm, ColumnForm, RowsForm
from .models import Schema, Column, DataSet
from .services import csv_generator


class SchemasView(ListView):
    model = Schema

    def get_queryset(self):
        current_user = self.request.user
        return Schema.objects.filter(user_id=current_user.id)


# class CreateSchema(CreateView):
#     form_class = SchemaForm, ColumnForm
#     template_name = 'csv_generator/schema_create.html'
@login_required(login_url='login_url')
def create_schema(request):
    if request.method == 'POST':
        form_schema = SchemaForm(request.POST)
        form_column = ColumnForm(request.POST)
        if form_schema.is_valid() and form_column.is_valid():
            schema = form_schema.save(commit=False)
            schema.user = request.user
            schema.save()

            columns = form_column.save(commit=False)
            columns.schema = schema
            columns.save()
        else:
            return HttpResponseBadRequest('Schema with such name Already Exist')
        return redirect('schemas')
    else:
        form_schema = SchemaForm()
        form_column = ColumnForm()
        context = {
            'form_schema': form_schema,
            'form_column': form_column
        }
    return render(request, 'csv_generator/schema_create.html', context=context)


@login_required(login_url='login_url')
def delete_schema(request, schema_id):
    try:
        obj = get_object_or_404(Schema, pk=schema_id)
        # obj = Schema.objects.get(pk=schema_id)
        obj.delete()
        return redirect('schemas')
    except:
        return False


def edit_schema(request, schema_id=None):
    if schema_id:
        schema = Schema.objects.get(pk=schema_id)
        column_obj = Column.objects.get(schema=schema_id)
    form = SchemaForm(request.POST or None, instance=schema)
    form_column = ColumnForm(instance=column_obj)
    context = {
        'form': form,
        'form_column': form_column
    }

    if request.POST and form.is_valid():
        form.save()
        # Save was successful, so redirect to another page
        return redirect('schemas')
    return render(request, 'csv_generator/schema_edit.html', context=context)


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


class SchemaDetailView(DetailView, FormMixin):
    model = Schema
    form_class = RowsForm
    template_name = 'csv_generator/schema_detail.html'

    def post(self, request, *args, **kwargs):
        schema = self.get_object()

        # create DataSet, Get Rows count from Form
        dataset_obj = DataSet.objects.create(schema=schema, rows=request.POST['rows'])

        # get column object and filter them from empty values
        column_obj = Column.objects.get(schema=schema)
        csv_columns = csv_generator.generate_dict_values(column_obj)
        csv_generator.create_csv(csv_columns, schema, dataset_obj, column_obj)
        dataset_obj.status = 1
        dataset_obj.save()
        return redirect('detail_schema', schema.id)

    def get_context_data(self, **kwargs):
        from .services.csv_generator import generate_dict_values
        context = super().get_context_data(**kwargs)

        # get all DataSets for html template
        context['datasets'] = DataSet.objects.filter(schema=self.get_object())

        # get dictionary with filtered columns
        column_obj = Column.objects.get(schema=self.get_object())
        context['columns_filtered'] = csv_generator.generate_dict_values(column_obj)
        return context
