from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Заменили 'description' на 'content'
        fields = ['title', 'content', 'category'] 

    # Валидация проверяет поле 'content'
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content and len(content) < 50:
            raise forms.ValidationError("The minimum number of characters must be 50!")
        return content

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'is_active']