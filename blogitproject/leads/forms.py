from django import forms
from leads.models import Lead

class LeadForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "name":"name", "id":"name", "type":"text", "onfocus":"this.placeholder = ''", "onblur":"this.placeholder : 'Enter your name'", "placeholder":"Enter your name"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "name":"subject", "id":"subject", "type":"text", "onfocus":"this.placeholder = ''", "onblur":"this.placeholder : 'Enter your subject'", "placeholder":"Enter your subject"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "name":"email", "id":"email", "type":"text", "onfocus":"this.placeholder = ''", "onblur":"this.placeholder : 'Enter your email'", "placeholder":"Enter your email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control w-100", "name":"message", "id":"message", "cols":"30", "rows":"9", "onfocus":"this.placeholder : ''", "onblur":"this.placeholder = 'Enter Message'", "placeholder":"Enter Message"}))

    class Meta:
        model = Lead
        fields = ['name', 'subject', 'email', 'message']
