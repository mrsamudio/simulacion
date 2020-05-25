# Función seno
import bpy
import numpy as np
from math import sin

# Configuración de las variables globales
scene = bpy.data.scenes['Scene']
g = 360 # grados de la circunferencia
obj = bpy.data.objects
objops = bpy.ops.object
objactive = bpy.context.scene.objects

# Configuración de la escena
def escena():
    #bpy.context.area.type = 'TIMELINE'
    bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
    bpy.context.scene.show_subframe = True
    bpy.context.scene.frame_start = 0
    bpy.context.scene.frame_end = 360
    pass

# Selecting objects by name
def seleccionar(objName):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[objName].select = True

# Delete an object by name
def borrar(objName):
    seleccionar(objName)
    bpy.ops.object.delete(use_global=False)

# Crear un objeto
def crearObjeto():
    bpy.ops.mesh.primitive_uv_sphere_add( size=0.5, location=(0, -8, 0) )
    bpy.context.object.name = 'Esfera'
    pass

#---------------------------------------------------------------------
# Ejecución de funciones
borrar('Cube')
escena()
crearObjeto()
#---------------------------------------------------------------------

# Gráfica del seno, trayectoria del objeto
for i, j in zip(range(g), np.arange(0, 1 , 0.00025)):
    bpy.context.scene.frame_float = i # al frame
    bpy.ops.transform.translate(value=(0, j, sin(i)))
    scene.timeline_markers.new( f'{i}', frame = i ) # crea un nuevo marcador para el timeline

# Ir al primer frame para iniciar la reproducción en el Timeline desde la interfaz
bpy.context.scene.frame_set(0)

# limpiar restricciones
objops.constraints_clear()

# Seleccionar y Activar la camara
obj['Camera'].select = True
objactive.active = obj['Camera']

# Configuración de la restricción de la Cámara
objops.constraint_add(type='TRACK_TO')
bpy.context.active_object.constraints['Track To'].target = obj['Esfera']
bpy.context.active_object.constraints['Track To'].up_axis       = 'UP_Y'
bpy.context.active_object.constraints['Track To'].track_axis    = 'TRACK_NEGATIVE_Z'