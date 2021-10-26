from django import forms


class TrackerForm(forms.Form):
    number = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(TrackerForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs.update({'class': 'form-control'})
