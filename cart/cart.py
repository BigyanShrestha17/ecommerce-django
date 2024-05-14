class Cart():
    def __init__(self,request):
        self.session = request.session

        # Get the session key if it exists
        cart = self.session.get('session_key')

        # if the user is ne, no session key! create one!

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

            # let's make sure that cart is available on all the page sof sites
            self.cart = cart

            