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
    return JsonResponse({"Emp fetched successfully": f'{emp.Name}'}, status=200)
    
def getEmpByEmail(request, empEmail):
    emp = Employee.objects.get(Email=empEmail)
    return JsonResponse({"Emp fetched successfully": f'{emp.Name}'}, status=200)



@csrf_exempt
def addEmp(request):
    if request.method != 'POST':
        return JsonResponse({"message": "Invalid Request"}, status=400)
    payload = json.loads(request.body)

    name, desg, email = payload.values()
    if (len(name) == 0 or len(desg) == 0 or email==""):
        return JsonResponse({"message": "Please fill all fields"}, status=400)

    newEmp = Employee.objects.create()
    newEmp.Name = name
    newEmp.Desg = desg
    newEmp.Email = email
    newEmp.save()
    return JsonResponse({"New Emp": f'{name} and {email} added as an employee successfully.'}, status=200)


