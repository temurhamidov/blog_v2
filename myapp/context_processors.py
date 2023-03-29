from .models import Category, Tag

def category_list(request):
    categories = Category.objects.all()
    return {'categories' : categories}

def tags_list(request):
    tags = Tag.objects.all()
    return {'tags':tags}