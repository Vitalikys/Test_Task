from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from .forms import SchemaForm
from .models import Schema


class SchemasView(ListView):
    model = Schema

    def get_queryset(self):
        return Schema.objects.all()


# class CreateSchema(CreateView):
#     form_class = SchemaForm
#     template_name = 'csv_generator/schema_create.html'

def create_schema(request):
    if request.method == 'POST':
        form = SchemaForm(request.POST)
        if form.is_valid():
            schema = form.save(commit=False)
            schema.user = request.user
            schema.save()
            print('schema-dict', schema.__dict__)
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
