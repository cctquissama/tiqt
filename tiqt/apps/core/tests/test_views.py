from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from model_mommy import mommy
import pytest

from tiqt.apps.core import views

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
