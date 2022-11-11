from django.shortcuts import render
from django.http import JsonResponse
from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *  # import serializers in here

from django.contrib.auth.models import User
import uuid
@api_view(['POST'])
def register_newuser(request):
    if request.method=='POST':
        data=request.data
        print('REGISTER: ', data['username'])

        username=data.get('username')
        password=data.get('password')
        email=data.get('email')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        gender=data.get('gender')
        birthday=data.get('birthday')
        profilepic=data.get('profilepic')
        
        print('CHECK USR: ', username, password)
        if username==None and password==None:
            dt={'status':'username and password cannot be empty'}
            return Response(data=dt, status=status.HTTP_400_BAD_REQUEST)
        
        check=User.objects.filter(username=username)  # เช็คว่ามียูสเซอร์เนมนี้ไหม
        if len(check)==0:
            newuser=User()
            newuser.username=username
            newuser.set_password(password)  # sha256
            newuser.first_name=first_name
            newuser.last_name=last_name
            newuser.email=email
            newuser.save()

            newmember=Member()
            newmember.user=User.objects.get(username=username)
            newmember.Member_usertype='PATIENT'
            newmember.Member_gender=gender
            newmember.Member_birthdate=birthday
            gentoken=uuid.uuid1().hex
            newmember.Member_token=gentoken
            print(profilepic)
            newmember.Member_URLPic=profilepic
            newmember.save()
            dt={'status':'account-created', 'token':gentoken, 'first_name':first_name, 'last_name':last_name, 'username':username}
            return Response(data=dt, status=status.HTTP_201_CREATED)
        else:
            dt={'status':'user-exist'}
            return Response(data=dt, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate, login
@api_view(['POST'])
def authentiate_app(request):
    if request.method=='POST':
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        try:
            user=authenticate(username=username, password=password)
            login(request, user)
            getuser=User.objects.get(username=username)  # display info back to screen
            dt={'status':'login-succeed', 'token':getuser.member.Member_token, 'first_name':getuser.first_name, 'last_name':getuser.last_name, 
            'username':getuser.username, 'role':getuser.member.Member_usertype, 'profilepic':getuser.member.Member_URLPic,
            'birthdate':getuser.member.Member_birthdate, 'gender':getuser.member.Member_gender, 'id':getuser.id}
            print('Succeed', dt)
            return Response(data=dt, status=status.HTTP_200_OK)
        except:
            dt={'status':'login-failed'}
            return Response(data=dt, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def all_caretaker(request):
    allcaretaker=Caretaker.objects.filter(Caretaker_status=True)
    serializer=CaretakerSerializer(allcaretaker, many=True)
    caretaker_list=[]
    for i in allcaretaker:
        dt={}
        dt['id']=i.id
        dt['fullname']=i.member.user.first_name+' '+i.member.user.last_name
        dt['Caretaker_since']=i.Caretaker_since
        dt['image_url']=i.member.Member_URLPic
        caretaker_list.append(dt)

    #print(dt)
    return Response(data=caretaker_list, status=status.HTTP_200_OK)

@api_view(['GET'])
def all_medicine(request):
    allmedicine=Medicine.objects.all()
    serializer=MedicineSerializer(allmedicine, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_record(request):
    allpatient=Patient.objects.all()
    allmedicine=Medicine.objects.all()
    # print check
    for i in allpatient:
        print(i)
    for i in allmedicine:
        print(i)

    if request.method=='POST':
        serializer=RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_profile(request, UID):
    usr=User.objects.get(id=UID)
    mem=Member.objects.get(user=usr)
    print(usr.username, mem.Member_usertype, usr.id, mem.id)
    if request.method=='PUT':
        serializer1=UserSerializer(usr, data=request.data)
        if serializer1.is_valid():
            serializer2=MemberSerializer(mem, data=request.data)
            if serializer2.is_valid():
                serializer1.save()
                serializer2.save()
                profile_upd['status']='updated'
                return Response(data=profile_upd, status=status.HTTP_201_CREATED)
            return Response(serializer2.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer1.errors, status=status.HTTP_404_NOT_FOUND)

oldhomedata={"message":"hello Django my old friend"}

def Home(request):
    return JsonResponse(data=oldhomedata, safe=False, json_dumps_params={'ensure_ascii': False})
