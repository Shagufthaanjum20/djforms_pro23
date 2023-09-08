from django import forms


class studentform(forms.Form):
    sname=forms.CharField(max_length=100)
    sid=forms.IntegerField()
    