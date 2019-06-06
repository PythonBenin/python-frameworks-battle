"""A ReviewController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.helpers import compact


class ReviewController(Controller):
    """ReviewController Controller Class."""

    def __init__(self, request: Request):
        """ReviewController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: View):
        reviews = Review.all()

        return view.render('reviews.index', compact('reviews'))