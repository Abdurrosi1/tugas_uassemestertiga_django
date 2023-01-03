from django.forms import ModelForm
from home.models import dataMahasiswa
class FormMahasiwa(ModelForm):
    class Meta:
      model = dataMahasiswa
      fields =  "__all__"