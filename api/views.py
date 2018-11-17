from rest_framework import generics, permissions

from quotes.models import Quote, QuoteCategory

from .serializers import QuoteSerializer, QuoteCategorySerializer


class QuoteAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer


class QuoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteAPINewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Quote.objects.all().order_by('-id')[:1] #Latest Quote
    serializer_class = QuoteSerializer