from django.db import models
from django.contrib.gis.db import models as gis_models


class ReporteCrimen(models.Model):

    # Modelo que almacena reportes de crimenes ubicados geograficamente.

    ubicacion = gis_models.PointField(

            srid = 4326,
            help_text="Latitud y Longitud del incidente"
            )

    tipo_crimen = models.CharField(

            max_length=50,
            choices=[

                ('robo', 'Robo a una persona'),
                ('asalto', 'Asalto a Domicilio / Negocio'),
                ('secuestro', 'Secuestro'),
                ('extorsion', 'Extorsión'),
                ('asesinato', 'Asesinato/Homicidio'),
                ('otro', 'Otro Incidente'),
                ],
            default='robo'
            )

    fecha_hora = models.DateTimeField(


            auto_now_add = True, # Usa la hora de creacion por defecto
            help_text = "Fecha y hora del reporte"
            )

    descripcion = models.TextField(

            help_text = "Descripción detallada del incidente",
            blank = True,
            null = True,
            )

    ciudad = models.CharField(

            max_length = 100,
            help_text = "Ciudad o Sector del Incidente" 
            )

    estado_verificacion = models.CharField(

            max_length = 20,
            choices = [

                ('pendiente', 'Pendiente/En Proceso'),
                ('verificado', 'Verificado'),
                ('falso', 'Falso')
                ],
            default = 'pendiente'
            )

    class Meta:
        verbose_name = "Reporte de Crimen"
        verbose_name_plural =  "Reporte de Crimenes"
        # Indexar la publicacion mejorara el rendimiento de las consultas espaciales
        indexes = [

                models.Index(fields=['ubicacion']),
        ]

    def __str__(self):
        return f"[{self.get_tipo_crimen_display()}] en {self.ciudad} ({self.fecha_hora.date()})"

