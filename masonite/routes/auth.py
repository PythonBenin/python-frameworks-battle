from masonite.routes import Get as get, Post as post

AUTH_ROUTES = [
    get('/login', 'LoginController@show').name('auth.login'),
    get('/logout', 'LoginController@logout').name('auth.logout'),
    post('/login', 'LoginController@store'),
    get('/register', 'RegisterController@show').name('auth.register'),
    post('/register', 'RegisterController@store'),
    # Get().route('/home', 'HomeController@show').name('home'),
    # Get().route('/email/verify', 'ConfirmController@verify_show').name('verify'),
    # Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    # Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    # Get().route('/password', 'PasswordController@forget').name('forgot.password'),
    # Post().route('/password', 'PasswordController@send'),
    # Get().route('/password/@token/reset', 'PasswordController@reset').name('password.reset'),
    # Post().route('/password/@token/reset', 'PasswordController@update'),
]