from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# NAO ESQUEÇAM DE ATUALIZAR OS IMPORTS
from .models import Medico
from .models import Evento
from .forms import Medico_Form
from .forms import Evento_Form
from .models import Emprestimo
from .forms import Emprestimo_Form
from .models import Time
from .forms import Time_Form
from .models import Medico, Classe_Social
from .forms import Medico_Form, Classe_Social_Form
from .models import Rodada
from .forms import Rodada_Form

# from django.core.exceptions import ObjectDoesNotExist

# views para home

@login_required(login_url='/login/')
def index(request):
    return render(request, 'jogo/index.html', {})


def base_configuracoes(request):
    return render(request, 'jogo/base_configuracoes.html', {})


def base_aplicar_dinamica(request):
    return render(request, 'jogo/base_aplicar_dinamica.html', {})


def login(request):
    contexto = {}
    if request.method == 'POST':
        try:
            usuario = request.POST['usuario']
            senha = request.POST['senha']

            try:
                user = User.objects.get(username=usuario)

                if user.is_active:
                    usuario_autenticado = authenticate(username=usuario, password=senha)

                    if usuario_autenticado is not None:
                        django_login(request, usuario_autenticado)
                        return HttpResponseRedirect('/home/')
                    else:
                        contexto['erro'] = 'Usuário ou senha inválidos.'
                else:
                    contexto['erro'] = 'Usuário inativo.'
            except:
                contexto['erro'] = 'Usuário inexistente.'
        except:
            contexto['erro'] = 'Parâmetros inválidos.'

    return render(request, 'jogo/login.html', contexto)


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)

    return HttpResponseRedirect('/login/')



# Views para médico:

def medico_index(request):
    medicos = Medico.objects.order_by('perfil')
    return render(request, 'medico/medico_index.html', {'medicos':medicos})

# TODO login_required
#@login_required(login_url='/adm/login/')
def medico_new(request):
    # medico = None
    # try:
    #     medico = Medico.objects.latest('id')
    # except:
    #     pass
    # if medico == None:
    #     id = 1
    # else:
    #     id = medico.id + 1

    if request.method == 'POST':
        form = Medico_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medico')
        else:
            return render(request, 'medico/medico_new.html', {'form':form})
    else:
        form = Medico_Form()
        return render(request, 'medico/medico_new.html', {'form': form})

# TODO login_required
#@login_required(login_url='/adm/login/')
def medico_edit(request, id):
    medico = get_object_or_404(Medico,pk=id)
    form = Medico_Form(instance=medico)

    if request.method == 'POST':
        form = Medico_Form(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medico')

    return render(request, 'medico/medico_edit.html', {'form':form, 'id':id})

# TODO login_required
#@login_required(login_url='/adm/login/')
def medico_delete(request, id):
    get_object_or_404(Medico, pk=id).delete()
    return HttpResponseRedirect('/medico')

def evento_index(request):
    eventos = Evento.objects.all()
    print(eventos)
    return render(request, 'evento/evento_index.html', {'eventos': eventos})
def rodada_index(request):
    rodadas = Rodada.objects.order_by('numeroRodada')
    return render(request, 'rodada/rodada_index.html', {'rodadas':rodadas})

def evento_new(request):
    if request.method == 'POST':
        form = Evento_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/evento')
        else:
            return render(request, 'evento/evento_new.html', {'form': form})
    else:
        form = Evento_Form()
        return render(request, 'evento/evento_new.html', {'form': form})
#VIEWS PARA TIME
def time_index(request):
    times = Time.objects.order_by('id')
    return render(request, 'time/time_index.html', {'times': times})
# Views para classe social:
# TODO login_required
#@login_required(login_url='/adm/login/')
def rodada_new(request):
    # TODO verificar se esta parte deve ser descomentada
    # rodada = None
    # try:
    #     rodada = Rodada.objects.latest('numeroRodada')
    # except:
    #     pass
    # if rodada == None:
    #     numeroRodada = 1
    # else:
    #     numeroRodada = rodada.numeroRodada + 1
    if request.method == 'POST':
        form = Rodada_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rodada')
        else:
            return render(request, 'rodada/rodada_new.html', {'form': form})
    else:
        form = Rodada_Form()
        return render(request, 'rodada/rodada_new.html', {'form': form})


def evento_edit(request, id):
    pass

def evento_delete(request, id):
    pass




# Views para empréstimo:

def emprestimo_index(request):
    emprestimos = Emprestimo.objects.order_by('valor')
    return render(request, 'emprestimo/emprestimo_index.html', {'emprestimos':emprestimos})

def emprestimo_edit(request, id):
    emprestimo = get_object_or_404(Emprestimo, pk=id)
    form = Emprestimo_Form(instance=emprestimo)

    if request.method == 'POST':
        form = Emprestimo_Form(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/emprestimo')

    return render(request, 'emprestimo/emprestimo_edit.html', {'form': form})

def emprestimo_delete(request, id):
    get_object_or_404(Emprestimo, pk=id).delete()
    return HttpResponseRedirect('/emprestimo')

def emprestimo_new(request):
    if request.method == 'POST':
        form = Emprestimo_Form(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/emprestimo')
        else:
            return render(request, 'emprestimo/emprestimo_new.html', {'form': form})
    else:
        form = Emprestimo_Form()
        return render(request, 'emprestimo/emprestimo_new.html', {'form': form})
#@login_required(login_url='/adm/login/')
def time_new(request):
    if request.method == 'POST':
        form = Time_Form(request.POST)
        if form.is_valid():
            repetesenha =  form.cleaned_data['repetesenha']
            senha = form.cleaned_data['senha']
            if(repetesenha == senha):
                form.save()
                return HttpResponseRedirect('/time')
            else:
                return render(request, 'time/time_new.html', {'form': form, 'id': id})
        else:
            return render(request, 'time/time_new.html', {'form': form, 'id': id})
    else:
        form = Time_Form()
        return render(request, 'time/time_new.html', {'form': form, 'id': id})

#@login_required(login_url='/adm/login/')
def time_edit(request, id):
    time = get_object_or_404(Time,pk=id)
    form = Time_Form(instance=time)

    if request.method == 'POST':
        form = Time_Form(request.POST, instance=time)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/time')

    return render(request, 'time/time_edit.html', {'form':form, 'id':id})

#@login_required(login_url='/adm/login/')
def time_delete(request, id):
    get_object_or_404(Time, pk=id).delete()
    return HttpResponseRedirect('/time')
def classe_social_index(request):
    classes = Classe_Social.objects.order_by('id')
    return render(request, 'classe_social/classe_social_index.html', {'classes':classes})

def classe_social_edit(request, id):
    classe = get_object_or_404(Classe_Social, pk=id)
    form = Classe_Social_Form(instance=classe)

    if request.method == 'POST':
        form = Classe_Social_Form(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/classe_social')

    return render(request, 'classe_social/classe_social_edit.html', {'form': form, 'id': id})

def classe_social_delete(request, id):
    get_object_or_404(Classe_Social, pk=id).delete()
    return HttpResponseRedirect('/classe_social')

def classe_social_new(request):
    classe = None
    try:
        classe = Classe_Social.objects.latest('id')
    except:
        pass
    if classe == None:
        id = 1
    else:
        id = classe.id+1
    if request.method == 'POST':
        print(request.POST)
        form = Classe_Social_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/classe_social')
        else:
            return render(request, 'classe_social/classe_social_new.html', {'form': form, 'id': id})
    else:
        form = Classe_Social_Form()
        return render(request, 'classe_social/classe_social_new.html', {'form': form, 'id': id})

# TODO login_required
#@login_required(login_url='/adm/login/')
def rodada_edit(request, id):
    rodada = get_object_or_404(Rodada,pk=id)
    form = Rodada_Form(instance=rodada)

    if request.method == 'POST':
        form = Rodada_Form(request.POST, instance=rodada)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rodada')

    return render(request, 'rodada/rodada_edit.html', {'form':form})