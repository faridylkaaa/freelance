def prepare(qs):
    d = dict()
    for obj in qs:
        cat, price = obj.category, obj.price
        d[cat] = d.get(cat, 0) + price
    return d