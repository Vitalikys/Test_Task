from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin

from .forms import SchemaForm
from .models import Schema


class SchemasView(ListView):
    model = Schema

    def get_queryset(self):
        current_user = self.request.user
        return Schema.objects.filter(user_id=current_user.id)


# class CreateSchema(CreateView):
#     form_class = SchemaForm
#     template_name = 'csv_generator/schema_create.html'
@login_required(login_url='login_url')
def create_schema(request):
    if request.method == 'POST':
        form = SchemaForm(request.POST)
        if form.is_valid():
            schema = form.save(commit=False)
            schema.user = request.user
            schema.save()
            # print('schema-dict: ', schema.__dict__)
            # new_schema = Schema(name=schema.name,
            #                     separator=schema.separator,
            #                     string_character=schema.string_character,
            #                     user= request.user,
            #                     full_name=schema.full_name,
            #                     age=schema.age,
            #                     job=schema.job)
            # new_schema.save()
            return redirect('schemas')
    else:
        form = SchemaForm()
    return render(request, 'csv_generator/schema_create.html', {'form': form})


@login_required(login_url='login_url')
def delete_schema(request, schema_id):
    try:
        obj = Schema.objects.get(pk=schema_id)
        obj.delete()
        return redirect('schemas')
    except:
        return False


def edit_schema(request, schema_id=None):
    if schema_id:
        schema = Schema.objects.get(pk=schema_id)
        print('schema', schema)
    form = SchemaForm(request.POST or None, instance=schema)
    if request.POST and form.is_valid():
        form.save()
        # Save was successful, so redirect to another page
        return redirect('schemas')
    return render(request, 'csv_generator/schema_edit.html', {'form': form})


def generate_csv(request, schema_id):
    schema = Schema.objects.get(pk=schema_id)

    # Select -> save columns names to variable 'csv_columns'
    csv_columns = {}
    my_keys = ['full_name', 'integer_num', 'job', 'email', 'domain_name',
               'phone_number', 'company', 'text', 'address', 'date_fake']
    for k, v in schema.__dict__.items():
        if k in my_keys and v:
            csv_columns[k] = v     # print('csv_columns = ', csv_columns)

    from .services.csv_generator import create_csv
    create_csv(csv_columns, schema, rows_count=10)

    return redirect('schemas')


class SchemaDetailView(DetailView):
    model = Schema
    # form_class = RowsForm
    template_name = 'csv_generator/schema_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

