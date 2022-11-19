
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
from django.db.models import Sum
from rest_framework import viewsets
from home.models import Cargo, vehicleCategory,TrackCargo,CurrentLocation
from .serializers import CargoSerializer, VehicleSerializers,CargoTrackSerializer
from geopy import distance
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.



def get_distance(driver_lat, driver_long,client_lat,client_long):
    coords_1 = (float(client_lat), float(client_long))
    coords_2 = (float(driver_lat), float(driver_long))

    return distance.distance(coords_1, coords_2).km

class PostCargo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data =  request.data  
        cargo_name = data['cargo_name']
        vehicle_type =  data['vehicle_type']
        phone_number = data['phone_number']
        pick_up = data['pick_up']
        destination = data['destinanition']
        location_description = data['location_description']

        vehicle_catrgory =  vehicleCategory.objects.filter(id = int(vehicle_type))
        if(len(vehicle_catrgory) > 0):
            vehicle_cat  =  vehicleCategory.objects.get(id= int(vehicle_type))
            created =  Cargo.objects.create(
                user =  request.user,
                vehicle_type = vehicle_cat,
                phone_number = phone_number,
                pick_up = pick_up,
                cargo_name = cargo_name,
                desitnation = destination,
                location_description = location_description,
                price = random.uniform(4000.00,20000.00)
            )
            if created is not None:

                return Response({
                "success":"success",
                "message":"Created Successfully!"
            })
            else:
                return Response({
                "status":"failed",
                "message":"Error creating object"
            })

        else:
            return Response({
                "status":"failed",
                "message":"Vehicle Category does Not exist"
            })

    def get(self,request,format = None):
        queryset = Cargo.objects.filter(user =  request.user,arrived = False)
        serializer_class = CargoSerializer(queryset,many = True,read_only = True)
     
        return Response(serializer_class.data)




class GetHistory(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data =  request.data  
        cargo_id = data['cargo_id']
        status =  data['status']

        cargo_filter =  Cargo.objects.filter(id = int(cargo_id))
        if(len(cargo_filter) > 0):
            obj =  Cargo.objects.update(
                id = int(cargo_id),
                arrived = status
            )


            if obj is not None:
                return Response({
                    "status":"success",
                    "message":"cargor updated!!"

                })

            else:
                return Response({
                    "status":"failed",
                    "message":"Error Updating Cargo"
                })
        else:
            return Response({
                "status":"failed",
                "message":"Cargo does not exist"
            })



    def get(self,request,format = None):
        queryset = Cargo.objects.filter(user =  request.user,arrived = True)
        serializer_class = CargoSerializer(queryset,many = True,read_only = True)
     
        return Response(serializer_class.data)



class AllVehicleCategory(APIView):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        def get(self,request,format = None):
            queryset = vehicleCategory.objects.all()
            
            print("user id",request.user)

            usr = User.objects.get(id = request.user.id)
            client_dist = CurrentLocation.objects.filter(user =  usr).first()
            # print("client dist",client_dist.lon)
            array = []
            for k in queryset:
                print("k",k.lat,k.lon,client_dist.lat,client_dist.lon)
                ds = get_distance(k.lat,k.lon,client_dist.lat,client_dist.lon)
                print("the dispance",ds)
                array.append(float(ds))

            sorted_list = sorted(array)

            call_list = []

            for i in sorted_list:
                for j in queryset:
            
                    ds = get_distance(j.lat,j.lon,client_dist.lat,client_dist.lon)
                    if float(ds) ==  float(i):
                        call_list.append(j)


            print("sorted",sorted_list)
            
            serializer_class = VehicleSerializers(call_list,many = True,read_only = True)
        
            return Response(serializer_class.data)


class AllUserPrice(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format = None):
        queryset = Cargo.objects.filter(user =  request.user,arrived = False).aggregate(Sum('price'))

        return Response(
            {"status":"success",
            "total":queryset
            }
        )
    

class CargoTrack(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,format = None):
        cargo_id = request.data['id']

        cargo = Cargo.objects.get(id = int(cargo_id))
        cargoost =TrackCargo.objects.filter(cargos = cargo)
        ser = CargoTrackSerializer(cargoost,many= True)





        return Response(
            {"status":"success",
            "total":ser.data
            }
        )


class CurrentLocationApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format = None):
        lat = request.data['lat']
        lon = request.data['lon']

        if(float(lat) < float(-90)):
            final_lat = float(lat) - -90
            obj =  CurrentLocation.objects.create(
                        user = request.user,
                        lat = float(final_lat),
                        lon = float(lon)
                    )

            if obj is not None:
                return Response(
                        {
                            "status":"success",
                            "message":"created successuflly"
                        }
                    )
            else:
                    return Response(
                        {
                            "status":"failed",
                            "message":"Error while creating"
                        }
                    )
        elif (float(lon) < float(-90)):
            final_lat = float(lon) - -90
            obj =  CurrentLocation.objects.create(
                        user = request.user,
                        lat = float(lat),
                        lon = float(final_lat)
                    )

            if obj is not None:
                return Response(
                        {
                            "status":"success",
                            "message":"created successuflly"
                        }
                    )
            else:
                    return Response(
                        {
                            "status":"failed",
                            "message":"Error while creating"
                        }
                    )

        else:
            final_lat = float(lon) + -90
            obj =  CurrentLocation.objects.update_or_create(
                        user = request.user,
                        lat = float(lat),
                        lon = float(lon)
                    )

            if obj is not None:
                return Response(
                        {
                            "status":"success",
                            "message":"created successuflly"
                        }
                    )
            else:
                    return Response(
                        {
                            "status":"failed",
                            "message":"Error while creating"
                        }
                    )

       

        


        

        




    








    
      
       
