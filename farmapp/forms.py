from django import forms
from .models import FarmBlock, FarmBudget, CropCalendar

class FarmBlockForm(forms.ModelForm):
    class Meta:
        model = FarmBlock
        fields = ['blockname', 'blocksize', 'crop', 'location','numberofridges', 'blockmanager', 'obstacles', 'sizeofobstacles', 'remark']
        labels = {
            'blockname': 'Block Name',
            'blocksize': 'Block Size',
            'crop': 'Crop',
            'location': 'Location',
            'numberofbridges': 'Number of Ridges',
            'blockmanager': 'Block Manager',
            'obstacles': 'Obstacles',
            'sizeofobstacles': 'Size of Obstacles',
            'remark': 'Remark',
        }

        widgets = {
            'blockname': forms.TextInput(attrs={'class': 'form-control'}),
            'blocksize': forms.NumberInput(attrs={'class': 'form-control'}),
            'crop': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'numberofridges': forms.NumberInput(attrs={'class': 'form-control'}),
            'blockmanager': forms.TextInput(attrs={'class': 'form-control'}),
            'obstacles': forms.TextInput(attrs={'class': 'form-control'}),
            'sizeofobstacles': forms.NumberInput(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }



class FarmBudgetForm(forms.ModelForm):
    
    class Meta:
        model = FarmBudget
        fields = ['farmname', 'blocks', 'crop', 'location', 'hectares', 'cropseason', 'particulars', 'productbrand', 'quantity', 'description', 'units', 'rates', 'totalcost']
        labels = {
            'farmname': 'Farm Name', 
            'blocks': 'Blocks', 
            'crop': 'Crop', 
            'location': 'Location', 
            'hectares': 'Hectares', 
            'cropseason': 'Crop Season', 
            'particulars': 'Particulars', 
            'productbrand': 'Product Brand', 
            'quantity': 'Quantity', 
            'description': 'Description', 
            'units': 'Units', 
            'rates': 'Rates', 
            'totalcost': 'Total Cost',
        }

        widgets = {
            'farmname': forms.TextInput(attrs={'class': 'form-control'}), 
            'blocks': forms.TextInput(attrs={'class': 'form-control'}), 
            'crop': forms.TextInput(attrs={'class': 'form-control'}), 
            'location': forms.TextInput(attrs={'class': 'form-control'}), 
            'hectares': forms.NumberInput(attrs={'class': 'form-control'}), 
            'cropseason': forms.TextInput(attrs={'class': 'form-control'}), 
            'particulars': forms.TextInput(attrs={'class': 'form-control'}), 
            'productbrand': forms.TextInput(attrs={'class': 'form-control'}), 
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}), 
            'description': forms.TextInput(attrs={'class': 'form-control'}), 
            'units': forms.NumberInput(attrs={'class': 'form-control'}), 
            'rates': forms.NumberInput(attrs={'class': 'form-control'}), 
            'totalcost': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CropCalendarForm(forms.ModelForm):
    class Meta:
        model = CropCalendar
        fields = ['activity', 'tasks', 'startdate', 'enddate', 'duration']
        labels = {
            'activity': 'Activity', 
            'tasks': 'Tasks', 
            'startdate': 'Start Date', 
            'enddate': 'End Date', 
            'duration': 'Duration'
            }

        widgets = {
            'activity': forms.TextInput(attrs={'class': 'form-control'}), 
            'tasks': forms.TextInput(attrs={'class': 'form-control'}), 
            'startdate': forms.DateField(), 
            'enddate': forms.DateField(), 
            'duration': forms.IntegerField()
        }