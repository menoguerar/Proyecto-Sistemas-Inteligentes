from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'action_weather'
        
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot("tipo-producto")
        print("<--------------",tracker.get_latest_entity_values)
        response = "El clima es una mierdaaaaaa en "+mylocation(loc)
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]

def mylocation(location):
    return location+"xD"


def informar_tipo_pago():
    return ("Lo tenemos disponible en Bogotá, desde el barrio Venecia al sur, hasta la 170 de la Autopista Norte. Por favor indíquenos su dirección, su número móvil y el horario en que podemos realizar la entrega.")

def informar_tienda_horarios():
    return ("De lunes a viernes de 6.30pm á 8.30pm y los fines de semana de 8.00am á 8.00pm")

def informar_tiempoEntrega_fuera():
    return ("Buen día,para bogotá la entrega es inmediata, fuera de bogota son dos días hábiles, es decir, si se compra mañana llegaría el miércoles")
def informar_producto_sexo():
    return("sirven tanto para hombre y para mujer")
def informar_producto_restock():
    return("BAse de datos")

def informar_producto_repuesto():
     return("No contamos con los repuestos, solo el kit completo")
def informar_producto_calidad():
    return("Son Rockbros originales")
def informar_producto_atributo():
    return("base de datos")
def informar_producto(tipo):
    return("bd tipo prodcuto")

def informar_proceso_compra():
    return """Lo puedes realizar:
    a) Visitando cualquiera de nuestros locales en Hayuelos y Salitre El Greco
    b) Por el pago a través de un enlace web de Mercado Pagos que le permite pagar en efectivo por Efecty
    o Baloto, por tarjeta de débito o por tarjeta de crédito
    (https://www.mercadopago.com/mco/checkout/start?pref_id=192583938_cd231fd6_78a1_4c76_b350_e2ff87ece864)
    c) Por Mercado Libre: https://articulo.mercadolibre.com.co/MCO_453032170_gafas_ciclismo_
    profesionales_rockbros_5_lentes__JM?quantity=1"""

def informar_color_producto():
    return "consulta bd"
def informar_alcance_envios():
    return"""Si! a través de Mercado Envíos de Mercado Libre, o si gusta, realiza la compra indicando que recogera
    el producto y se lo enviamos por Envía y ud. Paga por el valor del transporte cuando reciba el producto.
    Por su tranquilidad, nosotros le enviaremos el número de guía para su seguimiento."""
def confirmar_ubicaciones():
    return "Puedes pasar de lunes a viernes de 6.30pm á 8.30pm y los fines de semana de 8.00am á 8.00pm, por favor confirmar su hora de llegada al numero 320 3475909" 
    
def confirmar_tipo_pago():
    return """Puedes tratar directamente con la opción de Mercado Envíos.
     Si no figura, podemos enviárselo por otro medio y ud. paga el valor del transporte cuando reciba el producto.
     Al comprarlo, selecciona la opción de que ud. recoge el producto"""


#  def tipo_intent(intent):
#     switcher = {
#         1: informar_tipo_pago,
#         2: informar_tienda_horarios,
#         3: informar_tiempoEntrega,
#         4: informar_producto_sexo,
#         5: informar_producto_restock,
#         6: informar_producto_repuesto,
#         7: informar_producto_calidad,
#         8: informar_producto_atributo,
#         9: informar_producto,
#         10: informar_proceso_compra,
#         11: informar_horario,
#         12: informar_color_producto,
#         13: informar_alcance_envios,
#         14: confirmar_ubicaciones,
#         15: confirmar_tipo_pago
#         16: informar-ubicaciones
#         17: informar-tipo-venta
#         18: informar-proceso-compra-PSE
#         19: informar-envio-empresa
#         20: informar-envio-costo
#         21: informar-contacto
#         22: devolver-gracias
#     }
#     Get the function from switcher dictionary
#     func = switcher.get(argument, lambda: "Invalid month")
#     Execute the function
#     print func()