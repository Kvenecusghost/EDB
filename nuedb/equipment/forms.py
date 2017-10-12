from django import forms

from .models import Equipment, Manufacturer, Room, Hazard

class EquipmentForm(forms.ModelForm):
    last_service = forms.DateField(widget=forms.SelectDateWidget())
    next_service = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Equipment
        fields = '__all__'


class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = '__all__'


class RoomForm(forms.ModelForm):
    # plan = forms.ImageField(
    #     label='Select an image',
    #     widget=forms.FileInput,
    # )
    # caution = forms.ModelMultipleChoiceField(
    #     widget=forms.widgets.CheckboxSelectMultiple,
    #     queryset=Hazard.objects.all())

    class Meta:
        model = Room
        fields = ('number','block', 'department', 'person_incharge',
                  'autonomous_power', 'electricity', 'gases', 'ventilation',
                  'water', 'clean_room', 'room_type', 'caution')
