from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from  .models import Expense,Category
from .forms import ExpenseForm
from collections import defaultdict
from datetime import datetime
import json
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse

# Create your views here.
def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def home(request):
    expenses= Expense.objects.filter(user=request.user).order_by('-date')
    expenses_list=expenses
    paginator=Paginator(expenses_list,5)
    page_number=request.GET.get('page')
    expenses=paginator.get_page(page_number)

    category = request.GET.get('category')
    date=request.GET.get('date')
    search=request.GET.get('search')

    if category:
        expenses = expenses.filter(category__name=category)

    if date:
        expenses=expenses.filter(date=date)

    if search:
        expenses=expenses.filter(description__icontains=search)

    total=sum(expense.amount for expense in expenses)
    latest=expenses[0].amount if expenses else 0

    #monthly total
    current_month= datetime.now().month
    monthly_total=sum(expense.amount for expense in expenses
                      if expense.date.month == current_month)
    
    #budget warning
    budget_limit=100000
    warning=total>budget_limit

    #category chart
    category_data = defaultdict(float)
    for expense in expenses:
        category_data[expense.category.name] += expense.amount

    category_labels= list(category_data.keys())
    category_amounts= list(category_data.values())

    context={
        'expenses':expenses,
        'total':total,
        'latest':latest,

        'category_labels':json.dumps(category_labels),
        'category_amounts':json.dumps(category_amounts),
        'categories':Category.objects.all(),
        'monthly_total':monthly_total,
        'warning':warning,
    }
    return render(request,'home.html',context)


@login_required
def add_expense(request):
    if request.method=='POST':
        form= ExpenseForm(request.POST)
        if form.is_valid():
            expense=form.save(commit=False)
            expense.user=request.user
            expense.save()
            return redirect('/')
    else:
        form=ExpenseForm()

    return render(request, 'add_expense.html',{'form':form})

@login_required
def delete_expense(request,id):
    expense= get_object_or_404(Expense,id=id,user=request.user)
    expense.delete()
    return redirect('/')

@login_required
def edit_expense(request,id):
    expense=get_object_or_404(
        Expense,id=id,user=request.user
    )

    if request.method=="POST":
        form=ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ExpenseForm(
            instance=expense
        )
    
    return render(
        request,'add_expense.html',{'form':form}
    )

@login_required
def export_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="expenses.csv" '
    writer=csv.writer(response)
    writer.writerow(['Amount','Category','Date','Description'])
    expenses=Expense.objects.filter(user=request.user)
    for expense in expenses:
        writer.writerow([
            expense.amount,
            expense.category,
            expense.date,
            expense.description
        ])
    return response