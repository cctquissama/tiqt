from django.views import View
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import reverse
from django.http import HttpResponseRedirect

from django_tables2 import SingleTableMixin

from tiqt.apps.core.models import Ticket
from tiqt.apps.core.models import Comentario
from tiqt.apps.core.tables import TicketTable
# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/home.html'


class MyTicketsView(LoginRequiredMixin, SingleTableMixin, TemplateView):
    template_name = 'core/tickets_list.html'
    table_class = TicketTable
    table_pagination = {
        'per_page': 5
    }

    def get_table_data(self, **kwargs):
        return Ticket.objects.filter(status=Ticket.EM_ATENDIMENTO,
                                     responsavel=self.request.user)


class OpenTicketsView(LoginRequiredMixin, SingleTableMixin, TemplateView):
    template_name = 'core/tickets_list.html'
    table_class = TicketTable
    table_data = Ticket.objects.filter(status=Ticket.ABERTO)
    table_pagination = {
        'per_page': 5
    }


class ClosedTicketsView(LoginRequiredMixin, SingleTableMixin, TemplateView):
    template_name = 'core/tickets_list.html'
    table_class = TicketTable
    table_pagination = {
        'per_page': 5
    }

    def get_table_data(self):
        return Ticket.objects.filter(status=Ticket.ENCERRADO,
                                     responsavel=self.request.user)


class NewTicketView(LoginRequiredMixin, CreateView):
    template_name = 'core/ticket_form.html'
    model = Ticket
    fields = ['departamento', 'setor', 'patrimonio', 'contato']


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'core/ticket_form.html'
    model = Ticket
    fields = ['departamento', 'setor', 'patrimonio', 'contato']


class TicketDetailView(LoginRequiredMixin, DetailView):
    template_name = 'core/ticket_detail.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = modelform_factory(
            Comentario, exclude=('criado_em', 'ticket', ))
        context["comments"] = self.object.comentario_set.all()
        return context


class TicketAcceptView(LoginRequiredMixin, View):

    def get(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.iniciar_atendimento(request.user)
        return HttpResponseRedirect(reverse("ticket_detail", kwargs={"pk": pk}))


class CloseTicketView(LoginRequiredMixin, View):

    def get(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.encerrar_atendimento()
        return HttpResponseRedirect(reverse("ticket_detail", kwargs={"pk": pk}))


class CommentView(LoginRequiredMixin, View):

    def post(self, request, ticket_pk):
        ticket = Ticket.objects.get(pk=ticket_pk)
        comment = Comentario(ticket=ticket, texto=request.POST['texto'])
        comment.save()
        return HttpResponseRedirect(reverse("ticket_detail", kwargs={"pk": ticket_pk}))
