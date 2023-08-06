from flask import redirect
from werkzeug.exceptions import NotFound, Forbidden
from .NotFoundException import NotFoundException
from .NotAuthException import NotAuthException

class ExceptionInterceptor:
    def error(self, error: Exception):
        return redirect('http://localhost:3000/error-server')
    
    def not_found(self, error: NotFound | NotFoundException):
        return redirect('http://localhost:3000/not-found')
    
    def forbidden(self, error: Forbidden | NotAuthException):
        return redirect('http://localhost:3000/not-auth')