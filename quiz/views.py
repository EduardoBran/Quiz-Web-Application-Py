from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import *
from .models import *


def home(request):
    if request.method == 'POST':
        questions = QuestionsModel.objects.all().filter(
            mostrar=True
        )
        score = 0
        wrong = 0
        correct = 0
        total = 0
        
        for q in questions:
            total += 1
            
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
                
            else:
                wrong += 1
        
        percent = score / (total * 10) * 100
        
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        } 
        return render(request, 'quiz/result.html', context)
    
    else:
        questions = QuestionsModel.objects.all().filter(
            mostrar=True
        )
        
        context = {
            'questions': questions
        }
        return render(request, 'quiz/home.html', context)
    

def addQuestionPage(request):
    if request.user.is_staff:
        form = addQuestionForm()
        if request.method == 'POST':
            form = addQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        
        context = {'form': form}
        return render(request, 'quiz/addQuestion.html', context)
    
    else:
        return redirect('home')
    

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        form = createUserForm()
        
        if request.method == 'POST':
            form = createUserForm(request.POST)
            
            if form.is_valid():
                user = form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f'Bem vindo(a). Agora você já pode realizar o login com sucesso.'
                )
                return redirect('login')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    f'Ooops... parece que temos algum dado inválido.'
                )

        context = {'form': form}
        
        return render(request, 'quiz/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f'Bem vindo(a) {username}. Você agora está logado.'
                )
                return redirect('home')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    f'Usuário ou senha incorretas.'
                )
                return render(request, 'quiz/login.html')  
            
        context = {}
        
        return render(request, 'quiz/login.html', context)

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(
            request,
            messages.WARNING,
            f'Usuário foi deslogado com sucesso.'
        )
        return redirect('home')
    else:        
        return redirect('home')
