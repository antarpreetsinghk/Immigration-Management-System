from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Lead, Application, Payment


class DateInput(forms.DateInput):
    input_type = 'date'


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)

        self.fields['branch'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].label = "Select Branch"
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].label = "Full Name"
        self.fields['case_type'].widget.attrs['class'] = 'form-control'
        self.fields['countery_for_apply'].widget.attrs['class'] = 'form-control'
        self.fields['countery_for_apply'].label = "Country To Apply"
        self.fields['qualification'].widget.attrs['class'] = 'form-control'
        self.fields['experience'].widget.attrs['class'] = 'form-control'
        self.fields['mobile_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['succeed'].widget.attrs['class'] = 'form-control'
        self.fields['succeed'].label = "Status"


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'estimate_compleation_date': DateInput(),
            'application_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        self.fields['branch'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].label = "Select Branch"
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['file_number'].widget.attrs['class'] = 'form-control'
        self.fields['uic_number'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].label = "Full Name"
        self.fields['case_type'].widget.attrs['class'] = 'form-control'
        self.fields['countery_for_apply'].widget.attrs['class'] = 'form-control'
        self.fields['countery_for_apply'].label = "Country To Apply"
        self.fields['qualification'].widget.attrs['class'] = 'form-control'
        self.fields['experience'].widget.attrs['class'] = 'form-control'
        self.fields['mobile_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['total_fees'].widget.attrs['class'] = 'form-control'
        self.fields['estimate_compleation_date'].widget.attrs['class'] = 'form-control'
        self.fields['succeed'].widget.attrs['class'] = 'form-control'
        self.fields['succeed'].label = "Status"
        self.fields['application_date'].widget.attrs['class'] = 'form-control'
        self.fields['application_date'].label = "Submited Date"


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        self.fields['amount'].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control text-input'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
