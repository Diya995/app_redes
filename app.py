#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#app.py
#Este modulo se encarga de brindar informacion de como usar la aplicacion en heroku 
#En este archivo tambien se tienen los metodos para guardar los datos en la base de datos
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#NOTA: Los metodos aqui especificados estan sujetos a varios cambios 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#index
#Vista principal con instrucciones
#Este metodo se encarga de brindar una vista en HTML Plano con la informacion
#de como llevar a cabo los procesos dentro de la aplicacion, todos estos se 
#llevan escribiendo URLs en el navegador
@app.route('index', methods=['GET'])
def index():
	#...
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#conectarBaseDatos
#Realiza la conexion a la base de datos
#Este metodo se encarga de realizar la conexion a la base de datos
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#estadoMaquina
#Consultar estado de la maquina
#Este  metodo hace la consulta de la ultima actualizacion de estado de la maquina, almacenada
#en la base de datos
@app.route('index/estadomaquina', methods=['GET'])
def estadoMaquina():
	#...
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#estadoMaquinaParametro
#Consultar el estado de un parametro especifico de la maquina
#Este metodo se encarga de consultar la ultima actualizacion de estado de un parametro especifico 
#almacenada en la base de datos
@app.route('index/estadomaquina/<string:parametro>', methods=['GET'])
def estadoMaquinaParametro(parametro):
	#... 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#ordenarDescargaTorrent
#Ordenar la descarga de un torrent
#Este metodo se encarga de ordenar la descarga de un torrent que se hace a traves de un magnet link
# y almacena la orden en la base de datos
@app.route('index/ordenardescarga/<string:parametro>', methods=['GET'])
def ordenarDescarga(parametro):
		#...
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#consultarEstadoDescarga
#Consultar el estado de una descarga de torrent
#Este metodo se encarga de consultar el estado de una descarga de torrent anteriormente ordenada
@app.route('index/descarga/estado', methods=['GET'])
def descargaEstado():
		#...
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#