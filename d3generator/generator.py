from d3generator.settings import CHART_TYPE
import string
import random


def generate(config):
    if config.chart_type == CHART_TYPE.RADIAL:
        return generate_radial(config)
    if config.chart_type == CHART_TYPE.GAUGE:
        return generate_gauge(config)

def generate_radial(config):
    str_list = []

    js_variable_name = ''.join(random.choice(string.ascii_uppercase) for i in range(12))

    str_list.append('var ' + js_variable_name + ' = radialProgress')
    str_list.append('(document.getElementById("'+ config.container_id +'"))')
    str_list.append('.label("'+ config.label +'")')

    return ''.join(str_list)

def generate_gauge(config):
    return ''