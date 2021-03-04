from users.models import KmPrice


def get_user_km_price(user):
    km_price = KmPrice.objects.latest('id')
    return km_price.price