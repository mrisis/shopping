from django import forms
from . models import Comment


class CommetnCreateForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('body', )
        widgets ={
            'body':forms.Textarea(attrs={'class':'form-control w-25','placeholder':'please enter your comment'})
        }


class CommentReplayForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets={
            'body':forms.Textarea(attrs={'class':'form-control w-25' , 'placeholder':'please enter your replay comment'})
        }
