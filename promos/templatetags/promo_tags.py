from django import template

register = template.Library()

@register.inclusion_tag('promo_tag.html')
def show_promo(promo):
    return {"promo": promo}
