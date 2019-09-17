from django import forms
from .models import Event, Venue

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ('genre', 'artists', 'description', 'date', 'venue',)

  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user')
    super().__init__(*args, **kwargs)
    self.fields['venue'].queryset = Venue.objects.filter(user=user)