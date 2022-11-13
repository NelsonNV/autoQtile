import os
import datetime
import time

volumen = {
  'ideal' : 10,           # El nivel de volumen que quieres optener
  'inicial': 20,          # El volumen con el que iniciaras estos cambios
  'cadaCuanto': 14,        # Cada cuantos dias pasaran para el cambio
  'fecha': '2022-09-01',  # La fecha en la que iniciaras este proceso
  'baja': 1,              # Cuanto baja cada cuanto
}

fechaInicio = datetime.date(int(volumen['fecha'][0:4]),
                            int(volumen['fecha'][5:7]),
                            int(volumen['fecha'][8:]))
fechaActual = time.strftime('%Y-%m-%d')
fechaActual = datetime.date(int(fechaActual[0:4]),
                            int(fechaActual[5:7]),
                            int(fechaActual[8:]))
Dias = fechaActual - fechaInicio
#primero colocamos el volumen de inicio por si lo modifico alguna persona
os.system(f"amixer sset 'Master' {volumen['inicial']}%")
def calIntentos(p_inicial, p_ideal, p_bajar):
  volumen = p_inicial
  intentos = 0
  while (not p_ideal == volumen):
    intentos += 1
    volumen = volumen - p_bajar
    if volumen < p_ideal:
      break
  return intentos

volumen ['intentos'] = calIntentos(volumen['inicial'], volumen['ideal'], volumen['baja'])+1


anterior = 1
for i in range(1,(volumen['intentos']),1):
  print(f'fila {i} Cuanto {i*volumen["cadaCuanto"]} anterior: {anterior} dia :{Dias.days} baja: {i*volumen["baja"]} resultado: {volumen["inicial"]- (i *volumen["baja"])}')
  if( Dias.days <= i*volumen['cadaCuanto'] and Dias.days > anterior):
    if((volumen['inicial']-(i*volumen['baja']))< volumen['ideal'] ):
      os.system(f"amixer sset 'Master' {volumen['ideal']}%")
      break
    os.system(f"amixer sset 'Master' {volumen['inicial']-i}%")
    break

animals = {
    'a' : ['ant', 'antelope', 'armadillo'],
    'b' : ['beetle', 'bear', 'bat'],
    'c' : ['cat', 'cougar', 'camel']
}


