from django.template import Library
from utils import utils

register = Library()

@register.filter
def formata_pontuacao(var):
    return utils.formata_pontuacao(var=var)
