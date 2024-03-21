from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from Ashop.settings import EMAIL_HOST_USER
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import VendorApplyForm
from django.utils import timezone
from datetime import timedelta

from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


# Create your views here.

User = get_user_model()  # Get the active user model

class Signup(View):
    def get(self, request):
        return render(request, 'user/signup.html')
    

    def post(self, request):
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exist')

        user = User.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name)

        generate_verification = random.randint(100000, 999999)
        user.otp = generate_verification
        user.otp_created_at = timezone.now()  # Store the timestamp when OTP was generated
        user.save()

        subject = "OTP Verification"
        body = f"Your verification code is: {generate_verification}"
        from_email = EMAIL_HOST_USER
        to_email = email
        send_now = send_mail(subject, body, from_email, [to_email])
        
        if send_now:
            messages.success(request, 'Successfully sent OTP. Verify your email here.')
            return redirect('verifyit')
        messages.error(request, 'Sign up')
        return render(request, 'user/signup.html')





class Verify(View):
    def get(self, request):
        return render(request, 'user/verify.html')

    def post(self, request):
        entered_otp = request.POST.get('otp')
        try:
            user = User.objects.get(otp=entered_otp, is_emailverified=False)
            if user.otp_created_at and timezone.now() - user.otp_created_at <= timedelta(minutes=2):
                user.is_emailverified = True
                user.save()
                login(request, user)
                messages.success(request, 'Success! You are logged in. Create your account here.')
                return redirect('registerit')
            else:
                # user.delete()
                messages.error(request, 'OTP is expired,resend another one here')
                return redirect('reverifyit')
            
        except User.DoesNotExist:
            messages.error(request, 'User not found, sign up.')
            return redirect('signup')
            



class ReverifyOtp(View):
    def get(self, request):

        return render(request, 'user/reverify-otp.html')


    def post(self, request):
        
        entered_email = request.POST.get('email')

        # Check if the entered email matches the one in the database
        try:
            user = User.objects.get(email=entered_email, is_emailverified=False)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email address.')
            return redirect('reverifyit')

        # Generate new OTP
        new_otp = random.randint(100000, 999999)
        user.otp = new_otp
        user.otp_created_at = timezone.now()
        user.save()

        # Send new OTP
        subject = "New OTP Verification"
        body = f"Your new verification code is: {new_otp}"
        from_email = EMAIL_HOST_USER  # Update with your email host user
        to_email = entered_email
        send_now = send_mail(subject, body, from_email, [to_email])

        if send_now:
            messages.success(request, 'New OTP sent successfully.')
            return redirect('verifyit') 
        else:
            messages.error(request, 'Failed to send new OTP, resend again here.')
            return redirect('reverifyit')





class Register(View):

    def get(self, request):
        
        return render(request, 'user/page-register.html')


    def post(self, request):
        # Ensure the user is logged in
        if not request.user.is_authenticated:
            messages.error(request, 'User not authenticated')
            return redirect('login')

        # Retrieve the logged-in user
        user = request.user

        # Retrieve the username entered in the form
        entered_username = request.POST.get('username')
        entered_email = request.POST.get('email')

        if entered_email != request.user.email:
            return HttpResponse('email_mismatch')

        if entered_username != request.user.username:
            return HttpResponse('username_mismatch')

        # Update user password provided in the form
        password = request.POST['password']
        confirm_password = request.POST['password']
        if password and confirm_password:
            if password == confirm_password:
                user.set_password(password)
                user.save(update_fields=['password'])
                messages.success(request, 'Password updated successfully')
            else:
                messages.error(request, 'Passwords did not match')
        else:
            messages.warning(request, 'No password provided')

        # Check if the user selected the vendor option
        is_vendor = request.POST.get('payment_option') == 'is_vendor'
        if is_vendor:
            user.is_vendor = False
            user.vendor_application_status = 'pending'
            user.save()

            login(request, user)
            messages.success(request, 'Apply for Vendorship')
            return redirect('apply')
        else:
            messages.success(request, 'Welcome,Account created successfully, login with your password')
            return redirect('login')






class UserAccount(View):
    def get(self, request):
        return render(request, 'dash/page-account.html')


    def post(self, request):
        pass    
        





class VendorApply(View):
    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'User not authenticated')
            return redirect('login')
        
        form = VendorApplyForm()  # Create an empty form instance
        return render(request, 'dash/vendor-apply.html', {'form': form})

    def post(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'User not authenticated')
            return redirect('login')

        # Retrieve the logged-in user
        user = request.user

        # Initialize the form with the POST data
        form = VendorApplyForm(request.POST)

        if form.is_valid():
            # Update the user's fields with the form data
            user.business_name = form.cleaned_data['business_name']
            user.location = form.cleaned_data['location']
            user.registration_no = form.cleaned_data['registration_no']
            user.registering_body = form.cleaned_data['registering_body']
            user.business_description = form.cleaned_data['business_description']
            user.website_url = form.cleaned_data['website_url']

            # Update user's vendor status
            is_vendor = form.cleaned_data.get('is_vendor')
            if is_vendor:
                user.is_vendor = False
                user.vendor_application_status = 'pending'

            # Save the user instance
            user.save()
            messages.success(request, 'Account created successfully, vendor status..Pending')
            return redirect('account')
        else:
            messages.info(request, 'Please fill all required fields')
            return render(request, 'dash/vendor-apply.html', {'form': form})





class VendorPage(View):
    def get(self, request):
        return render(request, 'dash/vendor-dashboard.html')
    

    def post(self, request):
        pass





class Home(View):
    def get(self, request):
        return render(request, 'index.html')
    




class Login(View):
    def get(self, request):
        return render(request, 'user/page-login.html')

    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Retrieve the user by email
            user = User.objects.get(email=email)

            # Check if the user is a superuser
            if user.is_superuser and user.check_password(password):
                # Log in the superuser if password match
                login(request, user)
                messages.success(request, 'Welcome back, Admin!')
                return redirect('account')

            # For regular users, check email verification
            if not user.is_emailverified:
                # Redirect to reverifyit page if email is not verified
                messages.info(request, 'Verify your email')
                return redirect('reverifyit')

            # Authenticate the user
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                
                if user.is_vendor:
                    messages.success(request, 'Welcome back, Vendor!')
                    return redirect('vendor')
                else:
                    messages.success(request, 'Welcome back, Customer!')
                    return redirect('account')
            else:
                messages.error(request, 'Invalid input')
                return redirect('login')

        except User.DoesNotExist:
            messages.info(request, 'Sign up to get started')
            return redirect('signup')





def Logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')





class ForgotPassword(View):
  def get(self, request):
    messages.success(request, 'Enter your email here to get a password reset link')
    return render(request, 'user/page-forgot-password.html')

  def post(self, request):
    email = request.POST.get('email')

    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      messages.error(request, 'User with this email address does not exist.')
    #   return HttpResponse('', status=404)

    # Generate a one-time use token for password reset
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    # Construct the password reset link
    current_site = get_current_site(request)
    reset_link = f"http://{current_site.domain}{reverse('reset-password', args=(uid, token))}".strip('/')

    # Send the password reset link to the user's email
    send_mail(
      'Password Reset',
      f'Use this link to reset your password: {reset_link}',
      'emchadexglobal@gmail.com',
      [email],
      fail_silently=False,
    )
    messages.success(request, 'A password reset link has been sent to your email.')
    return render(request, 'user/page-forgot-password.html')
    



class PasswordReset(View):
    def get(self, request, uidb64, token):
        try:
            # Decode the user ID from base64
            uid = force_str(urlsafe_base64_decode(uidb64))
            # Get the user based on the decoded ID
            user = User.objects.get(pk=uid)

            # Check if the token is valid for the user
            if default_token_generator.check_token(user, token):
                # Render the password reset form
                messages.success(request, 'Reset your password here.')
                return render(request, 'user/page-reset-password.html', {'validlink': True, 'uidb64': uidb64, 'token': token})
            
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, MultipleObjectsReturned):
            pass

        # If the link is invalid,
        messages.info(request, 'Enter your email for password reset link.') 
        return render(request, 'user/page-forgot-password.html')
    


    def post(self, request, uidb64, token):
        # Handle the form submission to set a new password
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
 
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'user/page-reset-password.html', {'error': 'Passwords do not match'})

        # Set the new password
        user.set_password(password)
        user.save()

        # Redirect to the login page
        messages.success(request, 'Password reset success, login with your new password')
        return redirect('login')
