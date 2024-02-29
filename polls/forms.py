from django import forms

from .models import registering, posting

# new register form

class newregister(forms.ModelForm):
    class Meta:
        model = registering
        fields = ['name','Age','ide','collage_name','field','location']

# edit register form

class Editregister(forms.ModelForm):
    class Meta:
        model = registering
        fields = ['name','Age','ide','collage_name','field','location']

# new post form

class newpost(forms.ModelForm):
    class Meta:
        model = posting
        fields = ['name','dis','sub','img']
        

# edit post form

class Editpost(forms.ModelForm):
    class Meta:
        model = posting
        fields = ['name','dis','sub','img']
        