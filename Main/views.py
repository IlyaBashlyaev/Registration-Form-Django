from django.shortcuts import render, redirect
from .models import Account
from .forms import AccountForm
from django.views.generic import DetailView

def index(request):
    accounts = Account.objects.order_by('id')
    context = {'accounts': accounts}
    return render(request, 'Main/index.html', context)

def login(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            return redirect('login')

    accounts = Account.objects.order_by('id')
    form = AccountForm()
    
    context = {
        'accounts': accounts,
        'form': form
    }
    return render(request, 'Main/login.html', context)

def signIn(request, pk, password):
    global globalPassword
    globalPassword = password
    return redirect(f'/{str(pk)}')

def AccountDetailView(request, pk):
    global globalPassword
    account = Account.objects.get(pk = pk)
    length = len(account.password)
    password = ''

    if 'globalPassword' in globals() and globalPassword == account.password:
        password = globalPassword
        del globalPassword

    else:
        password = '•' * length
    
    
    context = {
        'account': account,
        'password': password    
    }
    return render(request, 'Main/detail_view.html', context)

'''class AccountDetailView(DetailView):
    model = Account
    template_name = 'Main/detail_view.html'
    content_object_name = 'account'''