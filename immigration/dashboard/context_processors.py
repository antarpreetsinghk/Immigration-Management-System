from .models import Branch


def branches(request):
    return {'branches': Branch.objects.all().order_by('-id'),}
