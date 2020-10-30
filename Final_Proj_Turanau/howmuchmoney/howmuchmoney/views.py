from datetime import datetime
from decimal import Decimal

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    if request.method == 'GET':
        amount = 100
        selected_currency = 'BYN'
    elif request.method == 'POST':
        amount = Decimal(request.POST['amount'])
        selected_currency = request.POST['currency']

    calculated = calculate_values(amount, selected_currency)
    template_path = 'howmuchmoney/index.html'

    context = {
        'current_time': datetime.now(),
        'calculated': calculated,
        'amount': amount,
        'selected_currency': selected_currency
    }

    rendered = render_to_string(template_path, context, request=request)
    response = HttpResponse(rendered)
    return response


def calculate_values(amount, currency):
    usd_buy, usd_sale, eur_buy, eur_sale, rur_buy, rur_sale = get_rates()
    
    if currency == "BYN":
        USD = amount / usd_sale
        EUR = amount / eur_sale
        RUR = amount / rur_sale
        BYN = amount
    elif currency == "USD":
        USD = amount
        EUR = amount * usd_buy / eur_sale
        RUR = amount * usd_buy / rur_sale
        BYN = amount * usd_buy
    elif currency == "EUR":
        USD = amount * eur_buy / usd_sale
        EUR = amount
        RUR = amount * eur_buy / rur_sale
        BYN = amount * eur_buy
    elif currency == "RUR":
        USD = amount * rur_buy / usd_sale
        EUR = amount * rur_buy / eur_sale
        RUR = amount
        BYN = amount * rur_buy

    calculated = {'USD': USD, 'EUR': EUR, 'RUR': RUR, 'BYN': BYN}
    return calculated


def get_rates():
    tutby_page_response = requests.get('https://finance.tut.by/kurs/')
    tutby_page = tutby_page_response.text
    soup = BeautifulSoup(tutby_page, 'html.parser')
    elements = soup.select('td > div > p')

    usd_buy = Decimal(elements[0].text)
    usd_sale = Decimal(elements[1].text)
    eur_buy = Decimal(elements[4].text)
    eur_sale = Decimal(elements[5].text)
    rur_buy = Decimal(elements[8].text)/100
    rur_sale = Decimal(elements[9].text)/100
    return usd_buy, usd_sale, eur_buy, eur_sale, rur_buy, rur_sale