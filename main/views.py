from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

from main.models import Meal, Staff

# Create your views here.
def index(request):     
    return render(request,'main/index.html')

                        
def about(request):
    return render(request,'main/about.html')

def meal(request):
    return render(request,'main/meal.html')

def finapply(request):
    return render(request,'main/finapply.html')

def opinion(request):
    return render(request,'main/opinion.html')

def fee(request):
    return render(request,'main/fee.html')


def meal_list(request):
    meals = Meal.objects.all().order_by('setup_date')

    print("Number of meals:", meals.count())  # Debug print
    print("Meals:", list(meals.values()))     # Debug print
    return render(request, 'main/meal.html', {'meals': meals})

def staffs(request):
    staffs = Staff.objects.filter(staff_type='Specialist')
    return render(request, 'main/staffs.html', {'staffs': staffs})

def qa(request):
    return render(request,'main/qa.html')

def services(request):
    return render(request,'main/services.html')

def movein(request):
    return render(request,'main/movein.html')

def facilities(request):
    return render(request,'main/facilities.html')
 
                        
def map(request):
    return render(request,'main/map.html')


def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        telephone = request.POST['telephone']
        email = request.POST['email']
        opinion = request.POST['opinion']

        subject = '養心園安老院舍 - 聯絡我們'
        email_message = f'姓名: {name}\n電話號碼: {telephone}\n電子郵件: {email}\n意見:\n{opinion}'
 
        try: 
            # Send the email
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL, email])
            messages.success(request, '您的請求已提交，請耐心等待，我們的工作人員將儘快與您聯繫。')
        except Exception as e:
            print('Error sending email:', e)
            messages.error(request, f'Error sending email: {e}')



        return redirect('index')    

    return render(request,'main/contactus.html')

def application(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        application_message = request.POST['application_message']

        # Construct the email content
        subject = '養心園安老院舍 - 預約參觀'
        email_message = f'姓名: {name}\n電子郵件: {email}\n電話號碼: {phone}\n留言:\n{application_message}\n\n\n您的請求已提交,請耐心等待,我們的工作人員將儘快與您聯繫'
        # List of recipient emails
        recipient_list = [email]  # Add your email addresses here
 
        try: 
            # Send the email
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            messages.success(request, '您的請求已提交，請耐心等待，我們的工作人員將儘快與您聯繫。')
        except Exception as e:
            print('Error sending email:', e)
            messages.error(request, f'Error sending email: {e}')

  
        return redirect('index')  # Redirect to the home page after submission

    return render(request, 'main/application.html')


def opinion(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            contact = request.POST.get('contact')   
            checkin = request.POST.get('checkin')
            checkout = request.POST.get('checkout')
            accommodation = request.POST.get('accommodation')
            dinning = request.POST.get('dinning')
            staff = request.POST.get('staff') 
            suggestions = request.POST.get('suggestion')

            # Validate required fields
            required_fields = [contact, checkin, checkout, 
                             accommodation, dinning, staff]
            
            if not all(required_fields):
                messages.error(request, '請填寫所有必需欄位。')
                return redirect('opinion')

            # Prepare email content
            subject = '養心園安老院舍 - 意見收集'
            email_message = f'''
申請人資料：
姓名: {name}
年齡: {age}
性別: {gender}
電子郵件: {contact}
入住時間: {checkin}
退房時間: {checkout}
服務評分：
住宿滿意度: {accommodation}
餐飲滿意度: {dinning}
員工滿意度: {staff} 

其他意見：
{suggestions if suggestions else "無"}
'''
            
            email_message=email_message+'\n\n\n 感謝你的意見!!'

            # Send email
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL, contact],
                fail_silently=False
            )

            messages.success(request, '您的意見已提交，感謝你的意見。')
            return redirect('index')

        except Exception as e:
            print('Error:', str(e))
            messages.error(request, '發送電子郵件時出現錯誤，請稍後再試。')
            return redirect('opinion')

    return render(request, 'main/opinion.html')
 
def booking(request):
    if request.method == 'POST':
        try:
            # Use get() to avoid MultiValueDictKeyError
            name = request.POST.get('name')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            medicalHistory = request.POST.get('medicalHistory')
            emergencyContact = request.POST.get('emergencyContact')
            relationship = request.POST.get('relationship')
            stayDuration = request.POST.get('stayDuration')

            if not all([name, age, gender, email, address, phone, 
                       medicalHistory, emergencyContact, relationship, stayDuration]):
                messages.error(request, '請填寫所有必需欄位。')
                return redirect('booking')

            subject = '養心園安老院舍 - 床位預約申請'
            email_message = f'''
            申請人資料：
            姓名: {name}
            年齡: {age}
            性別: {gender}
            電子郵件: {email}
            地址: {address}
            電話號碼: {phone}
            病史: {medicalHistory}
            緊急聯絡人: {emergencyContact}
            關係: {relationship}
            預計入住日期: {stayDuration}
                        '''



            email_message=email_message+'\n\n\n 您的預約申請已提交，我們會盡快與您聯絡。'

            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL, email],
                fail_silently=False
            )
            messages.success(request, '您的預約申請已提交，我們會盡快與您聯絡。')
            return redirect('index')

        except Exception as e:
            print('Error:', str(e))
            messages.error(request, '發送電子郵件時出現錯誤，請稍後再試。')
            return redirect('booking')

    return render(request, 'main/booking.html')
