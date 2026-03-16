from sqlalchemy import or_
from app.models.product import Product


def keyword_search(message: str, db):

    message = message.lower()

    # Split message into keywords
    words = message.split()

    query = db.query(Product).filter(Product.is_active == True)

    filters = []

    for word in words:
        filters.append(Product.name.ilike(f"%{word}%"))
        filters.append(Product.tags.ilike(f"%{word}%"))
        filters.append(Product.category.ilike(f"%{word}%"))

    if not filters:
        return []

    products = query.filter(or_(*filters)).limit(5).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "image": p.image_url,
            "link": f"/products/{p.id}"
        }
        for p in products
    ]