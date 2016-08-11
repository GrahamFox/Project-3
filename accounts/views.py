from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings
import stripe
from blog.models import Post

stripe.api_key = settings.STRIPE_SECRET


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=499,
                    currency="EUR",
                    description=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'], )

            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                form.save()

                user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))

                if user:
                    auth.login(request, user)
                    messages.success(request, 'You have successfully registered')
                    return redirect(reverse('profile'))

                else:
                    messages.error(request, 'Unable to log you in at this time ')
            else:
                messages.error(request, "We were unable to take a payment with that card!")

    else:
        form = UserRegistrationForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'register_form.html', args)


@login_required(login_url='/login/')
def profile(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'profile.html', {'posts': posts})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, 'You have successfully logged in! ')
                return redirect(reverse('profile'))
            else:
                form.add_error(None, 'Your email or password was not recognised')
    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
