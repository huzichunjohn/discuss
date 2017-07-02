#/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from links.models import Comment

class CommentModelForm(forms.ModelForm):
    link_pk = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ('body',)
