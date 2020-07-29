from Student.models import Student
from Teacher.serializers import SectionClasses_Serializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import datetime


@api_view(('POST',))
@permission_classes((AllowAny,))
def Assign_Teacher_To_Class(request):
    ser = Assign_TeacherToClass_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("Saved!!!")
    else:
        return HttpResponse("Not Saved!!")

@api_view(('GET',))
@permission_classes((AllowAny,))
def Get_Assigned_Teacher_List(request,grade,section):
    obj = Grade_Details.objects.all().filter(grade = grade,section = section)
    ser = Assign_TeacherToClass_Serializer(obj,many=True)
    return JsonResponse(ser.data,safe = False)


@api_view(['GET',])
@permission_classes((AllowAny,))
def Get_Subjects_By_Section_Class(request,grade,section,teacher):
    obj = Grade_Details.objects.all().filter(grade=grade,section=section,teacher=teacher)
    list1=[]
    for data in obj:
        list1.append(data.subject)

    return JsonResponse(list1,safe = False)



@api_view(('POST',))
@permission_classes((AllowAny,))
def Save_Section_For_Classes(request):
    print(request.data)
    ser = SectionClasses_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("Saved!!!")
    else:
        return HttpResponse("Not Saved!!!")

@api_view(('GET',))
@permission_classes((AllowAny,))
def Get_Section_For_Classes(request,grade):
    obj = ClassWithSection.objects.all().filter(grade = grade)
    list1=[]
    for sec in obj:
        list1.append(sec.section)
    return JsonResponse(list1, safe = False)



@api_view(('POST',))
@permission_classes((AllowAny,))
def Add_Section(request):
    ser = Section_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("Saved!!!")
    else:
        return HttpResponse("Not Saved!!!")

#PRINCE
@api_view(['GET',])
@permission_classes((AllowAny,))
def Get_Section_List(request):
    obj = Section.objects.all().filter()
    ser = Section_Serializer(obj,many=True)
    return JsonResponse(ser.data,safe = False)


@api_view(('POST',))
@permission_classes((AllowAny,))
def Add_Subject(request):
    ser = Subject_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status = status.HTTP_201_CREATED)
    else:
        return HttpResponse(ser.data,status = status.HTTP_400_BAD_REQUEST)

#PRINCE
@api_view(['GET',])
@permission_classes((AllowAny,))
def Get_Subject_List(request):
    obj = Subject.objects.all()
    list1=[]
    for sub in obj:
        list1.append(sub.subject)
    return JsonResponse(list1,safe = False)

#PRINCE
@api_view(['GET',])
@permission_classes((AllowAny,))
def GetStudentsListByClass(request,grade,section):
    grade = request.data.get("grade")
    section = request.data.get("section")
    obj = Student.objects.filter(classs=grade,section=section)
    list1=[]
    for i in obj:
        dict1={"student_id":i.id,"student_name":i.name,"roll_number":i.roll_number}
        list1.append(dict1)
    return JsonResponse(list1,safe=False)

#PRINCE
@api_view(['POST',])
@permission_classes((AllowAny,))
def Save_Result(request):
    ser = Result_Serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return HttpResponse("Saved!!!")
    else:
        return HttpResponse("Not Saved!!!")

#PRINCE
@api_view(['GET'])
@permission_classes((AllowAny,))
def GetResultsList(request,grade,section,exam_type):
     obj = Result.objects.all().filter(classes = grade,section = section,exam_type = exam_type)

     print(obj)
     list1 = []
     for data in obj:
         dict1 = {"student_id":data.student_id,"student_name":data.student_name,"classes":data.classes,"section":section
                  ,"roll_number":data.roll_number,"subject":data.subject,"exam_type":data.exam_type,"obtained_marks":data.obtained_marks}
         list1.append(dict1)

     return JsonResponse(list1,safe = False)

#This view is for submitting result where an eligible teacher submits result of a student of a single subject and can edit with the same view
@api_view(['POST',])
@permission_classes((AllowAny,))
def Post_Result(request):
    student_id =  request.data.get("student_id")
    student_name = request.data.get("student_name")
    roll_number = request.data.get("roll_number")
    grade = request.data.get("classes")
    section = request.data.get("section")
    exam_type =  request.data.get("exam_type")
    subject = request.data.get("subject")
    marks = request.data.get("obtained_marks")
    year = datetime.datetime.now().year
    obj2,created = Result.objects.get_or_create(student_name=student_name,year=year,exam_type=exam_type)
    print("hy")

    if subject=="English":
        obj2.english=marks
    elif subject=="Maths":
        obj2.maths=marks
    elif subject=="Nepali":
        obj2.nepali=marks
    elif subject=="SocialStudies":
        obj2.socialstudies=marks
    elif subject=="Computer":
        obj2.computer=marks
    elif subject=="Science":
        obj2.science=marks
    elif subject=="EPH":
        obj2.eph=marks

    obj2.classes = grade
    obj2.section = section
    obj2.name = student_name
    obj2.roll_number = roll_number
    obj2.student_id = student_id
    obj2.exam_type = exam_type

    # FOR CALCULATING TOTAL
    if obj2.english is None:
        eng = 0
    else:
        eng = int(obj2.english)
    if obj2.maths is None:
        ma = 0
    else:
        ma =  int(obj2.maths)
    if obj2.nepali is None:
        nep = 0
    else:
        nep = int(obj2.nepali)
    if obj2.socialstudies is None:
        soc = 0
    else:
        soc = int(obj2.socialstudies)
    if obj2.computer is None:
        comp = 0
    else:
        comp = int(obj2.computer)
    if obj2.science is None:
        sci = 0
    else:
        sci =  int(obj2.science)
    if obj2.eph is None:
        ep=0
    else:
        ep = int(obj2.eph)

    total =eng+ma+nep+soc+comp+sci+ep
    print(total)
    percentage = total/6
    obj2.total =  total
    obj2.percentage = percentage

    if obj2.percentage is None:
        percentage = 0
    else:
        percentage = int(obj2.percentage)
    if percentage>=80:
        obj2.division = "Distinction"
    elif percentage<80 & percentage>60:
        obj2.division = "First Division"
    elif percentage<60 & percentage>50:
        obj2.division = "Second Division"
    elif percentage<50:
        obj2.division = "Third Division"
    obj2.save()

    return HttpResponse("DONE!!!")


#This View returns the result of a class of a particular subject #This view is for teacher that teaches a particular subject in a class
@api_view(['GET',])
@permission_classes((AllowAny,))
def Get_Result_Of_Class_By_Subject(request):
    grade = request.GET['classes'] #request.data.get is used when some data is sent in post request bcoz in post request data is sent in body but in get request data is sent in params not in body
    section = request.GET['section']
    exam_type =  request.GET['exam_type']
    subject = request.GET['subject']
    obj = Result.objects.all().filter(classes=grade,section=section,exam_type=exam_type)
    if obj:
        list=[]
        for i in obj:
            if subject=="English":
                marks=i.english
            elif subject=="Maths":
                marks=i.maths
            elif subject=="Nepali":
                marks=i.nepali
            elif subject=="Science":
                marks=i.science
            elif subject=="EPH":
                marks=i.eph
            elif subject=="Computer":
                marks=i.computer
            elif subject=="SocialStudies":
                marks=i.socialstudies
            dict={"student_id":i.student_id,"student_name":i.student_name,"roll_number":i.roll_number,"marks":marks}
            list.append(dict)
        return JsonResponse(list,safe=False)
    else:
        return JsonResponse({"Message":"Empty Result Database"})


#This view returns the class that are taught in a class
@api_view(['GET',])
@permission_classes((AllowAny,))
def Get_Subject_Of_Class(request):
    grade = request.GET["grade"]
    section = request.GET["section"]
    obj = Grade_Details.objects.all().filter(grade=grade,section=section)
    if obj:
        list=[]
        for i in obj:
            list.append(i.subject)
        return JsonResponse(list,safe=False)
    else:
        return JsonResponse({"message":"Empty Result Database"})


#This view returns the result of a particular class
@api_view(['GET',])
@permission_classes((AllowAny,))
def Get_Result_Of_Class(request):
    grade = request.GET["grade"]
    section = request.GET["section"]
    exam_type = request.GET["exam_type"]
    obj = Result.objects.all().filter(classes=grade,section=section,exam_type=exam_type)
    print(obj)
    if obj:
        list = []
        for i in obj:
            print(obj)
            dict1 ={"maths":i.maths,"english":i.english,"nepali":i.nepali,"science":i.science,"computer":i.computer,"socialstudies":i.socialstudies,"gk":i.gk,"eph":i.eph}
            dict2={"student_id":i.student_id,"student_name":i.student_name,"subject":dict1,"total":i.total,"percentage":i.percentage,"division":i.division}
            list.append(dict2)
        return JsonResponse(list,safe=False)
    else:
        return JsonResponse({"message":"Empty Result Database"})



import datetime
from .renders import Render
@api_view(['GET',])
@permission_classes((AllowAny,))
def Result_Pdf(request):
    student = request.GET["student"]
    exam_type = request.GET["exam_type"]
    year = datetime.datetime.now().year
    obj = Result.objects.get(student_name=student,exam_type=exam_type,year=year)
    params={
        'obj':obj,
        'request':request
    }
    return Render.renders('pdf.html',params)


#This view return the result data of a particular student via student_id
api_view(['GET',])
@permission_classes((AllowAny,))
def Get_Student_Result(request):
    id = request.GET["student_id"]
    exam_type = request.GET["exam_type"]
    year = datetime.datetime.now().year
    obj = Result.objects.all().filter(student_id=id,exam_type=exam_type,year=year)
    if obj:
        for obj in obj:
            dict1 ={"maths":obj.maths,"english":obj.english,"nepali":obj.nepali,"science":obj.science,"computer":obj.computer,"socialstudies":obj.socialstudies,"gk":obj.gk,"eph":obj.eph}
            dict2 ={"student_id":obj.student_id,"student_name":obj.student_name,"roll_number":obj.roll_number,"grade":obj.classes,"section":obj.section,"exam_type":obj.exam_type,"subject":dict1,"total":obj.total,"division":obj.division,"percentage":obj.percentage}
    else:
        dict2={"message":"Student id didn't match in Database"}
    return JsonResponse(dict2)
