from users.models import KmPrice


def get_user_km_price(user):
    if user.is_staff:
        km_price = KmPrice.objects.get(id=1)
        return km_price.price
    else:
        km_price = KmPrice.objects.get(id=2)
        return km_price.price