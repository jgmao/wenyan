from django.forms import ModelForm
from ArticalManager.models import Artical
class ArticalForm(ModelForm):
    class Meta:
        model = Artical
        exclude=('index',)