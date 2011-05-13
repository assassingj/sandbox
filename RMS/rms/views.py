from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rms.forms import BacklogForm
from rms.models import Product, Backlog
from django.shortcuts import get_object_or_404


class ProductView(ListView):
    context_object_name = 'product_index'
    template_name = 'rms/index.html'
    paginate_by = 5
    paginator_class = Paginator

    def get_queryset(self):
        return Product.objects.all()


class BacklogView(ListView):
    context_object_name = 'backlog_index'
    template_name = 'rms/backlog.html'
    paginate_by = 10
    paginator_class = Paginator

    def get_queryset(self):
        if len(self.args) != 0:
            product = Product.objects.get(id=self.args[0])
            if product:
                return Backlog.objects.all().filter(product=product).order_by('-gmt_last_modify')
            return self.get_all()
        return self.get_all()

    def get_all(self):
        return Backlog.objects.all().order_by('-gmt_last_modify')


def add_backlog(request, slug=None):
    form = BacklogForm(request.POST or None,instance=slug and Backlog.objects.get(slug=slug))
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('backlog_index'))
    return render_to_response('rms/backlog_editor.html',
                              {'form':form},
                              context_instance=RequestContext(request))






