from django.http import JsonResponse
#call this function for sending realtime data
def to_react(request,data):
    return JsonResponse(data,safe=False)#change safe = True if the data is a dictionary

def main(request):
    return JsonResponse("Main is working",safe=False)

