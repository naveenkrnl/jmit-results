from django import forms
from .models import ResultData
from django.db.models import Q


class EntryForm(forms.Form):
    user=forms.CharField(widget=forms.TextInput(attrs=
                                {
                                    'class':'fadeIn second',
                                    'label' : 'Enter your username, Email or 12th Roll Number',
                                }))

    dob=forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'fadeIn third',
                                    'type':'date',
                                }))


    def clean_user(self, *args, **kwargs):
        userdata = self.cleaned_data.get("user")
        try:
            user=ResultData.objects.get(
                        Q(email__icontains=userdata)|
                        Q(username__icontains=userdata)|
                        Q(rollno__icontains=userdata)
                                            )
        except:
            return userdata
        return user.rollno

    def clean_dob(self, *args, **kwargs):
        datedata = self.cleaned_data.get("dob")
        userdata = self.cleaned_data.get("user")
        try:
            user=ResultData.objects.get(
                        Q(email__icontains=userdata)|
                        Q(username__icontains=userdata)|
                        Q(rollno__icontains=userdata)
                                            )
        except:
            raise forms.ValidationError("Incorrect Username")
        if user is not None:
            if user.dob==datedata:
                print("OK")
                return datedata
            else:
                raise forms.ValidationError("Date of Birth for {} is incorrect".format(user))




