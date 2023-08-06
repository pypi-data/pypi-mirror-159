from .NotAuthException import NotAuthException
from .NotFoundException import NotFoundException
from flask import redirect


class ExceptionInterceptor:
    def error(self, _: Exception):
        return redirect('http://localhost:3000/error-server')

    def notFound(self, _: NotFoundException):
        return redirect('http://localhost:3000/not-found')

    def notAuth(self, _: NotAuthException):
        return redirect('http://localhost:3000/not-authority')