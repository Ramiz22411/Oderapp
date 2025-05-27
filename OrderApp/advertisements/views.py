from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Advertisement
from django.urls import reverse_lazy
from .filters import AdvertisementFilters
from .forms import AdsFormCreations


# Create your views here.

class IndexPage(TemplateView):
    template_name = "ads/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad_filter = AdvertisementFilters(self.request.GET, queryset=Advertisement.objects.all())

        if self.request.GET:
            context['ads'] = ad_filter.qs
        else:
            context['ads'] = []

        context['filter'] = ad_filter
        return context


class AdsList(ListView):
    template_name = "ads/list-ads.html"
    model = Advertisement
    context_object_name = "ads"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdvertisementFilters(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class AdsCreate(CreateView):
    model = Advertisement
    template_name = 'ads/create-ads.html'
    form_class = AdsFormCreations
    success_url = reverse_lazy("ads-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AdsDetail(DetailView):
    model = Advertisement
    context_object_name = "item"
    template_name = "ads/detail-ads.html"


class AdsDelete(DeleteView):
    model = Advertisement
    success_url = reverse_lazy("my-ads")


class AdsUpdate(UpdateView):
    model = Advertisement
    template_name = "ads/update-ads.html"
    form_class = AdsFormCreations
    success_url = reverse_lazy("my-ads")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MyadsList(ListView):
    template_name = "ads/my-list-of-ads.html"
    context_object_name = "ads"
    model = Advertisement

    def get_queryset(self):
        queryset = Advertisement.objects.filter(owner=self.request.user)
        self.filterset = AdvertisementFilters(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class ExchangeOfferList(ListView):
    template_name = "ads/list-offers"
