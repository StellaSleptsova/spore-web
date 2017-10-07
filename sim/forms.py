from django import forms


class ValueForm(forms.Form):
    ARG_TYPE_CHOICE = (
        ('r', 'Range'),
        ('v', 'List of values'),
    )
    type = forms.ChoiceField(label="Type of argument", choices=ARG_TYPE_CHOICE)
    name = forms.CharField(label="Element name", max_length=50)
    args = forms.CharField(label="Arguements", max_length=300)


class AddFileForm(forms.Form):
    file = forms.FileField(label="Upload file")
    name = forms.CharField(label="Include in the args as", max_length=50, required=False)


