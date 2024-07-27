from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

@api_view(["GET"])
def dt(request):
    d = datetime.now()
    msg = "Server date and time: " + str(d)
    return Response({"msg": msg})
