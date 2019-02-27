from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import csv
import pandas
df = pandas.read_csv('Inventario_Muju.csv')

class ActionStore(Action):
    def name(self):
        return 'action_store'

    def run(self, dispatcher, tracker, domain):
        tipo_prod = tracker.get_slot("tipo-producto")
        response="gg wp"
        if (tipo_prod=="gafas"):
                gafas_r=df[24][4]
                gafas_a=df[25][4]
                gafas_n=df[25][4]
                gafas_b=df[26][4]
                response = "En este momento contamos con"+ str(gafas_r) +" gafas de color rojo, "+str(gafas_a)+" azules"+ str(gafas_n)+" negras y "+str(gafas_b)+" de color blanco."

        dispatcher.utter_message(response)


        return [SlotSet('tipo-producto',tipo_prod)]



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
