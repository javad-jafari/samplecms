from shop.models import Category
def navbaritems(request):
    return {
        "categories":Category.objects.all()

        }