from django.shortcuts import render

from django.views.generic import DetailView
from .models import area_6_DMAs, area_6_bursts

class DMAmap(DetailView):
    template_name = 'DMA/DMA-detail.html'
    model = area_6_DMAs

def DMA_info(request,DMA_id):
    context_dict = {}

    DMA_objs = area_6_DMAs.objects.get(field_1 = DMA_id)
    context_dict['DMA_info'] = DMA_objs

    return render(request, 'DMA/DMA-info.html', context = context_dict)

## new

from django.http import HttpResponse

#def index(request):
    #return HttpResponse("DMA List")

def overviewMAP(request):
    context_dict = {}

    DMA_objs = area_6_DMAs.objects.all()
    context_dict['DMAs'] = DMA_objs

    top_DMAs = area_6_DMAs.objects.order_by('-leakage')[:20]
    context_dict['topDMAs'] = top_DMAs

    bursts = area_6_bursts.objects.all()
    context_dict['bursts'] = bursts
    
    return render(request, 'DMA/DMA-overview.html', context = context_dict)
