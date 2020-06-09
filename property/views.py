from django.db.models import Q
from django.shortcuts import render

from .forms import ReserverForm
from .models import Property


# Create your views here.
def property_list(request):
    property_list = Property.objects.all()
    template = 'property/list.html'

    address_query = request.GET.get('get_query')
    property_type = request.GET.get('property_type', None)
    if address_query and property_type:
        property_list = property_list.filter(
            Q(name__icontains=address_query) &
            Q(property_type__icontains=property_type[0])
        ).distinct()

    context = {
        'property_list': property_list
    }

    return render(request, template, context)


def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'property/detail.html'

    if request.method == 'POST':
        reserve_form = ReserverForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReserverForm()

    context = {
        'property_detail': property_detail,
        'reserve_form': reserve_form
    }

    return render(request, template, context)

# Q(location__icontains=address_query) &
