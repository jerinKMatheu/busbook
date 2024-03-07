from django import forms
from .models import register

# # class RegisterForm(forms.ModelForm):
# #     class Meta:
# #         model=register
# #         fields=["email","phone","password"]
# #         labels={"email":"email","phone":"phone","pass
# # forms.py
# # from django import forms

# class RegistrationForm(forms.ModelForm):
#     email = forms.EmailField()
#     phone = forms.CharField(max_length=20)
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError(
#                 "Password and Confirm Password do not match."
#             )

#         return cleaned_data


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = register  # Specify the model class
        fields = ['email', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password do not match."
            )

        return cleaned_data



