from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory

from django_tables2 import MultiTableMixin

from tiqt.apps.core.models import Ticket
from tiqt.apps.core.models import Comentario
from tiqt.apps.core.tables import TicketTable
# Create your views here.


class HomeView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    template_name = 'core/home.html'
    table_pagination = {
        'per_page': 10
    }

    def get_tables(self):
        return [
            TicketTable(Ticket.objects.filter(responsavel=self.request.user)),
            TicketTable(Ticket.objects.filter(responsavel=None))
        ]


class NewTicketView(LoginRequiredMixin, CreateView):
    template_name = 'core/ticket_form.html'
    model = Ticket
    fields = ['departamento', 'setor', 'patrimonio']


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'core/ticket_form.html'
    model = Ticket
    fields = ['departamento', 'setor', 'patrimonio']


class TicketDetailView(LoginRequiredMixin, DetailView):
    template_name = 'core/ticket_detail.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = modelform_factory(
            Comentario, exclude=('criado_em', 'ticket', ))
        context["comments"] = self.object.comentario_set.all()
        return context
