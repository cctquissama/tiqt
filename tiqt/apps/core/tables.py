from django_tables2 import Table
from tiqt.apps.core.models import Ticket


class TicketTable(Table):
    class Meta:
        model = Ticket
        attrs = {'class': 'striped'}
