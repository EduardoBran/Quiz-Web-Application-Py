from django.shortcuts import redirect, render


def home(request):
    return render(request, 'quiz/home.html')

def addQuestionPage(request):
    return render(request, 'quiz/addQuestion.html')

def registerPage(request):
    return render(request, 'quiz/register.html')

def loginPage(request):
    return render(request, 'quiz/login.html')

def logoutPage(request):
    return redirect('/')
