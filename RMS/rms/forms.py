from rms.models import Backlog

__author__ = 'gaojian'

from django import forms


class BacklogForm(forms.ModelForm):
    class Meta:
        model = Backlog
