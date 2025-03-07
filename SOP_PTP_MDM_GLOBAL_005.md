# CONDICIONES DE PRECIO EXPORTACION CARGA UNITARIOS A SAP MILLER E YBCP
[back](global.md)

Descripción del SOP: Carga de unitarios a SAP 	
Frecuencia del Proceso: pos solicitud 
Sistemas utilizados: SAP Heixs
Revisión: 	
Fecha de Creación:   febrero 2024	 
Número de Páginas:	
Creado por: Nallely Becerra	 
Revisado por: Ronaldo Chavez

## 1. Propósito
- Carga de unitarios a SAP de las condiciones de precio para Miller YTRP, ZFDF, ZFHH, ZFIF e YBCP

## 2. Alcance
- Carga de unitarios a SAP de las condiciones de precio para Miller YTRP, ZFDF, ZFHH, ZFIF e YBCP por solicitud tiempo de respuesta 2 días para solicitudes nuevas y carga única anual con condiciones del AP para el año siguiente la carga debe realizarse antes del 15 de diciembre, 

## 3. Responsabilidades
- Carga de unitarios a SAP de las condiciones de precio para Miller YTRP, ZFDF, ZFHH, ZFIF e YBCP por solicitud tiempo de respuesta 2 días para solicitudes nuevas y carga única anual con condiciones del AP para el año siguiente la carga debe realizarse antes del 15 de diciembre, notificada a finanzas antes para actualización de lista de precios

- La solicitud de carga de unitarios es por parte del equipo de operaciones, la solicitud de carga anual, expins solicitara el layout de carga de unitarios de AP a finanzas iniciando diciembre,

- Validación previa a la carga de la combinación ruta – SKU si existe en la conciliación previa reportar a Roberto Carlos el porqué de la modificación,


## 4. Descripción del proceso
- Para Miller
- La carga del costo logístico es por ruta en la transacción VK12 para las condiciones YTRP, ZFDF, ZFHH, ZFIF
![alt text](image-298.png)

*Miller Se carga por ruta*
- **YTRP**
  - Se ingresa en la transacción VK12 y se carga la condición YTRP.
![alt text](image-299.png)
  - Al ingresar te solicitará el company code y el material y damos F8.
![alt text](image-300.png)
  - Una vez dentro ingresarás los datos de material, Amount, Unit y Valid from y Valid to y presionamos Ctrl+S para guardar los cambios.
![alt text](image-301.png)

- **ZFDF**
  - Se ingresa en la transacción VK12 y se carga la condición ZFDF.
![alt text](image-302.png)
  - Al ingresar te solicitan los datos que se muestra en la siguiente pantalla y se llenan de acuerdo a lo que te solicitan una vez llenos presionamos F8.
![alt text](image-303.png)
  - Una vez dentro se ingresa el Customer, Mns, Material, Amount, Unit, Valid to y Valid from. Al terminar presionamos Ctrl+S para guardar los cambios.
![alt text](image-304.png)

- **ZFHH**
  - Se ingresa en la transacción VK12 y se carga la condición ZFHH.
  - Al ingresar te solicitan los datos que te muestran en la siguiente pantalla
![alt text](image-305.png)
  - Una vez dentro te solicitarán los datos de Customer, Mns, Material, Amount, Unit y Valid from/Valid to al terminar con el llenado de los datos guardamos con las teclas de Ctrl +S.
![alt text](image-306.png)

- **ZFIF**
  - Se ingresa en la transacción Vk12 en la condición ZFIF:
  - Al ingresar seleccionamos la opción Customer/Mns/Material
![alt text](image-307.png)
  - Una vez dentro ingresamos los datos que nos solicitan a cargar y presionamos F8.
![alt text](image-308.png)
  - Al dar F8 nos muestra la siguiente pantalla y nos solicita llenar Customer, Mns, Material, Amount, Unit y Valid to/ Valid from y guardamos en Ctrl+S.
![alt text](image-309.png)

- **YBCP**  
  - Se ingresa en la transacción VK12 en la condición YBCP y damos enter.
  - Al ingresar seleccionamos la opción Plant/Material.
  - Una vez dentro ingresamos los datos solicitados (Planta y Material) y damos F8.
![alt text](image-310.png)
  - En cuanto ingresamos nos arrojará la siguiente pantalla y llenamos los datos de Material, Amount, Unit y Valid from/Valid to.
![alt text](image-311.png)
<br>
**Fin del proceso**
