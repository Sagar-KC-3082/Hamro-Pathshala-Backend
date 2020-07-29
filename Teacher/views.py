from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly,IsAuthenticated
from School_Details.models import *



@api_view(['POST',])
@permission_classes((AllowAny,))
def Teacher_Register(request):
    ser = Teacher_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("Done")
    else:
        return HttpResponse("Not Done")


@api_view(('GET',))
@permission_classes((AllowAny,))
def View_All_Teacher_Partial_Info(request):
    obj = Teacher.objects.all()
    ser = Teacher_Partial_Info_Serializer(obj,many=True)
    return JsonResponse(ser.data,safe=False)

@api_view(('GET',))
@permission_classes((AllowAny,))
def Get_Teachers_List(request):
    obj = Teacher.objects.all()
    ser = Teachers_List_Serializer(obj,many=True)
    return JsonResponse(ser.data,safe=False)



@api_view(('GET',))
@permission_classes((AllowAny,))
def View_Teacher_Detail_Info(request,pk):
    i = Teacher.objects.get(id=pk)
    id = i.id
    name = i.name
    address = i.address
    email = i.email
    phone_number = i.phone_number
    date_of_birth =i.date_of_birth
    date_of_joining = i.date_of_joining
    date_left = i.date_left
    class_teacher = i.class_teacher
    subject_head = i.subject_head
    image = "http://127.0.0.1:8000"+i.image.url

    obj = Grade_Details.objects.all().filter(teacher=name)
    list1 = []
    for j in obj:
        grade = j.grade
        section = j.section
        subject = j.subject
        dict1 = {"grade":grade,"section":section,"subject":subject}
        list1.append(dict1)

    dict2 = {"id":id,"name":name,"address":address,"email":email,"phone_number":phone_number,"date_of_birth":date_of_birth,"date_of_joining":date_of_joining,"date_left":date_left,"image":image,"class_teacher":class_teacher,"subject_head":subject_head,"class_and_section":list1}
    return JsonResponse(dict2,safe=False)
