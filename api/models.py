from django.db import models

class Empresa(models.Model):
    idempresa = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.idempresa:  # Si no se proporciona un idempresa
            # Obtener el último idempresa en la base de datos
            ultimo_idempresa = Empresa.objects.order_by('-idempresa').first()

            # Si no hay registros en la base de datos, establecer el primer idempresa como "001"
            if not ultimo_idempresa:
                self.idempresa = "001"
            else:
                # Generar el siguiente idempresa
                ultimo_numero = int(ultimo_idempresa.idempresa)
                siguiente_numero = ultimo_numero + 1
                siguiente_idempresa = str(siguiente_numero).zfill(3)  # Rellenar con ceros a la izquierda si es necesario

                # Verificar si el siguiente idempresa ya existe
                while Empresa.objects.filter(idempresa=siguiente_idempresa).exists():
                    siguiente_numero += 1
                    siguiente_idempresa = str(siguiente_numero).zfill(3)

                self.idempresa = siguiente_idempresa

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.idempresa} - {self.nombre}"


from django.db import models

class TipoEnvio(models.Model):
    tipo_envio = models.CharField(max_length=1, blank=True)  # Campo no requerido
    nombre = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Convertir la primera letra del nombre a mayúscula antes de guardar
        self.nombre = self.nombre.capitalize()
        self.tipo_envio = self.nombre[0].upper() if self.nombre else ''  # Asignar la primera letra del nombre o una cadena vacía si no hay nombre
        super(TipoEnvio, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo_envio} - {self.nombre}"

class Responsable(models.Model):
    idresponsable = models.CharField(max_length=6, primary_key=True)
    nombre_apellido = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.idresponsable: 
            ultimo_idresponsable = Responsable.objects.order_by('-idresponsable').first()

            if not ultimo_idresponsable:
                self.idresponsable = "000001"
            else:
                ultimo_numero = int(ultimo_idresponsable.idresponsable)
                siguiente_numero = ultimo_numero + 1
                siguiente_idresponsable = str(siguiente_numero).zfill(6)
                while Responsable.objects.filter(idresponsable=siguiente_idresponsable).exists():
                    siguiente_numero += 1
                    siguiente_idresponsable = str(siguiente_numero).zfill(6)

                self.idresponsable = siguiente_idresponsable

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.idresponsable} - {self.nombre_apellido}"


class Planilla(models.Model):
    idplanilla = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.idplanilla} - {self.nombre}"



class Emisor(models.Model):
    idemisor = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.idemisor:  # Si no se proporciona un idempresa
            # Obtener el último idempresa en la base de datos
            ultimo_idemisor = Emisor.objects.order_by('-idemisor').first()

            # Si no hay registros en la base de datos, establecer el primer idempresa como "001"
            if not ultimo_idemisor:
                self.idemisor = "001"
            else:
                # Generar el siguiente idempresa
                ultimo_numero = int(ultimo_idemisor.idemisor)
                siguiente_numero = ultimo_numero + 1
                siguiente_idemisor = str(siguiente_numero).zfill(3)  # Rellenar con ceros a la izquierda si es necesario

                # Verificar si el siguiente idempresa ya existe
                while Emisor.objects.filter(idemisor=siguiente_idemisor).exists():
                    siguiente_numero += 1
                    siguiente_idemisor = str(siguiente_numero).zfill(3)

                self.idemisor = siguiente_idemisor

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.idemisor} - {self.nombre}"
    

class Especie(models.Model):
    idespecie = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.idespecie:  # Si no se proporciona un idempresa
            # Obtener el último idempresa en la base de datos
            ultimo_idespecie = Emisor.objects.order_by('-idespecie').first()

            # Si no hay registros en la base de datos, establecer el primer idempresa como "001"
            if not ultimo_idespecie:
                self.idespecie = "001"
            else:
                # Generar el siguiente idempresa
                ultimo_numero = int(ultimo_idespecie.idespecie)
                siguiente_numero = ultimo_numero + 1
                siguiente_idespecie = str(siguiente_numero).zfill(3)  # Rellenar con ceros a la izquierda si es necesario

                # Verificar si el siguiente idempresa ya existe
                while Especie.objects.filter(idespecie=siguiente_idespecie).exists():
                    siguiente_numero += 1
                    siguiente_idespecie = str(siguiente_numero).zfill(3)

                self.idespecie = siguiente_idespecie

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.idespecie} - {self.nombre}"
    


class Turno(models.Model):
    idturno = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.idturno:  # Si no se proporciona un idempresa
            # Obtener el último idempresa en la base de datos
            ultimo_idturno = Turno.objects.order_by('-idturno').first()

            # Si no hay registros en la base de datos, establecer el primer idempresa como "001"
            if not ultimo_idturno:
                self.idturno = "01"
            else:
                # Generar el siguiente idempresa
                ultimo_numero = int(ultimo_idturno.idturno)
                siguiente_numero = ultimo_numero + 1
                siguiente_idturno = str(siguiente_numero).zfill(2)  # Rellenar con ceros a la izquierda si es necesario

                # Verificar si el siguiente idempresa ya existe
                while Turno.objects.filter(idturno=siguiente_idturno).exists():
                    siguiente_numero += 1
                    siguiente_idturno = str(siguiente_numero).zfill(2)

                self.idturno = siguiente_idturno

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.idturno} - {self.nombre}"
    

class Consumidor(models.Model):
    idconsumidor = models.CharField(max_length=6, primary_key=True)
    nombre_apellido = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.idconsumidor: 
            ultimo_idconsumidor = Consumidor.objects.order_by('-idconsumidor').first()

            if not ultimo_idconsumidor:
                self.idconsumidor = "000001"
            else:
                ultimo_numero = int(ultimo_idconsumidor.idconsumidor)
                siguiente_numero = ultimo_numero + 1
                siguiente_idconsumidor = str(siguiente_numero).zfill(6)
                while Consumidor.objects.filter(idconsumidor=siguiente_idconsumidor).exists():
                    siguiente_numero += 1
                    siguiente_idconsumidor = str(siguiente_numero).zfill(6)

                self.idconsumidor = siguiente_idconsumidor

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.idconsumidor} - {self.nombre_apellido}"






# ------------------------------------------------------------------------------------

class ImportarAsistencia(models.Model):
    idempresa = models.CharField(max_length=6, null=True)
    tipo_envio = models.CharField(max_length=1, null=True)
    idresponsable = models.CharField(max_length=6, null=True)
    idplanilla = models.CharField(max_length=3, null=True)
    idemisor = models.CharField(max_length=3, null=True)
    idturno = models.CharField(max_length=2, null=True)
    fecha = models.CharField(max_length=8, blank=True, null=True)
    idsucursal = models.CharField(max_length=3, null=True)
    item = models.IntegerField(null=True)
    idcodigogeneral = models.CharField(max_length=8, null=True)
    idactividad = models.CharField(max_length=3, null=True)
    idlabor = models.CharField(max_length=6, null=True)
    idconsumidor = models.CharField(max_length=6, null=True)
    cantidad = models.CharField(max_length=255, blank=True)
    idespecie = models.CharField(max_length=3, null=True)  # Agregar este campo


#-------------------------------------------------------------------------------------
from django.utils import timezone
class EstadoDia(models.Model):
    fecha = models.DateField(unique=True)
    abierto = models.BooleanField(default=False)
    hora_cierre = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Estado para {self.fecha}: {'Abierto' if self.abierto else 'Cerrado'}"

    @classmethod
    def abrir_dia(cls, fecha):
        # Verificar si ya existe un registro para la fecha especificada
        try:
            estado = EstadoDia.objects.get(fecha=fecha)
            # Si ya está abierto, no permitir abrirlo de nuevo
            if estado.abierto:
                return estado
        except EstadoDia.DoesNotExist:
            # Si no existe un registro para la fecha especificada, crear uno nuevo
            pass
        
        # Crear un nuevo registro de estado para la fecha especificada
        estado = EstadoDia.objects.create(fecha=fecha, abierto=True)
        return estado
    
    def cerrar_dia(self):
        self.abierto = False
        self.hora_cierre = timezone.now().time()  # Registrando la hora de cierre
        self.save()

    @classmethod
    def determinar_estado(cls, fecha):
        try:
            estado = EstadoDia.objects.get(fecha=fecha)
            return estado.abierto
        except EstadoDia.DoesNotExist:
            return False  # Devolver cerrado si no se encuentra el registro.


#-------------------------------------------------------------------------------------
