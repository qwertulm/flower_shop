from django import forms
from .models import *


class SubscriberForm():

    class Meta:
        model = Subscriber
        exclude = [""]

