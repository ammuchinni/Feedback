from django import forms
from django.core import validators

class Feedbackform(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("Length should be greater than 4 letters")
        else:
            return inputname

    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        if len(str(inputrollno))>4:
            raise forms.ValidationError("Only three digit number is allowed")
        else:
            return inputrollno
