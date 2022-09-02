from django import forms
class TransferForm(forms.Form):
    sender = forms.ChoiceField(required=True, choices=)

    receiver_account_number = forms.CharField(required=True,
                                     widget=forms.widgets.TextInput(
                                         attrs={
                                             "placeholder": "receiver account number",
                                             "class": "textinput is-success is-medium",
                                         }
                                     ),
                                     label="Receiver account number", )

    amount = forms.CharField(required=True,
                             widget=forms.widgets.NumberInput(
                                 attrs={
                                     "placeholder": "amount to be transferred",
                                     "class": "textinput is-success is-medium",
                                 }
                             ),
                             label="Amount", )
