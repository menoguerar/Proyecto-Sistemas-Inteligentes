## story_001
* saludar
   - utter_saludar
* informar-tipo-pago
   - utter_informar_tipo_pago
* despedir
   - utter_despedir
## story_002
* saludar
   - utter_saludar
* informar-color-producto{"tipo-producto":"gafas"}
   - slot{"tipo-producto": "gafas"}
   - action_store
* despedir
   - utter_despedir
## 3
* informar-color-producto
   - utter_ask_tipo_producto
* informar-color-producto{"tipo-producto":"gafas"}
  - slot{"tipo-producto": "gafas"}
  - action_store
* informar-tipo-pago
  - utter_informar_tipo_pago
* despedir
  - utter_despedir

##4
* informar-alcance-envios{"location":"bogotá"}
  - utter_informar_alcance_envios
##5
* confirmar-tipo-pago{"empresa":"efecty"}
  - utter_informar_tipo_pago

##6
*
 - utter_informar_proceso_compra

##7
* informar-horario{"horario":"horarios"}
  - utter_confirmar_ubicaciones
## Generated Story 3098181650453234657
* saludar
    - utter_saludar
* informar-color-producto{"tipo-producto": "gafas"}
    - slot{"tipo-producto": "gafas"}
    - action_store
    - action_store
    - utter_despedir

## Generated Story 0

## Generated Story 397149037851360573
* saludar
    - utter_saludar
* informar-color-producto{"tipo-producto": "gafas", "color": "azules"}
    - slot{"color": "azules"}
    - slot{"tipo-producto": "gafas"}
* informar-color-producto{"tipo-producto": "marco", "color": "rojo"}
    - slot{"color": "rojo"}
    - slot{"tipo-producto": "marco"}

## Generated Story -2407238753886928672
* informar-color-producto{"tipo-producto": "gafas"}
    - slot{"tipo-producto": "gafas"}
    - action_store
    - slot{"tipo-producto": "gafas"}
* informar-proceso-compra
    - utter_informar_proceso_compra

