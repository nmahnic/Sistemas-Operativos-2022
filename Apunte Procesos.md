# Procesos
Los objetos que conforman la imagen de un programa (código, pila,y datos) están originalmente en algún medio masivo de almacenamiento.
La (text section), la (data section) que contiene las variables globales, y demás secciones componen esta imagen. 
Pero un proceso es bastante mas que eso. Es la instancia de ejecución de un programa en la memoria del sistema.

![2 Procesos](https://github.com/nmahnic/Sistemas-Operativos-2022/blob/master/img/procesos1.png)

Un proceso involucra mucha información además de su código y sus datos:
- Los file descriptors de los archivos abiertos por el programa,
- Las señales pendientes de atención,
- El estado interno del kernel para ese proceso
- El contexto de la CPU (valores de cada registro de la CPU),
- El espacio de direcciones de memoria,
- Estará ligado al usuario que lo ejecuta (tendrá sus permisos, sus variables de entorno, su HOME directory, etc)
- La prioridad de ejecución (el % de tiempo de CPU que el kernel le asignará para su ejecución)

![Espacio de memoria de un proceso](https://github.com/nmahnic/Sistemas-Operativos-2022/blob/master/img/procesos2.png)

Para ver el estados de los procesos que están corriendo en la PC puede ejecutar
```
ps -ely
```
![Procesos ](https://github.com/nmahnic/Sistemas-Operativos-2022/blob/master/img/procesos3.png)

Los UNIX identifican a los procesos con un Process ID (PID). LosPID van desde 0 a 32767.
- S: state. 
    - D: Uninterruptible sleep
    - R: Running or runnable (en run queue) 
    - S: Interruptible sleep (esperando que      se complete un evento) 
    - T: Stopped, por señal SIGTOP o si está en siendo Traced.
    - W: paging (inválido desde kernel 2.6.xx) 
    - X: Dead (nunca deberíamos verlo) 
    - Z: Defunct ("zombie") 

- UID: User ID. Es quien ejecutó el proceso. 
- PID: Process ID. 
- PPID: Parent Process ID.
- C: Uso de CPU. Es el porcentaje de uso de CPU sobre el tiempo de vida del proceso
- PRI: Prioridad. A mayor valor menor prioridad
- NI: Valor nice. (-19 a 20). nice modifica la prioridad desde el shell
- SZ: tamaño en páginas físicas de la imagen  core del proceso. Esto incluye el espacio para secciones text, data, y stack.
- WCHAN: Nombre de la función del kernel en la que el proceso está durmiendo y si el proceso está Running.
- STIME: Fecha de creación.
- TTY: Terminal asociada.
- TIME: Tiempo de CPU acumulado (por el kernel y el proceso) hh:mm:ss.
- CMD: comando ejecutado para crear el proceso.

## Ciclo de vida de un Proceso 
![Procesos ](https://github.com/nmahnic/Sistemas-Operativos-2022/blob/master/img/procesos4.png)