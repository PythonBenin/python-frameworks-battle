"""A ReviewController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.helpers import compact
from app.Review import Review


class ReviewController(Controller):
    """ReviewController Controller Class."""

    def __init__(self, request: Request):
        self.request = request

    def index(self, view: View):
        reviews = Review.all()
        # return view.render('reviews.index', compact(reviews))

    def create(self, view: View):
        review = Review
        return view.render('reviews.create', compact(review))