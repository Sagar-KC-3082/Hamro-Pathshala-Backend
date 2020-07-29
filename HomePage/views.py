from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST',])
@permission_classes((AllowAny,))
def Post_Banner_Image(request):
    ser = Banner_Image_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("DONE!!!")
    else:
        return HttpResponse("NOT DONE!!!")




@api_view(['PUT',])
@permission_classes((AllowAny,))
def Update_Banner_Image(request):
    obj = Banner_Image.objects.all().last()
    ser = Banner_Image_Serializer(obj,data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("UPDATED!!!")
    else:
        return HttpResponse("NOT UPDATED!!!")


@api_view(['POST',])
@permission_classes((AllowAny,))
def Post_Principal_Section(request):
    ser = Principal_Section_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("DONE!!!")
    else:
        return HttpResponse("NOT DONE!!!")


@api_view(['PUT',])
@permission_classes((AllowAny,))
def Update_Principal_Section(request):
    obj = Principal_Section.objects.all().last()
    ser = Principal_Section_Serializer(obj,data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("UPDATED!!!")
    else:
        return HttpResponse("NOT UPDATED!!!")


@api_view(['POST',])
@permission_classes((AllowAny,))
def Post_Notice(request):
    print(request.data)
    obj = Notice_Serializer(data=request.data)
    if obj.is_valid():
        obj.save()
        return HttpResponse(obj.data,status = status.HTTP_200_OK)
    else:
        return Response(obj.data,status = status.HTTP_400_BAD_REQUEST)



@api_view(['PUT',])
@permission_classes((AllowAny,))
def Update_Notice(request,pk):
    flag=request.data.get("flag")
    obj = Notice.objects.get(id=pk)
    ser = Notice_Serializer(obj,request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("UPDATED!!!")
    else:
        return HttpResponse("Not Updated!!!")


@api_view(['GET',])
@permission_classes((AllowAny,))
def View_Notice(request):
    obj = Notice.objects.all()
    list1 = []
    for i in obj:
        if i.image_notice != "":
            image_notice = "http://127.0.0.1:8000"+i.image_notice.url
            print(image_notice)
        else:
            image_notice=""
        dict={"id":i.id,"text_notice":i.text_notice,"image_notice":image_notice,"date_created":i.date_created}
        list1.append(dict)
    return JsonResponse(list1,safe=False)


@api_view(['POST',])
@permission_classes((AllowAny,))
def Post_Marquee(request):
    ser = Marquee_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("DONE!!!")
    else:
        return HttpResponse("NOT DONE!!!")


@api_view(['PUT',])
@permission_classes((AllowAny,))
def Update_Marquee(request,pk):
    obj = Marquee.objects.get(id=pk)
    print(obj)
    ser = Marquee_Serializer(obj,data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("UPDATED!!!")
    else:
        return HttpResponse("NOT UPDATED!!!")


@api_view(['GET',])
@permission_classes((AllowAny,))
def View_Marquee(request):
    obj = Marquee.objects.all()
    list1 = []
    for i in obj:
        dict1 = {"id":i.id,"marquee_text":i.marquee_text,"status":i.status}
        list1.append(dict1)
    return JsonResponse(list1,safe=False) #List.data is not used bcoz that is done only when we use serializer class object not when we use our custom objects..


@api_view(['POST',])
@permission_classes((AllowAny,))
def Post_Other(request):
    ser = Other_Section_Serializer(data=request.data)
    print(ser.is_valid())
    if ser.is_valid():
        data = ser.save()
        print("data")
        return HttpResponse("DONE!!!")
    else:
        return HttpResponse("NOT DONE!!!")


@api_view(['PUT',])
@permission_classes((AllowAny,))
def Update_Other(request,pk):
    obj = Other_Section.objects.get(id=pk)
    ser = Other_Section_Serializer(instance=obj,data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("UPDATED!!!")
    else:
        return HttpResponse("NOT UPDATED!!!")


@api_view(['GET',])
@permission_classes((AllowAny,))
def View_Other(request):
    obj = Other_Section.objects.all()
    ser = Other_Section_Serializer(obj,many=True,context={"request":request})
    return JsonResponse(ser.data,safe=False)



@api_view(['POST',])
@permission_classes((AllowAny,))
def Post_About_School(request):
    ser = About_School_Serializer(data=request.data)
    if ser.is_valid():
        data = ser.save()
        print("data")
        return HttpResponse("DONE!!!")
    else:
        return HttpResponse("NOT DONE!!!")


@api_view(['GET',])
@permission_classes((AllowAny,))
def View_About_School(request):
    obj = About_School.objects.all()
    ser = About_School_Serializer(obj,many=True,context={"request":request})
    return JsonResponse(ser.data,safe=False)

@api_view(['PUT',])
@permission_classes((AllowAny,))
def Update_About_School(request,pk):
    obj = About_School.objects.get(id=pk)
    ser = About_School_Serializer(instance=obj,data=request.data)
    print(ser)
    if ser.is_valid():
        ser.save()
        return HttpResponse("UPDATED!!!")
    else:
        return HttpResponse("NOT UPDATED!!!")

@api_view(['GET',])
@permission_classes((AllowAny,))
def View_Homepage1(request):
    obj = Banner_Image.objects.all().last()
    if obj.Banner_Image1=="":
        image1 = ""
        dict1 = {"image":"Null"}
    else:
        image1 = "http://127.0.0.1:8000"+obj.Banner_Image1.url
        image1_caption_heading = obj.Banner_Image1_caption_heading
        image1_caption = obj.Banner_Image1_caption
        image1_status = obj.Banner_status1
        dict1 = {"src":image1,"caption_heading":image1_caption_heading,"caption":image1_caption,"status":image1_status}

    if obj.Banner_Image2 =="":
        image2 = ""
        dict2 = {"image":"Null"}
    else:
        image2 = "http://127.0.0.1:8000"+obj.Banner_Image2.url
        image2_caption_heading = obj.Banner_Image2_caption_heading
        image2_caption = obj.Banner_Image2_caption
        image2_status = obj.Banner_status2
        dict2 = {"src":image2,"caption_heading":image2_caption_heading,"caption":image2_caption,"status":image2_status}

    if obj.Banner_Image3 =="":
        image3 = ""
        dict3 = {"image":"Null"}
    else:
        image3 = "http://127.0.0.1:8000"+obj.Banner_Image3.url
        image3_caption_heading = obj.Banner_Image3_caption_heading
        image3_caption = obj.Banner_Image3_caption
        image3_status = obj.Banner_status3
        dict3 = {"src":image3,"caption_heading":image3_caption_heading,"caption":image3_caption,"status":image3_status}

    if obj.Banner_Image4 =="":
        image4 = ""
        dict4 = {"image":"Null"}
    else:
        image4 = "http://127.0.0.1:8000"+obj.Banner_Image4.url
        image4_caption_heading = obj.Banner_Image4_caption_heading
        image4_caption = obj.Banner_Image4_caption
        image4_status = obj.Banner_status4
        dict4 = {"src":image4,"caption_heading":image4_caption_heading,"caption":image4_caption,"status":image4_status}

    if obj.Banner_Image5 =="":
        image5 = ""
        dict5 = {"image":"Null"}
    else:
        image5 = "http://127.0.0.1:8000"+obj.Banner_Image5.url
        image5_caption_heading = obj.Banner_Image5_caption_heading
        image5_caption = obj.Banner_Image5_caption
        image5_status = obj.Banner_status5
        dict5 = {"src":image5,"caption_heading":image5_caption_heading,"caption":image5_caption,"status":image5_status}

    if obj.Banner_Image6  =="":
        image6= ""
        dict6 = {"image":"Null"}
    else:
        image6 = "http://127.0.0.1:8000"+obj.Banner_Image6.url
        image6_caption_heading = obj.Banner_Image6_caption_heading
        image6_caption = obj.Banner_Image6_caption
        image6_status = obj.Banner_status6
        dict6 = {"src":image6,"caption_heading":image6_caption_heading,"caption":image6_caption,"status":image6_status}
    data1 = [dict1,dict2,dict3,dict4,dict5,dict6]
    dict = {"banner_images":data1}
    return JsonResponse(dict,safe=False)


api_view(['GET',])
@permission_classes((AllowAny,))
def View_Homepage2(request):

    obj1 = Principal_Section.objects.all().last()
    obj2 = Marquee.objects.filter(status="Active")
    obj3 = Notice.objects.filter(status="Active")
    Principal_Image = "http://127.0.0.1:8000"+obj1.principal_image.url
    dict1 = {"principal_image":Principal_Image,"principal_message":obj1.principal_message}
    # dict2 = {"principal_section":dict1}

    list1 = []
    for i in obj2:
        marquee_text = i.marquee_text
        list1.append(marquee_text)
    #dict3 = {"marquee_section":list1}

    list2 = []
    list3 = []
    for i in obj3:
        if i.text_notice!="":
            text_notice = i.text_notice
            list2.append(text_notice)
            print(list2)
        if i.image_notice!="":
            image_notice = "http://127.0.0.1:8000"+i.image_notice.url
            list3.append(image_notice)

    dict4 = {"text_notice":list2,"image_notice":list3}
    # dict5 = {"notice_section":dict4}
     #list_final = [dict2,dict3]
    finalDict = {"principle_section":dict1,"marquee_section":list1,"notice":dict4}
    return JsonResponse(finalDict,safe=False)



api_view(['GET',])
@permission_classes((AllowAny,))
def View_Homepage3(request):
    obj = Other_Section.objects.all().filter(status="Active").order_by('-id') #Shows only latest 3 objects
    obj1 = About_School.objects.all().last()
    print(obj1)
    list1 = []
    list2 = []
    count = 0  #TO MAKE SURE THAT ATMOST 3 OBJECTS ARE ONLY SENT EVEN THOUGH MORE THAN 3 OBJECTS HAVE FLAG SET AS ACTIVE
    for i in obj:
        count = count+1
        if count>3:
            break
        else:
            if i.image:
                image = "http://127.0.0.1:8000"+i.image.url
            else:
                image = "None"
            title = i.title
            description = i.description
            dict1={"image":image,"title":title,"description":description}
            list1.append(dict1)

    print("hyyy")
    images = "http://127.0.0.1:8000"+obj1.image.url
    texts = obj1.text
    print(texts)
    dict2={"image":images,"text":texts}
    list2.append(dict2)
    dict3 ={"Other_Section":list1,"About_School":list2}
    return JsonResponse(dict3)
