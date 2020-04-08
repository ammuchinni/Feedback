from django.shortcuts import render
from django.http import HttpResponse
from feedbackapp import forms
# Create your views here.
def thankview(request):
    return HttpResponse("Thanks for Registration...We will contact you soon....")
def Feedbackview(request):
    form=forms.Feedbackform()
    if request.method=='POST':
        form=forms.Feedbackform(request.POST)
        if form.is_valid():
            print('Validation Success')
            print('Student Name:',form.cleaned_data['name'])
            print('Student Rollno:',form.cleaned_data['rollno'])
            print('Student Email:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
            return thankview(request)
    return render(request,'feedbackapp/f.html',{'form':form})
