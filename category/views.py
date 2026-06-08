from django.shortcuts import render
from .models import Category


def category_list(request):
    categories = Category.objects.filter(is_active=True)

    return render(
        request,
        'categories.html',
        {'categories': categories}
    )