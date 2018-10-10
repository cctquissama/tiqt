from django_tables2 import Table, LinkColumn, A
from tiqt.apps.core.models import Ticket


class TicketTable(Table):
    id = LinkColumn('ticket_detail', args=[A('pk')])

    class Meta:
        model = Ticket
        attrs = {'class': 'striped responsive-table'}
