
# Create your views here.  
from django.http import HttpResponse  
def index(request):  
    
    html = "welcome to demo application" 
    return HttpResponse(html)    # rendering the template in HttpResponse  