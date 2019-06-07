"""The RegisterController Module."""

from config import auth
from masonite.auth import Auth
from masonite.helpers import password as bcrypt_password
from masonite.request import Request
from masonite.view import View
from app.User import User
from masonite.auth import MustVerifyEmail
from masonite.managers import MailManager
from validator import Required, Not, Blank, validate, Length, In


class RegisterController:
    """The RegisterController class."""

    def __init__(self):
        """The RegisterController Constructor."""
        pass

    def show(self, request: Request, view: View):
        """Show the registration page.

        Arguments:
            Request {masonite.request.request} -- The Masonite request class.

        Returns:
            masonite.view.View -- The Masonite View class.
        """
        return view.render('auth/register', {'app': request.app().make('Application'), 'Auth': Auth(request)})

    def store(self, request: Request, mail_manager: MailManager):
        ok, errors = self.validate_input(request.all())

        if not ok:
            display = ''
            for error in errors:
                request.session.flash(error, '{0} {1} \n\n\n'.format(error.title(), errors[error][0]))
            return request.redirect('/register')

        user = auth.AUTH['model'].create(
            name=request.input('name'),
            password=bcrypt_password(request.input('password')),
            email=request.input('email'),
        )

        if isinstance(user, MustVerifyEmail):
            user.verify_email(mail_manager, request)

        # Login the user
        if Auth(request).login(request.input(auth.AUTH['model'].__auth__), request.input('password')):
            # Redirect to the homepage
            return request.redirect('/')

        # Login failed. Redirect to the register page.
        return request.redirect('/register')

    def validate_input(self, data):
        users = User.all()
        rules = {
            'name': [Required, Not(Blank()),Length(3)],
            'email': [Required, Not(Blank()), Not(In(users.pluck('email')))],
            'password': [Required, Not(Blank()),Length(6)],
        }

        return validate(rules, data)