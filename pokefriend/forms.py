from django import forms
from pokefriend.validation import *


class TrainerRegisterForms(forms.ModelForm):
    code = forms.CharField(max_length=14)

    class Meta:
        model = Trainer
        fields = '__all__'
        exclude = ['last_modified']


    def clean(self):
        code = self.cleaned_data.get('code').replace(' ','')
        error_list = {}
        code_has_twelve_numbers(code, 'code', error_list)
        code_entered_24h_or_more(code, 'code', error_list)

        if error_list is not None:
            for error in error_list:
                error_message = error_list[error]
                self.add_error(error, error_message)

        return self.cleaned_data


class TrainerSearchForms(forms.ModelForm):
    class Meta:
        model = Trainer
        exclude = ['last_modified', 'code']

    def clean(self):
        return self.cleaned_data