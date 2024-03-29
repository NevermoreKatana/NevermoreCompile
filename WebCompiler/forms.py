from django import forms

init = 'void main(){\n\n\n};'


class CompilerForm(forms.Form):
    input_code = forms.CharField(label='Code', initial=init, widget=forms.Textarea(attrs={
        'class': 'flex rounded-md border border-input bg-background px-3 py-2 ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 min-h-[470px] text-sm font-mono w-full resize-none',
        'placeholder': 'Enter your code here', 'id': 'code'}))
