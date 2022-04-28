from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Session
from session.serializers import SessionSerializer

@api_view(['GET'])
def get_sessions(request):

    if request.user.is_authenticated:
        sessions = Session.objects.all()
        sessions_serializer = SessionSerializer(sessions, many = True)
        return Response(sessions_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def insert_session(request):

    if request.user.is_authenticated:    
        sessions_serializer = SessionSerializer(data = request.data)
        if sessions_serializer.is_valid():
            sessions_serializer.save()
            return Response(sessions_serializer.data, status = status.HTTP_200_OK)
        return Response(sessions_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_session_by_id(request, id):

    if request.user.is_authenticated:
        session = Session.objects.filter(id = id).first()
        session_serializer = SessionSerializer(session)
        return Response(session_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_session(request, id):

    if request.user.is_authenticated:    
        session = Session.objects.filter(id = id).first()
        session_serializer = SessionSerializer(session, data = request.data)
        if session_serializer.is_valid():
            session_serializer.save()
            return Response(session_serializer.data, status = status.HTTP_200_OK)
        return Response(session_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_session(request, id):

    if request.user.is_authenticated:  
        session = Session.objects.filter(id = id).first()
        session.delete()
        return Response({"message":"Sesion eliminada correctamente"}, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)
