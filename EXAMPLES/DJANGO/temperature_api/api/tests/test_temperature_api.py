import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

C_TEMPS = [(-40, -40), (0, 32), (50, 122.0), (37, 98.6), (100, 212)]
F_TEMPS = [(b, a) for a, b in C_TEMPS]  # reverse!

BAD_TEMPS = ['abc']


@pytest.fixture
def api_client():
    return APIClient()

def test_c2f_call_successful(api_client):
    c2f_url = reverse('api:c2f', args=[100])
    response = api_client.get(c2f_url)
    assert response.status_code == status.HTTP_200_OK

def test_f2c_call_successful(api_client):
    f2c_url = reverse('api:f2c', args=[212])
    response = api_client.get(f2c_url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.parametrize("ctemp,expected", C_TEMPS)
def test_c2f(ctemp, expected, api_client):
    c2f_url = reverse("api:c2f", args=[ctemp])
    response = api_client.get(c2f_url)
    assert response.data.get('fahrenheit') == expected

@pytest.mark.parametrize("ftemp,expected", F_TEMPS)
def test_f2c(ftemp, expected, api_client):
    f2c_url = reverse("api:f2c", args=[ftemp])
    response = api_client.get(f2c_url)
    assert response.data.get('celsius') == expected

@pytest.mark.parametrize("bad_temp", BAD_TEMPS)
def test_c2f_bad_temps_return_error(bad_temp, api_client):
    c2f_url = reverse("api:c2f", args=[bad_temp])
    response = api_client.get(c2f_url)
    assert 'error' in response.data

@pytest.mark.parametrize("bad_temp", BAD_TEMPS)
def test_f2c_bad_temps_return_error(bad_temp, api_client):
    f2c_url = reverse("api:f2c", args=[bad_temp])
    response = api_client.get(f2c_url)
    assert 'error' in response.data

def test_c2f_missing_parameter_returns_error(api_client):
    c2f_url = reverse("api:invalid_c2f")
    response = api_client.get(c2f_url)
    assert 'error' in response.data

def test_f2c_missing_parameter_returns_error(api_client):
    f2c_url = reverse("api:invalid_f2c")
    response = api_client.get(f2c_url)
    assert 'error' in response.data
