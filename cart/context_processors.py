from .cart import Cart

# Create context processors so our cart works on all the pages


def cart(request):
    return {'cart': Cart(request)}