from django import template

register = template.Library()


@register.simple_tag
def navactive(request, urls):
    if request.resolver_match.url_name in urls.split():
        return "active"
    return ""


@register.filter
def splitlist(l, n):
    return list((l[i:i+n] for i in range(0, len(l), n)))


@register.filter
def catfilter(l, cat):
    return [i for i in l if cat in i.categories.all()]


@register.filter
def isequal(i, comp):
    return i == comp


@register.filter
def difficulty(i):
    return ('success', 'info', 'warning', 'danger')[i-1]


@register.filter
def difficulty_pgbar(i):
    return ('success', 'primary', 'warning', 'danger')[i-1]
