from django.shortcuts import render,redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Destin
from .serializers import DestinSerializers
from .forms import DestinForm
import requests
from django.contrib import messages
import os

# Create your views here.
class DestinCreateView(generics.ListCreateAPIView):
    queryset=Destin.objects.all()
    serializer_class=DestinSerializers
    permission_classes=[AllowAny]

class DestinDetailView(generics.RetrieveAPIView):
    queryset=Destin.objects.all()
    serializer_class=DestinSerializers

class DestinUpdateView(generics.RetrieveUpdateAPIView):
    queryset=Destin.objects.all()
    serializer_class=DestinSerializers

class DestinDeleteView(generics.DestroyAPIView):
    queryset=Destin.objects.all()
    serializer_class=DestinSerializers

class DestinSearch(generics.ListAPIView):
    queryset=Destin.objects.all()
    serializer_class=DestinSerializers

    def get_queryset(self):
        name=self.kwargs.get('PlaceName')
        return Destin.objects.filter(PlaceName__icontains=name)

def create_destin(request):
        if request.method == 'POST':
            form=DestinForm(request.POST,request.FILES)
            print(form)
            if form.is_valid():
                try :
                    api_url="http://127.0.0.1:8000/create/"
                    form.save()
                    data=form.cleaned_data
                    print(data)
                    response=requests.post(api_url,data=data,files={'PlaceImage':request.FILES['PlaceImage']})
                    if response.status_code == 400:
                        messages.success(request,'New Destination Added Successfully')
                        return redirect('/')
                    else:
                        messages.error(request,f'Error{response.status_code}')
                except requests.RequestException as e:
                        messages.error(request,f'Error during API request {str(e)}')
            else :
                  messages.error(request,'Form is not valid')
        else:
            form=DestinForm()
        return render (request,'create_destin.html',{'form':form})


def fetch_tour(request,id):
    api_url=f'http://127.0.0.1:8000/details/{id}/'
    response=requests.get(api_url)
    if response.status_code ==200:
        data = response.json()
        overview = data['Description'].split('.')
        if request.POST: 
            temp = request.POST('GoogleMap')
            print(temp)
        return render(request,'fetch_tour.html',{'destinations':data,'overview':overview})
    return render(request,'fetch_tour.html')


def update_tour(request,pk):
    dest = Destin.objects.get(id=pk)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(dest.PlaceImage) > 0:
                os.remove(dest.PlaceImage.path)
            dest.PlaceImage = request.FILES['PlaceImage']
        dest.PlaceName = request.POST.get('PlaceName')
        dest.Weather = request.POST.get('Weather')
        dest.Location = request.POST.get('Location')
        dest.GoogleMap = request.POST.get('GoogleMap')
        dest.Description = request.POST.get('Description')
        dest.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('/')
    context = {'dest':dest}
    return render(request, 'update_tour.html', context)      

def delete_tour(request,id):
    api_url=f'http://127.0.0.1:8000/delete/{id}/'
    response=requests.delete(api_url)
    if response.status_code == 200:
        print(f'Destination with id {id} has been deleted')
    else:
        print(f'Failed to Deleted destination.status code {response.status_code}')
        return redirect('/')

def search_tour(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:
            datas = Destin.objects.filter(PlaceName__icontains = searched)
            return render(request,'search.html',{'datas': datas})
        else:
            print("Sorry !")
            return render(request,'search.html',{})


def indexs(request):
    return render(request,'indexs.html')

def packages(request):
    data = Destin.objects.all()
    return render (request,'packages.html',{'data':data})


