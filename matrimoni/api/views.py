from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer
from .serializers import GetInTouchSerializer
from rest_framework import serializers
from rest_framework import status
from .models import GetInTouch


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all': '/',
        'Add': '/create',
        'getIntouch': '/getInTouch',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        users = Users.objects.filter(email=email)
        if users.exists():
            return Response({'message': 'User already exists'}, status=status.HTTP_409_CONFLICT)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL
    if request.query_params:
        user = Users.objects.filter(**request.query_params.dict())
    else:
        user = Users.objects.all()

    # if there is something in items else raise error
    if user:
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    print(email + " " + password)

    if email is None or password is None:
        print("email is None or password is None")
        return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

    users = Users.objects.filter(email=email)
    print(users)

    if users.exists():
        user = users.first()
        print(user.password)

        if user.password == password:
            serializer = UserSerializer(user)  # Serialize the user
            return Response(serializer.data, status=status.HTTP_200_OK)

    print("not match")
    return Response({'message': 'Password not matched'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def SaveFeedback(request):
    print("Request Data:", request.data)  # Print request data
    serializer = GetInTouchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("Serializer Errors:", serializer.errors)  # Print serializer errors for diagnosis
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def findComment(request):
    # Retrieve all comments from the GetInTouch model
    getInTouch = GetInTouch.objects.all()
    # Serialize the queryset
    serializer = GetInTouchSerializer(getInTouch, many=True)
    # Return the serialized data as a response
    return Response(serializer.data)
