import string
from django.db.models import Q
from django.utils.text import slugify
import json
import random
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
 
def unique_slug_generator(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    Klass = instance.__class__
    max_length = Klass._meta.get_field('slug').max_length
    slug = slug[:max_length]
    qs_exists = Klass.objects.filter(slug = slug).exists()
     
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug[:max_length-5], randstr = random_string_generator(size = 2))
             
        return unique_slug_generator(instance, new_slug = new_slug)
    return slug

def remove_filter(lookup, queryset):

    query = queryset.query
    q = Q(**{lookup: None})
    clause, _ = query._add_q(q, query.used_aliases)

    def filter_lookups(child):
        return child.lhs.target != clause.children[0].lhs.target

    query.where.children = list(filter(filter_lookups, query.where.children))

