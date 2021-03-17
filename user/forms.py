from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Parolayı Doğrula",widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50,label="Adınız")
    last_name = forms.CharField(max_length=50,label="Soyadınız")
    email = forms.EmailField(max_length=50,label="E-Mail")
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor!")

        values = {
            "username" : username,
            "password" : password,
            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email
        }
        return values