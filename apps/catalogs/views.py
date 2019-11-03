from django.shortcuts import render
from django.core.paginator import Paginator
from apps.catalogs.models import Empresa, NotaFiscal
import csv, io
from django.contrib import messages

def empresas_list(ListView):
    empresas = Empresa.objects.all()
    return render(ListView, 'empresas_list.html', {'empresa':empresas})

def empresas_notas_list(request):
    empresas_notas = NotaFiscal.objects.all()
    search = request.GET.get('search')
    if search:
        empresas_notas = empresas_notas.filter(nome_descricao__icontains=search) or empresas_notas.filter(
            numero__icontains=search)
    paginator = Paginator(empresas_notas,10)
    page = request.GET.get('page')
    empresas_notas = paginator.get_page(page)
    return render(request, 'notasfiscais.html', {'empresas_notas':empresas_notas})

def notafiscal_list(request,pk):
    empresas_notas = NotaFiscal.objects.filter(empresa=pk)
    search = request.GET.get('search')
    if search:
        empresas_notas = empresas_notas.filter(nome_descricao__icontains=search) or empresas_notas.filter(numero__icontains=search)
    paginator = Paginator(empresas_notas, 10)
    page = request.GET.get('page')
    empresas_notas = paginator.get_page(page)
    return render(request, 'notasfiscais.html', {'empresas_notas':empresas_notas})



def popula_sql(request):

    template = 'popula_sql.html'

    prompt = {
        'orderm': "Ordem dos campos: "
    }

    if request.method == 'GET':
        return render(request, template, prompt)


    upload = request.FILES
    for a in upload:
        if a == 'empfile':
            csv_file_empresa = request.FILES['empfile']
            data_set_empresa = csv_file_empresa.read().decode('UTF-8')
            io_string_empresa = io.StringIO(data_set_empresa)
            next(io_string_empresa)

            for column in csv.reader(io_string_empresa, delimiter=','):
                _, created = Empresa.objects.update_or_create(
                    nome=column[0],
                    CNPJ=column[1]
                )

        elif a == 'notafile':
            csv_file_nota = request.FILES['notafile']

            if not csv_file_nota.name.endswith('.csv'):
                messages.error(request, 'Insira um arquivo csv notas')

            data_set_nota = csv_file_nota.read().decode('UTF-8')

            io_string_nota = io.StringIO(data_set_nota)

            next(io_string_nota)

            for column in csv.reader(io_string_nota, delimiter=','):
                _, created = NotaFiscal.objects.update_or_create(
                    serie=column[0],
                    numero=column[1],
                    nome_descricao=column[2],
                    peso=column[3],
                    cubagem=column[4],
                    data=column[5],
                    empresa_id=column[6]
                )


    context = {}
    return render(request, template, context)

def home_list(request):
    return render(request,"home.html")