from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView


# Create your views here.

class IndexPage(TemplateView):
    template_name = "ads/index.html"


class AdsList(ListView):
    pass


class AdsCreate(CreateView):
    pass


class AdsDetail(DetailView):
    pass


class AdsDelete(DeleteView):
    pass


class AdsUpdate(UpdateView):
    pass
