from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timezone
import os

EMAIL= os.getenv("EMAIL", default="")
GITHUB_URL= os.getenv("GITHUB_URL", default="")

# Create your views here.
class PublicInfo(APIView):
    """
    View to get students public information.
    """

    def get(self, request, format=None):
        """
        Return the public information of the student: 
            - ```{email,
                    current datetime [in UTC format],
                    github url }```
        """
        

        info = {
            "email": EMAIL,
            "current_datetime": datetime.now(timezone.utc),
            "github_url": GITHUB_URL,
        }

        return Response(info)