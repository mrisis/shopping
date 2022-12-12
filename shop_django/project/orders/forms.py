from django import forms

class CardAddForm(forms.Form):
    quantity=forms.IntegerField(label='',min_value=1 , max_value=10,
                                widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Quantity'}))


class CouponApplyForm(forms.Form):
    code = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control w-25','placeholder':'Coupon code'}))
