from rest_framework.exceptions import APIException

class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "The requested profile does not exist"