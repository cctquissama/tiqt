from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from model_mommy import mommy
import pytest

from tiqt.apps.core import views
from tiqt.apps.core.models import Ticket

pytestmark = pytest.mark.django_db


@pytest.fixture
def factory():
    return RequestFactory()


class TestHomeView():
    def test_anonymous_user(self, factory):
        req = factory.get('/')
        req.user = AnonymousUser()
        resp = views.HomeView.as_view()(req)
        assert resp.status_code == 302 and 'login' in resp.url, "Shoud be redirected to login view"

    def test_logged_in_user(self, factory):
        req = factory.get('/')
        req.user = mommy.make('core.User')
        resp = views.HomeView.as_view()(req)
        assert resp.status_code == 200, 'Shoud view home page if logged in'


class TestNewTicketView():
    def test_anonymous_user(self, factory):
        req = factory.get('/ticket/new')
        req.user = AnonymousUser()
        resp = views.NewTicketView.as_view()(req)
        assert resp.status_code == 302 and 'login' in resp.url, "Anonymous user cannot create tickets"

    def test_logged_in_user(self, factory):
        req = factory.get('/ticket/new')
        req.user = mommy.make('core.User')
        resp = views.HomeView.as_view()(req)
        assert resp.status_code == 200, 'Shoud view home page if logged in'

    def test_should_render_the_content(self, factory):
        req = factory.get('/ticket/new')
        req.user = mommy.make('core.User')
        resp = views.NewTicketView.as_view()(req)
        resp.render()
        assert bytes('form', encoding='utf-8') in resp.content


class TestTicketDetailView():
    def test_anonymous_user(self, factory):
        mommy.make('core.Ticket')
        req = factory.get('/ticket/1')
        req.user = AnonymousUser()
        resp = views.TicketDetailView.as_view()(req, pk=1)
        assert resp.status_code == 302 and 'login' in resp.url, "Anonymous user cannot create tickets"

    def test_logged_in_user(self, factory):
        mommy.make('core.Ticket')
        req = factory.get('/ticket/1')
        req.user = mommy.make('core.User')
        resp = views.TicketDetailView.as_view()(req, pk=1)
        assert resp.status_code == 200, 'Shoud view home page if logged in'


class TestTicketUpdateView():
    def test_anonymous_user(self, factory):
        mommy.make('core.Ticket')
        req = factory.get('/ticket/1/update')
        req.user = AnonymousUser()
        resp = views.TicketUpdateView.as_view()(req, pk=1)
        assert resp.status_code == 302 and 'login' in resp.url, "Anonymous user cannot create tickets"

    def test_logged_in_user(self, factory):
        mommy.make('core.Ticket')
        req = factory.get('/ticket/1/update')
        req.user = mommy.make('core.User')
        resp = views.TicketUpdateView.as_view()(req, pk=1)
        assert resp.status_code == 200, 'Shoud view home page if logged in'


def test_ticket_accept_view(factory):
    mommy.make('core.Ticket', iniciado_em=None, pk=1)
    req = factory.get('/ticket/1/accept')
    req.user = mommy.make('core.User')
    resp = views.TicketAcceptView.as_view()(req, pk=1)
    ticket = Ticket.objects.get(pk=1)
    assert resp.status_code == 302 and 'ticket/1/' in resp.url
    assert ticket.iniciado_em is not None
    assert ticket.status is Ticket.EM_ATENDIMENTO
    assert ticket.responsavel == req.user


def test_ticket_close_view(factory):
    mommy.make('core.Ticket', encerrado_em=None, pk=1)
    req = factory.get('/ticket/1/close')
    req.user = mommy.make('core.User')
    resp = views.CloseTicketView.as_view()(req, pk=1)
    ticket = Ticket.objects.get(pk=1)
    assert resp.status_code == 302 and 'ticket/1/' in resp.url
    assert ticket.encerrado_em is not None
    assert ticket.status is Ticket.ENCERRADO


def test_ticket_post_comment(factory):
    mommy.make('core.Ticket', pk=1)
    req = factory.post('/ticket/1/comment', {'texto': "HELLO"})
    req.user = mommy.make('core.User')
    resp = views.CommentView.as_view()(req, ticket_pk=1)
    assert resp.status_code == 302 and 'ticket/1/' in resp.url
    ticket = Ticket.objects.get(pk=1)
    assert ticket.comentario_set.count() == 1
    assert ticket.comentario_set.all()[0].texto == 'HELLO'
