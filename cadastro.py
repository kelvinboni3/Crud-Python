from django.forms import ModelForm
from app.models import Regiao_Fruta

# Create the form class.
class Regiao_FrutaForm(ModelForm):
    class Meta:
        model = Regiao_Fruta
        fields = ['Nome_Fruta', 'Nome_Regiao']