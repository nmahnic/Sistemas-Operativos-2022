# Sistemas Operativos

## ¿Que hace un sistema operativo?
- CPU, memoria, dispositivos de Entrada Salida... Sin software, son meros circuitos electrónicos.
- Firefox, Visual Studio Code, Slack, Telegram, VLC, spotify... Aplicaciones muy ́utiles. Pero si todas juntas quieren acceder al hardware... caos.
- Deberían ponerse de acuerdo entre las diferentes aplicaciones en todo momento para acceder a ́areas de memoria sin interferirse una a otras, para configurar el hardware con determinadas propiedades y utilizarlo en forma serializada también.
¿Hace falta mas para darse cuenta que se necesita una capa tipo “man in the middle” que intermedie entre el hardware y las aplicaciones?

![Arquitectura de un sistema de extremo a extremo](https://github.com/nmahnic/Sistemas-Operativos-2022/blob/master/apuntes/img/sistop1.png)

## Primera Conclusión
No importan tanto las características del hardware. Si lo que vamos a desarrollar está organizado en forma de diferentes tareas que ejecutan en forma concurrente, necesitamos una pieza de softwareque administre la forma en que los recursos de hardware se van a asignar a cada tarea (o proceso). De otra manera no existe protección entre tareas, y no se puede proveer sincronización entre los diferentes procesos para accedera un mismo recurso, por citar solo las problemáticas mas evidentes.


## Componentes de un Sistema Operativo
- Un sistema Operativo es básicamente un administrador de recursos.
- Los principales recursos del sistema son la CPU, la Memoria, los dispositivos de entrada salida, y en caso de que haya algún sistema de storage, ́este se convierte también en un recurso a administrar.
- Los usuarios de esos recursos son los procesos o tareas. Dicho de manera muy rudimentaria, los programas que se encuentran ejecutando en la memoria del sistema.

![Diagrama General de un Sistema Operativo](https://github.com/nmahnic/Sistemas-Operativos-2022/blob/master/apuntes/img/sistop2.png)


## Scheduling de Procesos
- Hemos dicho que los procesos son los principales usuarios de los recursos del computador, administrados bajo el Sistema Operativo.
- Un proceso necesita como para iniciar su ejecución dos elementos sin los cuales no le es posible operar: CPU, y Memoria.
- En un sistema multitasking hay una cantidad de procesos en condiciones de ser ejecutados. Esta cantidad normalmente es mayor que la cantidad de CPUs que tiene el sistema.
- El scheduler es el módulo del sistema operativo encargado de administrar la ejecución de los procesos, es decir, es quien les asigna uno de los recursos fundamentales: la CPU.
El Scheduler determina cuando y sobre cual de las CPUs ejecutará en cada uno de los procesos a fin de lograr el mejor rendimiento posibledel sistema.

### Sincronización de Procesos - singleCore
- Cuando un proceso debe esperar la ocurrencia de un evento,o la disponibilidad de un recurso actualmente no disponible se pone a dormir para suspender su ejecución y liberar la CPU. Esta podrá eventualmente ser asignada a otro proceso.
- Cuando el recurso se pone disponible el proceso en poder dela CPU la cede al proceso que espera el recurso. 
- Si esperaba un evento, la CPU le es devuelta al proceso dormido desde el handler de la interrupción que maneja el evento.


## Sistemas Operativos de Propósito general
Un GPOS (General Purpose Operating System), es un sistema operativo que implementa gestión de procesos, gestión de memomria, gestión de la Entrada/Salida, soporte a File System(s) como parte de la gestión de sistemas de storage, y posee una interfaz de usuario que le permite interactuar a demanda con el computador. Además cada proceso ejecuta en un espacio propio protegido del resto, por medio del hardware de manejo de memoria. Los procesos ejecutan y finalizan en forma dinámica la cantidad de veces que el usuario defina o cada vez que los ejecute a demanda. Solicitan recursos y cuando finalizan liberan todos los recursos quepueden ser reasignados a otro proceso.


## UNIX
- Escrito 99 % en un lenguaje específicamente diseñado para escribir Sistemas Operativos en reemplazo del assembler: C.
- Portable entre diferentes plataformas de hardware debido a la portabilidad nativa del C.
- Su Arquitectura base de extrema simplicidad, lo hace poderoso, versátil e ideal para programadores.
- Provee primitivas muy potentes que permiten construir programas complejos a partir de código relativamente simple.
- Introduce el concepto de stream de bytes que permite tratar entidades de diferente origen y características bajo una simple interfaz común. Se conoce como el paradigma “everything is afile”.
- Provee una visión de máquina transparente a los detalles de hardware.
- Provee un entorno de programación y ejecución multitarea y multiusuario, de bajo costo computacional y alta estabilidad y seguridad.
- La potencia de cada programa no se debe al programa en sí mismo, sino a su relación con el resto de los programas alojados en el file system
- Junto con las herramientas de programación y utilitarios que trae junto con el sistema, y al agregarse como protocolo de conectividad standard la suite TCP/IP, un System V o BSD 4.3 forman un ecosistema de desarrollo de muy alta productividadcuando se lo sabe utilizar.

### Every is a File
Una de las innovaciones que introdujo UNIX es que muchos dispositivos de E/S, se tratan como byte streams. Esto hace que un pequeño conjunto de operaciones sobre archivos tanto del API como del shell se utilicen para manipular E/S. Todo lo que se necesita es la descripción del dispositivo como un nodo del File System. 
En general encontramos en el directorio /dev todos los nodos que describen devices. Su implementación corre por cuenta del device driver correspondiente.

De este modo accedemos a un device de E/S como si fuese unarchivo
- OPEN: Obtenemos un file descriptor que será utilizado en delante para referenciarlo
- READ: Leemos en un buffer el byte stream que provee el device (a la velocidad del mismo)
- WRITE: Enviamos información presente en un buffer al device
- IOCTL: Accedemos a su configuración (depende de cada device)
- CLOSE: Una vez que terminamos de trabajar con ́el, devolve-mos el file descriptor y liberamos el recurso


## LINUX
- En 1991, un estudiante de la Universidad de Helsinki llamado Linus Torvalds, estaba ́avido por encontrar una versión de UNIX robusta y con fuentes disponibles e hizo lo que cualquier estudiante de computación inquieto y con vocación: comenzó a escribir su propio Sistema Operativo. Lo publicó a fines de 1991 bajo la GNU GeneralPublic Licence (GPL).
- Rápidamente se sumó un gran número de hackers y desarrolladores que comenzaron a mejorar corregir y aumentar su código y actualmente es un sistema operativo robusto, de interés comercial (Muchos fabricantes de Hardware ofrece soluciones basadas en LINUX), desarrollado por un equipo de desarrolladores a través de Internet.


### LINUX hoy
- Sistema Operativo Unix-like, con soporte a POSIX.
- Kernel monolítico: Imagen ́unica de código.
- Diseñado bajo el concepto Lightweight Processes (LWP)
- Preemptive Kernel
- Soporta SMP (Symmetric Multi Processing)
- Soporta un amplia diversidad de File Systems (IBM AIX, SGI Irix,FAT32, NTFS,etc.)
- Las herramientas de construcción del kernel, permiten customizar imágenes a la medida del hardware de base y con los componentes mínimos necesarios de modo de obtener sistemas muy compactos.

## Kernel
Es el Sistema Operativo propiamente dicho. Típicamente se encarga de: 
- Manejar las interrupciones de hardware, 
- Asignar el tiempo de CPU a cada uno de los procesos que estén enejecución en un instante dado, 
- Gestionar la memoria para manejar los diferentes espacios de direcciones de los procesos, 
- Gestionar servicios de sistema, como networking, Intercomunicación de procesos, etc.
Trabaja en un estado de elevado nivel comparado con las aplicaciones gracias a las funciones de protección de memoria y recursos que poseen los procesadores modernos.Tiene un ́area propia de memoria y acceso completo al hardware. A este estado de sistema y su espacio de memoria se lo suele referir como "kernel space". Y por otra parte al espacio de memoria y estado de las aplicaciones se lo refiere como "user space".

![El kernel](https://github.com/nmahnic/Sistemas-Operativos-2022/blob/master/apuntes/img/sistop3.png)