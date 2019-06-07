"""A ReviewController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.helpers import compact
from app.Review import Review
from validator import Required, Not, Blank, validate


class ReviewController(Controller):
    """ReviewController Controller Class."""

    def __init__(self, request: Request):
        self.request = request

    def index(self, view: View):
        reviews = Review.all()
        return view.render('reviews.index', compact(reviews))

    def create(self, view: View):
        review = Review
        return view.render('reviews.create', compact(review))

    def store(self, view: View):
        ok, errors = self.validate_input(self.request.all())

        if not ok:
            for error in errors:
                self.request.session.flash(error, '{0} {1} \n\n\n'.format(error.title(), errors[error][0]))
            return self.request.redirect_to('reviews.create')

        Review.create(
            company=self.request.input('company'),
            job=self.request.input('job'),
            headline=self.request.input('headline'),
            pros=self.request.input('pros'),
            cons=self.request.input('cons'),
            user_id=self.request.user().id,
        )

        return self.request.redirect_to('reviews.index')


    def validate_input(self, data):
        rules = {
            'company': [Required, Not(Blank())],
            'job': [Required, Not(Blank())],
            'headline': [Required, Not(Blank())],
            'pros': [Required, Not(Blank())],
            'cons': [Required, Not(Blank())],
        }
        return validate(rules, data)