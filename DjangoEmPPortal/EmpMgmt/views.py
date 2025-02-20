from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status, serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def home(request):
    return Response(data="Hello World !")


@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    print(username, password)

    if not username or not password:
        return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
    refresh = RefreshToken.for_user(user)
    return Response({
        "message": "Login successful!",
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh)
    }, status=status.HTTP_200_OK)



@api_view(['GET'])
def getAllEmp(request):
    empList = Employee.objects.all()

    paginator = PageNumberPagination()
    paginated_empList = paginator.paginate_queryset(empList, request)

    serializedEmpList = EmployeeSerializer(paginated_empList, many=True)  
    return Response(serializedEmpList.data)


@api_view(['GET'])
def getEmpById(request):
    if not (empId := request.query_params.get('id')):
        return Response({"error": "Employee ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    employee = Employee.objects.get(id=empId)  
    serializedEmp = EmployeeSerializer(employee)  
    return Response(serializedEmp.data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addEmp(request):
    newEmployee = EmployeeSerializer(data=request.data)
    if Employee.objects.filter(**request.data).exists():
        return serializers.ValidationError('This data is already exists !')

    if not newEmployee.is_valid():
        return Response(newEmployee.errors, status=status.HTTP_400_BAD_REQUEST)
    newEmployee.save()
    return Response(newEmployee.data)


@api_view(['PATCH'])
def updateEmpById(request, id):
    try:
        employee = Employee.objects.get(id=id)  
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = EmployeeSerializer(employee, data=request.data, partial=True)  # Allow partial update

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def deleteEmp(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    employee.delete()
    return Response({"message": f'{employee.username} - Employee deleted successfully'}, status=status.HTTP_200_OK)




