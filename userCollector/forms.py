from django.forms import ModelForm
from .models import BetaTester

class UserForm(ModelForm):
    class Meta:
        model = BetaTester
        fields = ['first_name','last_name','email','city',\
        'state','coach','parent','soccer','baseball','softball',\
        'lacrosse','basketball','volleyball','football','golf',\
        'tennis','ice_skating','swimming','gymnastics','other']
