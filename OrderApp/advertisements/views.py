from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Advertisement
from django.urls import reverse_lazy
from .filters import AdvertisementFilters


# Create your views here.

class IndexPage(TemplateView):
    template_name = "ads/index.html"


class AdsList(ListView):
    template_name = "ads/list-ads.html"
    model = Advertisement
    context_object_name = "ads"
    filterset_class = AdvertisementFilters


class AdsCreate(CreateView):
    model = Advertisement
    template_name = 'ads/create-ads.html'
    fields = ('title', 'description', 'condition', 'image', 'category')
    success_url = reverse_lazy("advertisements:ads-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AdsDetail(DetailView):
    model = Advertisement
    context_object_name = "item"
    template_name = "ads/detail-ads.html"


class AdsDelete(DeleteView):
    model = Advertisement
    success_url = reverse_lazy("")


class AdsUpdate(UpdateView):
    model = Advertisement
    template_name = "update_ads.html"
    fields = ('title', 'image', 'condition', 'description', 'category')
    success_url = reverse_lazy("advertisements:ads-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MyadsList(ListView):
    template_name = "ads/my-list-of-ads"


class ExchangeOfferList(ListView):
    template_name = "ads/list-offers"
