from main.models import Area, State
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions

class Search(forms.Form):
    search = forms.CharField(required = False, label='Search by State')


class CityDetails(forms.Form):
    choices = [choice for choice in State.objects.all().values_list("pk", 'name')]
    print choices
    city = forms.CharField(required=True)
    county = forms.CharField(required=True)
    lat = forms.FloatField(required=False)
    lon = forms.FloatField(required=False)
    zip_code = forms.CharField(required=True)
    state = forms.ChoiceField(required=True, choices=choices)

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    # args are variables, key-word arguments are variables and a value
    # val, val2 = something
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'contact_view'
        self.helper.layout = Layout(
                Div('name', 'email', 'phone', css_class="col-md-6"),
                Div('message', css_class='col-md-6')
            )

        self.helper.layout.append(
                FormActions(
                    Submit('submit', 'Submit', css_class="btn-primary")
                )  
            )


class AreaEditForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['lat', 'lon', 'county', 'state_abbrev', 'state']

    def __init__(self, *args, **kwargs):
        super(AreaEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/city_edit/%s/' % self.instance.pk 

        self.helper.layout.append(
                FormActions(
                    Submit('submit', 'Submit', css_class="btn-primary")
                )  
            )

            





        







