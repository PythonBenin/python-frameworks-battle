"""Web Routes."""

from masonite.routes import (
    Get as get,
    Post as post,
    Redirect as redirect,
    RouteGroup as group,
)
from .auth import AUTH_ROUTES

ROUTES = [
    get().view('/', 'welcome').name('home'),
    group(
        [
            get('/', 'ReviewController@index').name('index'),
            get("/create", "ReviewController@create").name("create"),
            post("/", "ReviewController@store").name("store"),
        ],
        prefix="/reviews",
        name="reviews.",
        middleware=("auth",),
    ),
]

ROUTES = ROUTES + AUTH_ROUTES
