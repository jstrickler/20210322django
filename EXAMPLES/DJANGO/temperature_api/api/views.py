from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse

class CelsiusToFahrenheitView(APIView):
    """A view that converts Celsius to Fahrenheit"""
    renderer_classes = [JSONRenderer]

    def get(self, request, celsius):
        try:
            celsius = float(celsius)
        except ValueError as err:
            response = {"error": str(err)}
        else:
            fahrenheit = convert_c2f(celsius)
            response = {
                "celsius": celsius,
                "fahrenheit": fahrenheit,
            }
        return Response(response)

class FahrenheitToCelsiusView(APIView):
    """A view that converts Celsius to Fahrenheit"""
    renderer_classes = [JSONRenderer]

    def get(self, request, fahrenheit):
        try:
            fahrenheit = float(fahrenheit)
        except ValueError as err:
            response = {"error": str(err)}
        else:
            celsius = convert_f2c(fahrenheit)
            response = {
                "fahrenheit": fahrenheit,
                "celsius": celsius,
            }
        return Response(response)

class ErrorHandlerView(APIView):
    """A view to provide error messages"""

    def get(self, response):
        c2f_url = reverse('api:c2f', args=['num'])
        f2c_url = reverse('api:f2c', args=['num'])

        return Response({
            'error': """This is an invalid URL""",
            'detail': f"""A numeric value must be specified. Try {c2f_url} or {f2c_url}""",
        })

def convert_c2f(c):
    """
    Convert Celsius to Fahrenheit

    :param c: Celsius temperature as int or float
    :return: Fahrenheit temperature as int or float
    """
    return ((9 * c) / 5) + 32

def convert_f2c(f):
    """
    Convert Fahrenheit to Celsius

    :param f: Fahrenheit temperature as int or float
    :return: Celsius temperature as int or float
    """
    return (f - 32) * (5 / 9)


