from rest_framework.exceptions import APIException

class NotFoundException(APIException):
    status_code = 404
