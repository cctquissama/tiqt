import pytest
from model_mommy import mommy

from tiqt.apps.core.models import Ticket

pytestmark = pytest.mark.django_db


class TestTicket:
    def test_ticket_model(self):
        ticket = mommy.make('core.Ticket')
        assert ticket.status == Ticket.ABERTO, 'Should create ticket as open'

    def test_user_accept_ticket(self):
        ticket = mommy.make('core.Ticket', iniciado_em=None)
        user = mommy.make('core.User')
        ticket.iniciar_atendimento(user)
        assert ticket.responsavel == user, 'Should be tied to the user that accepted it'
        assert ticket.status == Ticket.EM_ATENDIMENTO, 'Should change state when accepted'
        assert ticket.iniciado_em is not None, 'Should not be None after ticket is accepted'


def test_departamento_str():
    dep = mommy.make('core.Departamento')
    assert str(dep) == dep.nome, 'Should return name when casting to string'


def test_secretaria_str():
    secretaria = mommy.make('core.Secretaria')
    assert str(
        secretaria) == secretaria.nome, 'Should return name when cast to string'


def test_setor_str():
    setor = mommy.make('core.Setor')
    assert str(setor) == setor.nome + ' - ' + \
        setor.secretaria.sigla, 'Should return name and secretaria when cast to string'
