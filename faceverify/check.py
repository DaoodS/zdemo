from django import forms
from .models import Kyc

import time

# class KycForm(forms.ModelForm):
#     class Meta:
#         model = Kyc
#         fields = ['camera_image', 'id_image']

class KycForm(forms.Form):
    photo = forms.ImageField()
    id = forms.ImageField()

    def save(self, commit=True):
        uploaded_file1 = self.cleaned_data['photo']
        uploaded_file2 = self.cleaned_data['id']

        # Save the first image - {uploaded_file1.name}
        with open(f'media/photo_image.jpg', 'wb+') as destination:
            for chunk in uploaded_file1.chunks():
                destination.write(chunk)

        # Save the second image - {uploaded_file2.name}
        with open(f'media/id_image.jpg', 'wb+') as destination:
            for chunk in uploaded_file2.chunks():
                destination.write(chunk)
        
        time.sleep(2)
        