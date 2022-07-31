from django.shortcuts import redirect, render

from .forms import *
from .models import *


def home(request):
    if request.method == 'POST':
        questions = QuestionsModel.objects.all()
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
        questions = QuestionsModel.objects.all()
        
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
    return render(request, 'quiz/register.html')

def loginPage(request):
    return render(request, 'quiz/login.html')

def logoutPage(request):
    return redirect('/')
