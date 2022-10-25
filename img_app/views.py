from rest_framework.decorators import api_view
from rest_framework.response import Response
import cv2

@api_view(['GET', 'POST'])
def home(request):
    f = request.FILES
    print(f)
    img = f['img'].read()
    with open('img.png', 'wb') as f:
        f.write(img)
        f.close()
    
    img = cv2.imread('img.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite('gray.png', gray)
    with open('gray.png', 'rb') as f:
        content = f.read()
    print(content)
    return Response({"status":str(content)})