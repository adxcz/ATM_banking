from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import BankAccount, Transaction, ContactMessage
from django.db import transaction
from decimal import Decimal

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        pin = request.POST.get('pin')
        confirm_pin = request.POST.get('confirm_pin')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')

        # Check if pins match
        if pin != confirm_pin:
            messages.error(request, 'PINs do not match')
            return render(request, 'signup.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'signup.html')

        # Create user and bank account in a transaction
        with transaction.atomic():
            user = User.objects.create_user(username=username, email=email, password=password)
            BankAccount.objects.create(
                user=user, 
                account_number=f'ACCT{user.id:06d}', 
                pin=pin
            )
        
        login(request, user)
        return redirect('dashboard')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have logged out successfully!')
    return redirect('login')

@login_required
def dashboard(request):
    account = BankAccount.objects.get(user=request.user)
    transactions = Transaction.objects.filter(account=account).order_by('-timestamp')[:5]
    return render(request, 'dashboard.html', {
        'account': account,
        'transactions': transactions
    })


@login_required
def deposit(request):
    if request.method == 'POST':
        # Convert amount from float to Decimal
        amount = Decimal(request.POST.get('amount'))
        account = BankAccount.objects.get(user=request.user)
        
        # Add the amount to the account's balance
        account.balance += amount
        account.save()
        
        # Create a transaction record
        Transaction.objects.create(
            account=account,
            amount=amount,
            transaction_type='DEPOSIT'
        )
        
        # Display success message
        messages.success(request, f'Deposited ${amount}')
        return redirect('dashboard')
    
    return render(request, 'deposit.html')

@login_required
def withdraw(request):
    if request.method == 'POST':
        # Convert amount from float to Decimal
        amount = Decimal(request.POST.get('amount'))
        account = BankAccount.objects.get(user=request.user)
        
        # Check if the user has enough balance
        if amount > account.balance:
            messages.error(request, 'Insufficient funds')
            return render(request, 'withdraw.html')
        
        # Subtract the amount from the account's balance
        account.balance -= amount
        account.save()
        
        # Create a transaction record
        Transaction.objects.create(
            account=account,
            amount=amount,
            transaction_type='WITHDRAW'
        )
        
        # Display success message
        messages.success(request, f'Withdrew ${amount}')
        return redirect('dashboard')
    
    return render(request, 'withdraw.html')

@login_required
def send_money(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        amount = Decimal(request.POST.get('amount'))  # Convert to Decimal
        
        sender_account = BankAccount.objects.get(user=request.user)
        
        try:
            recipient = User.objects.get(username=recipient_username)
            recipient_account = BankAccount.objects.get(user=recipient)
            
            if amount > sender_account.balance:
                messages.error(request, 'Insufficient funds')
                return render(request, 'sendmoney.html')
            
            # Atomic transaction to ensure consistency
            with transaction.atomic():
                sender_account.balance -= amount  # Subtract amount from sender's account
                recipient_account.balance += amount  # Add amount to recipient's account
                
                sender_account.save()
                recipient_account.save()
                
                # Record transactions
                Transaction.objects.create(
                    account=sender_account,
                    amount=amount,
                    transaction_type='TRANSFER',
                    description=f'Transfer to {recipient_username}'
                )
                Transaction.objects.create(
                    account=recipient_account,
                    amount=amount,
                    transaction_type='TRANSFER',
                    description=f'Received from {request.user.username}'
                )
            
            messages.success(request, f'Transferred ${amount} to {recipient_username}')
            return redirect('dashboard')
        
        except (User.DoesNotExist, BankAccount.DoesNotExist):
            messages.error(request, 'Recipient not found')
    
    return render(request, 'sendmoney.html')

@login_required
def change_pin(request):
    if request.method == 'POST':
        # Get the current PIN input from the form and new PIN input
        current_pin = request.POST.get('current_pin')
        new_pin = request.POST.get('new_pin')

        # Get the current user's bank account
        account = BankAccount.objects.get(user=request.user)

        # Check if the entered current PIN is correct
        if current_pin != account.pin:
            messages.error(request, 'The current PIN is incorrect.')
            return redirect('change_pin')

        # Check if the new PIN is the same as the current PIN
        if new_pin == account.pin:
            messages.error(request, 'The new PIN cannot be the same as the current PIN.')
            return redirect('change_pin')

        # Update the pin with the new value
        account.pin = new_pin
        account.save()

        messages.success(request, 'PIN updated successfully')
        return redirect('dashboard')

    return render(request, 'change_pin.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')