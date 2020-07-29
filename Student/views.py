from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly,IsAuthenticated

@api_view(['POST',])
@permission_classes((AllowAny,))
def Student_Register(request):
    ser = Student_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("Done")
    else:
        return HttpResponse("Not Done")


@api_view(('GET',))
@permission_classes((AllowAny,))
def View_All_Student_Partial_Info(request):
    obj = Student.objects.all()
    ser = Student_Partial_Info_Serializer(obj,many=True)
    return JsonResponse(ser.data,safe=False)

@api_view(('GET',))
@permission_classes((AllowAny,))
def GetAllStudentByClassAndSection(request,grade,section):
    obj = Student.objects.all().filter(classs = grade,section = section)
    list1 = []
    for i in obj:
        dict1 = {"student_id": i.id, "student_name": i.name, "roll_number": i.roll_number}
        list1.append(dict1)
    return JsonResponse(list1, safe=False)

@api_view(('GET',))
@permission_classes((AllowAny,))
def View_Student_Detail_Info(request,pk):
    obj = Student.objects.get(id=pk)
    print(obj)
    image = "http://127.0.0.1:8000"+obj.image.url
    dict1={"name":obj.name,"class":obj.classs,"section":obj.section,"roll_number":obj.roll_number,"gender":obj.gender,"date_of_birth":obj.date_of_birth,"date_joined":obj.date_joined,"date_left":obj.date_left,"address":obj.address,"parents_name":obj.parents_name,"parents_number":obj.parents_number,"parents_occupation":obj.parents_occupation,"image":image}
    return JsonResponse(dict1,safe=False)

import datetime
@api_view(('GET',))
@permission_classes((AllowAny,))
def Upgrade_Student(request):
    obj = Student.objects.all()
    obj1 = datetime.datetime.now().year
    #obj2 = obj1.strftime('%Y') #Gives current year first month first date i.e the date when the students are supposed to be upgraded to new class.
    list=[]
    for i in obj:
        if int(i.upgrade_year)!=obj1:
            x =  int(i.classs)+1
            i.classs = x
            i.upgrade_year=obj1
            i.save()
            list.append("update")
    if len(list)!=0:
        return HttpResponse("DONE!!")
    else:
        return HttpResponse("Already UpToDate")
