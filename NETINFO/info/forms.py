from django.forms import Form, ModelForm
from info.models import Gateway

class GatewayForm(ModelForm):
	class Meta:
		model = Gateway
		fields = "__all__"
	