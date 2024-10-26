from store.models import Product
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

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product.id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # gets id from cart
        product_ids = self.cart.keys()
        # use id to look up products in database
        products = Product.objects.filter(id__in=product_ids)
        # return those looked up products
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self,product,quantity):
        product_id= str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self,product):
        product_id = str(product)
        # delete from cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True


    def cart_total(self):
        # get product id
        product_ids = self.cart.keys()
        # look those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        # get quantities
        quantites = self.cart
        # start counting at 0
        total = 0
        for key, value in quantites.items():
            # convert key string into int so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total

