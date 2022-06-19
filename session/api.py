from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Session, CustomUser, VolunteerRequest, Turn
from session.serializers import SessionSerializer, VolunteerRequestSerializer, TurnSerializer

@api_view(['GET'])
def get_sessions(request):
    if request.user.is_authenticated:
        sessions = Session.objects.all()
        sessions_serializer = SessionSerializer(sessions, many = True)
        return Response(sessions_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_sessions_by_organization(request):

    if request.user.is_authenticated:
        sessions = Session.objects.filter(organization = request.user.id)
        sessions_serializer = SessionSerializer(sessions, many = True)
        return Response(sessions_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def insert_session(request):
    if request.user.is_authenticated:
        if request.user.user_type == "Volunteer":
            return Response({"message": "Un usuario de tipo voluntario no puede crear sesiones"}, status = status.HTTP_400_BAD_REQUEST)
        request.data["organization"] = request.user.id
        sessions_serializer = SessionSerializer(data = request.data)
        if sessions_serializer.is_valid():
            sessions_serializer.save()
            return Response(sessions_serializer.data, status = status.HTTP_200_OK)
        return Response(sessions_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getVolunteerRequests(request):
    if request.user.is_authenticated:
        requestV = VolunteerRequest.objects.filter(organization=request.user)
        request_serializer = VolunteerRequestSerializer(requestV, many=True)
        return Response(request_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_turn(request, id):

    if request.user.is_authenticated:
        volunteer = CustomUser.objects.filter(id=request.user.id).first()
        session = Session.objects.filter(id=id).first()
        turn = Turn(available=request.data['available'], full=request.data['full'], start_time=request.data['start_time'], end_time=request.data['end_time'], session=session)
        turn.save()
        turn_serializer = TurnSerializer(session)
        return Response(turn_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def insert_volunteer_in_session(request, id):

    if request.user.is_authenticated:
        volunteer = CustomUser.objects.filter(id = request.user.id).first()
        if (volunteer == None or volunteer.user_type == "Organization"):
            return Response({"message": "El id ingresado no corresponde a un usuario validov"}, status = status.HTTP_400_BAD_REQUEST) 
        session = Session.objects.filter(id = id).first()
        session.volunteer.add(request.user.id)
        session.save()
        request_volunteer = VolunteerRequest.objects.filter(session = session).filter(volunteer = volunteer).first()
        if((request_volunteer == None)):
            request_volunteer = VolunteerRequest.objects.create(status = 0,
                                session = session, organization = session.organization, volunteer = volunteer)        
            request_volunteer.save()
            sessions_serializer = SessionSerializer(session)
            return Response(sessions_serializer.data, status = status.HTTP_200_OK)
        return Response({"message": "El Usuario ya se postulo para este voluntariado"}, status = status.HTTP_400_BAD_REQUEST) 

    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def approve_volunteer_in_session(request, idSession, idVolunteer):
    if request.user.is_authenticated:
        volunteer = CustomUser.objects.filter(id = idVolunteer).first()
        if (volunteer == None or volunteer.user_type == "Organization"):
            return Response({"message": "El id ingresado no corresponde a un usuario valido"}, status = status.HTTP_400_BAD_REQUEST) 
        session = Session.objects.filter(id = idSession).first()
        sessionVolunteer = VolunteerRequest.objects.filter(session = session).filter(volunteer = volunteer).first()
        sessionVolunteer.status = 1
        sessionVolunteer.save()
        request_serializer = VolunteerRequestSerializer(sessionVolunteer)
        return Response(request_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def reject_volunteer_in_session(request, idSession, idVolunteer):
    if request.user.is_authenticated:
        volunteer = CustomUser.objects.filter(id = idVolunteer).first()
        if (volunteer == None or volunteer.user_type == "Organization") :
            return Response({"message": "El id ingresado no corresponde a un usuario valido"}, status = status.HTTP_400_BAD_REQUEST) 
        session = Session.objects.filter(id = idSession).first()
        sessionVolunteer = VolunteerRequest.objects.filter(session = session).filter(volunteer = volunteer).first()
        sessionVolunteer.status = 2
        sessionVolunteer.save()
        request_serializer = VolunteerRequestSerializer(sessionVolunteer)
        return Response(request_serializer.data, status=status.HTTP_200_OK)
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
        if session.organization == request.user:
            session_serializer = SessionSerializer(session, data = request.data)
            if session_serializer.is_valid():
                session_serializer.save()
                return Response(session_serializer.data, status = status.HTTP_200_OK)
            return Response(session_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({"message" : "El voluntariado no pertenece a la organizacion que se encuentra actualmente autenticada"}
                        , status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_session(request, id):

    if request.user.is_authenticated: 
        if session.organization == request.user: 
            session = Session.objects.filter(id = id).first()
            session.delete()
            return Response({"message":"Sesion eliminada correctamente"}, status = status.HTTP_200_OK)
        return Response({"message" : "El voluntariado no pertenece a la organizacion que se encuentra actualmente autenticada"}
                        , status = status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)
