import stripe
from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse
from rest_framework.views import APIView

import django_stripe_backend
from items.models import Item
from django_stripe_backend.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY

from .serializers import ItemSerializer

DOMAIN = 'http://127.0.0.1:8000/'
stripe_api_key = STRIPE_SECRET_KEY


class ItemDetailView(APIView):

    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        serializer = ItemSerializer(item)
        context = {
            'item': serializer.data,
            'stripe_public_key': STRIPE_PUBLIC_KEY
        }

        return render(request, template_name='index.html', context=context)


class BuyView(APIView):

    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            lie_items = [
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': item.price,
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=DOMAIN + 'success/',
            cancel_url=DOMAIN + 'cancel/'
        )

        return JsonResponse({'id': checkout_session.id})
