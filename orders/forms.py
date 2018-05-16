from django import forms
from django.contrib.auth import get_user_model 
from .models import UserAddress
User = get_user_model()
from django.contrib.auth.models import User




class UserForm(forms.Form):
    """Serializer to map the Model instance into JSON format."""
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('id','username', 'first_name', 'last_name',
                  'email', 'password',  )

class GuestCheckoutForm(forms.Form):
	email = forms.EmailField()
	email2 = forms.EmailField(label='Verify Email')

	def clean_email2(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")

		if email == email2:
			user_exist = User.objects.filter(email=email).count()
			if user_exist != 0:
				raise forms.ValidationError("user exist please login instead")
			return email2
		
        # else:
        #     raise forms.ValidationError("please confirm your email")




class AddressForm(forms.Form):
	billing_address = forms.ModelChoiceField(
			queryset= UserAddress.objects.filter(type="billing"),
			widget = forms.RadioSelect,
			empty_label = None
			)
	shipping_address = forms.ModelChoiceField(
		queryset= UserAddress.objects.filter(type="shipping"),
		widget = forms.RadioSelect,
		empty_label = None,
		
)



class UserAddressForm(forms.ModelForm):
	class Meta:
		model = UserAddress
		fields = [
			'street',
			'city',
			'state',
			'zipcode',
			'type'
		]
