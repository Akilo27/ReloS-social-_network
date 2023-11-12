from .models import Menu


def menu(request):
    menus = Menu.objects.order_by('order_by')
    return {'menus': menus}