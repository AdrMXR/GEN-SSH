<p align="center"><img src="https://www.razoyo.com/wp-content/uploads/2018/12/ssh.jpg" /></p>

## Acerca de
SSH es un protocolo de administración remota que nos permite controlar uno o varios servidores por medio de internet. GEN-SSH se encarga de generar estos servidores de manera automatizada así como configuraciones o instalación de requerimientos necesarios para el buen funcionamiento de estos mismos. Esta herramienta esta enfocada en la automatización ya que ciertas configuraciones al hacerlas manualmente normalmente generan problemas hacia los usuarios. Este script aparte de facilitar esta tarea también es de gran ayuda para los principiantes o personas de menor experiencia.

## ¿Cómo funciona?
GEN-SSH consta de 2 opciones. 

* SSH local: Servidor ssh que solo nos permite conectarnos en nuestra propia red. Al seleccionar esta opción nos solicitarán crear un usuario nuevo y una contraseña que serán con los que iniciaremos en nuestro servidor ssh. También nos solicitará el puerto en el que queremos que corra nuestro servidor, por default esta el puerto 23 pero por cuestiones de seguridad es recomendable escoger un puerto diferente para evitar cierto tipo de ataques hechos por hackers. Todos estos datos serán transferidos al archivo sshd_config y se copiara a su directorio /etc/ssh para poner en marcha su servidor. Al final se nos solicitará si deseamos acceder a nuestro servidor o no. Cabe destacar que al concluir todo el procedimiento usted puede modificar manualmente el archivo sshd_config en su directorio /etc/ssh utilizando un editor de textos como nano o leafpad, puede modificar otro tipo de configuraciones como quitarle el acceso al usuario root, agregar mas usuarios o un grupo especifico de usuarios, configurar llaves ssh y entre otras cosas.

* SSH publico: Servidor ssh que nos permite conectarnos en cualquier parte del mundo con acceso a internet. Para poder generar un ssh publico es necesario configurar primero un ssh local, ya que es necesario configurar los puertos correspondientes en la configuración de nuestro router para que las peticiones publicas sean aceptadas y redirigidas a nuestro ssh local. 

Al seleccionar la segunda opción GEN-SSH nos cuestionará primero si ya contamos con un servidor ssh local, en caso de que no sea así automaticamente comenzará a instalarse y a poner en marcha los pasos anteriores. Al finalizar la instalación nos volverá a cuestionar la misma pregunta y mientras la respuesta no sea positiva el proceso se repetirá como un bucle. Ya que la respuesta sea positiva nos solicitará como primer paso nuestro gateway (puerta de enlace para acceder a la configuración de nuestro router), si no sabemos cual es nuestro gateway podemos obtenerlo con el siguiente comando: 
```bash
route -n 
```
Posteriormente, se nos abrirá automaticamente el login de nuestro router. 
<p align="center"><img src="https://github.com/AdrMXR/GEN-SSH/blob/master/screenshot-1.png" /></p>

Cabe destacar que el siguiente proceso puede variar por los diferentes modelos de routers, si tienen problemas o se traban en algun paso les recomiendo buscar en internet algún manual o tutorial para abrir puertos en su determinado router. 

Posteriormente ya que hayamos iniciado con nuestro usuario y contraseña de nuestro internet, buscaremos el apartado que se llama NAT, para configurar los puertos correspondientes. 
<p align="center"><img src="https://github.com/AdrMXR/GEN-SSH/blob/master/screenshot-2.png" /></p>

Una vez en este apartado, seleccionaremos la IP de nuestro servidor local, el puerto que configuramos en GEN-SSH al crear el servidor y escogeremos un puerto publico cualquiera, puede ser el mismo. Con ese puerto y con nuestra IP publica vamos a acceder publicamente a nuestro servidor ssh.

## ¿Cómo acceder mediante ssh?
Local:
```bash
ssh -p [PUERTO LAN] USERNAME@localhost  
```
Publico:
```bash
ssh -p [PUERTO PUBLICO] USERNAME@ip-publica 
```
Otro punto que cabe destacar es que para acceder a nuestro servidor ssh publicamente por obvias razones es necesario conectarse desde fuera de nuestra red local, ya que si lo intentamos desde nuestra red nos marcará un error. Podemos acceder mediante datos de nuestro móvil con la app de JuiceSSH para comprobar los resultados.

## Instalación 
```bash
sudo apt install python2.7 python-pip  
```
```bash
git clone https://github.com/AdrMXR/GEN-SSH.git
```
```bash
cd GEN-SSH 
```
```bash
pip install -r requirements.txt 
```
```bash
python gen-ssh.py 
```

## Screenshot de la herramienta
<p align="center"><img src="https://github.com/AdrMXR/GEN-SSH/blob/master/screenshot-3.png" /></p>

## Creditos
Creador de la herramienta: Adrian Guillermo

Facebook: https://www.facebook.com/Adrian.Guillermo.22

Instagram: https://www.instagram.com/adrian.guillermo22/

YouTube: https://www.youtube.com/channel/UCqEtxJKbIghx6lyymrjfvnA?view_as=subscriber














