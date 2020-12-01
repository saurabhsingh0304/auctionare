from django.shortcuts import render, redirect, get_object_or_404
from .models import VendorUser, BidderUser
from django.contrib import messages
from .forms import VendorCreationForm, BidderCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import Status
from .serializers import VendorSerializer, BidderSerializer

# Create your views here.

def registerVendorPage(request):
    form = VendorCreationForm()
    if request.method == 'POST':
        form = VendorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form,}
    return render(request, 'accounts/index.html', context)

def registerBidderPage(request):
    form = BidderCreationForm()
    if request.method == 'POST':
        form = BidderCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form,}
    return render(request, 'accounts/index.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        context = {}
        return render(request, 'accounts/contact.html', context)
    

@login_required(login_url='login')
def home(request):
    return render(request,'accounts/home.html')


class VendorList(APIView):
    def get(self, request):
        vendor1 = VendorUser.objects.all()
        serializer = VendorSerializer(vendor1, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        pass

class BidderList(APIView):
    def get(self, request):
        bidder1 = BidderUser.objects.all()
        serializer = BidderSerializer(bidder1, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        pass