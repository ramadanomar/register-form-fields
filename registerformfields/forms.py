from django import forms
from openedx.core.djangoapps.user_authn.views.registration_form import AccountCreationForm


class ExtendedRegistrationForm(AccountCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    work_phone_number = forms.CharField(required=True, max_length=30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].error_messages = {
            'required': 'First name is required',
            'max_length': 'First name cannot exceed 30 characters',
        }
        self.fields['last_name'].error_messages = {
            'required': 'Last name is required',
            'max_length': 'Last name cannot exceed 30 characters',
        }
        self.fields['work_phone_number'].error_messages = {
            'required': 'Work phone number is required',
            'max_length': 'Work phone number cannot exceed 30 characters',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            user_profile = UserProfile.objects.get(user=user)
            extended_profile = user_profile.extendeduserprofile
            extended_profile.work_phone_number = self.cleaned_data['work_phone_number']
            extended_profile.save()
        return user
