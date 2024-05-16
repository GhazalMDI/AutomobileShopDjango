from django import forms
from accounts.models import User
class LoginRegister(forms.Form):
    phone_number = forms.CharField(max_length=11,required=True)
class CodeRegister(forms.Form):
    code = forms.CharField(max_length=6)
class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','birthday','postal_code','address')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control','data-jdp':'true'}),
            'postal_code':forms.TextInput(attrs={'class':'form-control',}),
            'address': forms.Textarea(attrs={'class': 'form-control', })
        }
    def clean(self):
        cleaned_data = super().clean()
        postal_code = cleaned_data.get('postal_code')
        if postal_code != '10':
            raise forms.ValidationError('لطفا کد پستی معتبر وارد نمایید')
        return postal_code


    #
    # def clean_phone_number(self):
    #     if self.phone_number > 12:
    #         raise forms.ValidationError('لطفا شماره تلفن خود را صحیح وارد نمایید')