from django.forms import ModelForm
from .models import Connection

class ConnectForm(ModelForm):
	class Meta:
		model = Connection
		fields = ('name', 'email', 'phone', 'special_request')