from django import forms
from .models import Purchase, Review

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['name', 'email', 'payment_method']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(choices=[
                ('credit_card', 'Credit Card'),
                ('paypal', 'PayPal'),
                ('bank_transfer', 'Bank Transfer')
            ], attrs={'class': 'form-control'}),
        }


#         }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['customer_name', 'comment', 'rating'] 