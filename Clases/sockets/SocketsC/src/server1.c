// Ficheros de cabecera
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>

#include <fcntl.h> // for open
#include <unistd.h> // for close
 
//FunciÃ³n principal
int main(int argc, char **argv){
 
    if(argc > 1){
    
        //Primer paso, definir variables
        int fd,fd2,longitud_cliente,puerto;
        puerto=atoi(argv[1]);
    
        //Se necesitan dos estructuras del tipo sockaddr
        //La primera guarda info del server
        //La segunda del cliente
        struct sockaddr_in server;
        struct sockaddr_in client;
        
        //Configuracion del servidor
        server.sin_family= AF_INET; //Familia TCP/IP
        server.sin_port = htons(puerto); //Puerto
        server.sin_addr.s_addr = INADDR_ANY; //Cualquier cliente puede conectarse
        bzero(&(server.sin_zero),8); //Funcion que rellena con 0's
    
        //Paso 2, definicion de socket
        if (( fd=socket(AF_INET,SOCK_STREAM,0) ) <0 ){
            perror("Error de apertura de socket");
            exit(-1);
        }
    
        //Paso 3, avisar al sistema que se creo un socket
        if( bind(fd,(struct sockaddr*)&server, sizeof(struct sockaddr) )==-1) {
            printf("error en bind() \n");
            exit(-1);
        }
    
        //Paso 4, establecer el socket en modo escucha
        if( listen(fd,5) == -1 ) {
            printf("error en listen()\n");
            exit(-1);
        }
    
        //Paso5, aceptar conexiones
        // while(1) {
            longitud_cliente = sizeof(struct sockaddr_in);
            /* A continuaciÃ³n la llamada a accept() */
            if ((fd2 = accept( fd,(struct sockaddr *)&client,(socklen_t *)&longitud_cliente ) ) == -1) {
                printf("error en accept()\n");
                exit(-1);
            }

            fork()
            
            send(fd2,"Bienvenido a mi servidor MASH.\n",31,0);
            
            close(fd2); /* cierra fd2 */
        // }
        close(fd);
    } else {
        printf("NO se ingreso el puerto por parametro\n");
    }
    return 0;
}