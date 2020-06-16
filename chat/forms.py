from django import forms


class AgencyLoginForm(forms.Form):

	email = forms.EmailField(
		label="",
		# required=False,
		widget = forms.EmailInput(
				attrs={"placeholder": "Email",
				# "class": "form-control" 
				}
			),
		)
	password = forms.CharField(
		label="",
		# required=False,
		widget = forms.PasswordInput(
				attrs={"placeholder": "Type you password here",
				# "class": "form-control" 
				}
			),
		)