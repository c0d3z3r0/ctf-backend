from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from registration.forms import \
    RegistrationForm as BaseRegistrationForm, DUPLICATE_EMAIL
from dynamic_preferences import global_preferences_registry as dynprefs
from .models import Profile
from betterforms.multiform import MultiModelForm

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['course', 'semester']


class UserForm(BaseRegistrationForm):

    prefs = dynprefs.manager()
    allowed_domains = \
        prefs['registration__allowed_domains'].replace(' ', '').split(',')

    if len(allowed_domains) > 1:
        BAD_DOMAIN = _("Registration using your email provider is prohibited. "
                       "Please enter an email address from one of %s." %
                       ', '.join(allowed_domains)
                       )
    else:
        BAD_DOMAIN = _("Registration using your email provider is prohibited. "
                       "Please enter an email address from %s." %
                       ', '.join(allowed_domains)
                       )

    def clean_email(self):
        # Check uniqueness
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(DUPLICATE_EMAIL)

        # Check for good domain
        email_domain = self.cleaned_data['email'].split('@')[1]
        if self.allowed_domains and email_domain not in self.allowed_domains:
            raise forms.ValidationError(self.BAD_DOMAIN)

        return self.cleaned_data['email']

    def get_user_kwargs(self, **cleaned_data):
        User = get_user_model()
        return {
            User.USERNAME_FIELD: cleaned_data['user']['username'],
            'email': cleaned_data['user']['email'],
            'password': cleaned_data['user']['password1'],
        }


class RegistrationForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'profile': ProfileForm,
    }
