from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .serializers import UserSerializers, UserListSerializers, UserActivitySerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .models import activity
from rest_framework import viewsets
from django.http import JsonResponse



#online users:

#class UserActivityViewSet(viewsets.ModelViewSet):
 #   queryset = activity.objects.all().order_by('-timestamp')  # Order by most recent
 #   serializer_class = UserActivitySerializer  
    
 #   def get_queryset(self):
  #      queryset = super().get_queryset()
        # You can filter by specific user or timeframe here
   #     return queryset



# API Overview View
@api_view(['GET'])
def api_overview(request):
    """
    Provides an overview of the available API endpoints.
    """
    api_urls = {
        'to login to your account ': 'login/',
        'to sign-up for the first time ': 'signup/',
        'to test token validity ': 'test_token/',
    }
    return Response(api_urls)


#################################################################

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, email = request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"details": "wrong password"}, status = status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializers(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(email = request.data['email'])
        user.set_password(request.data['password']) #to make sure password is hashed
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):

    return Response("passed for {}".format(request.user.email))   #request is passed for the email of user whose token was just provided 


###################################
# retrieve users:

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class =UserListSerializers

# retrieve active user:

class UserOnlineView(generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)  # Filter by active users
    serializer_class = UserListSerializers  
    
###################################################################3
