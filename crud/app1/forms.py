from django import forms

class UserForm(forms.Form):
    # User Input Fields
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    usercontactnumber = forms.CharField(max_length=15, label='Contact Number')
    usertype = forms.ChoiceField(
        choices=[
            ('d', 'DistributorCompany'),
            ('c', 'Customer'),
            ('w', 'WirehouseManager'),
            ('f', 'Farmer'),
            ('s', 'Supplier'),
            ('a', 'Agg Officer'),
            ('n', 'Neutroshonist'),
            ('r', 'Retailer'),
        ], label='Select User Type'
    )

    # Location Fields
    latitude = forms.CharField(max_length=15, label='Latitude')
    longitude = forms.CharField(max_length=15, label='Longitude')
    street = forms.CharField(max_length=255, label='Street')
    city = forms.CharField(max_length=100, label='City')
    state = forms.CharField(max_length=100, label='State')
    country = forms.CharField(max_length=100, label='Country')
    postalcode = forms.CharField(max_length=20, label='Postal Code')
    altitude = forms.CharField(max_length=20, label='Altitude')
    timezone = forms.CharField(max_length=100, label='Timezone')

