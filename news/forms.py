from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from django import forms


from .models import Article, Newsletter


class ArticleForm(forms.ModelForm):
    """Form used to create and update articles.

    This form is based on the Article model.
    The fields are the title, content, and optional publisher.
    """
    class Meta:
        """Meta"""
        model = Article
        fields = ['title', 'content', 'publisher']


class NewsletterForm(forms.ModelForm):
    """Form used to create and update Newsletters.

    Journalists can set a title, description and select one or more articles
        to be part of the newsletter.
    """
    class Meta:
        """Meta"""
        model = Newsletter
        fields = ['title', 'description', 'articles']
        widgets = {
            'articles': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        """Initialise the form and add helpful help text to the fields"""
        super().__init__(*args, **kwargs)
        self.fields['title'].help_text = 'Give your newsletter a title.'
        self.fields['description'].help_text = ('Give your newsletter a '
                                                + 'summary / description.')
        self.fields['articles'].help_text = ('Select one or more articles to'
                                             + ' include in this newsletter.')
