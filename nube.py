from pyairtable.orm import Model
from pyairtable.orm import fields as F


class Receta(Model):
    medicamento = F.TextField('medicamento')
    interacciones = F.TextField('interacciones')
    class Meta:
        api_key = 'patW1zT1fP1c4W7fH.7d98069a294a32fb535a6fe058a6ca80bdb53114de24b899dc0b18b88764a179'
        base_id = 'appYMHFwfsmkLPdXR'
        table_name = 'receta'

