from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from django.http import JsonResponse
from .models import Employee
import json


# Create your views here.
def home(request):
    return JsonResponse({"message": "Welcome Home !"}, status=200)




def getAllEmp(request):
    emplist = Employee.objects.all()
    if len(emplist) != 0:
        return JsonResponse({"employees": list(emplist.values())}, status=200)
    else:
        return JsonResponse({"message": "No Employees found"}, status=200)

 

def getEmpById(request, empId):
    emp = Employee.objects.get(id=empId)
    return JsonResponse({"message": "fetching details for the particular employee"}, status=200)
    




@csrf_exempt
def addEmp(request):
    if request.method != 'POST':
        return JsonResponse({"message": "Invalid Request"}, status=400)
    payload = json.loads(request.body)

    name, desg = payload.values()
    if (len(name) == 0 or len(desg) == 0):
        return JsonResponse({"message": "Please fill all fields"}, status=400)

    newEmp = Employee.objects.create()
    newEmp.Name = name
    newEmp.Desg = desg
    newEmp.save()
    return JsonResponse({"New Emp": "newEmp"}, status=200)


