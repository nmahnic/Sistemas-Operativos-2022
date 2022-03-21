
SECTION .data
    hello: db "Hello world!", 10 ; 10 is \n
    helloLen: equ $-hello

SECTION .text
    global _start

; from man 2 syscall, arguments to syscalls are passed in
; x86-64 rdi rsi rdx r10 r8 r9
; syscall numbers are obtained from https://filippo.io/linux-sy...

_start:
    mov rax, 1          ; 'write' system call = 4
    mov rdi, 1          ; file descriptor 1 = STDOUT
    mov rsi, hello      ; string to write
    mov rdx, helloLen   ; length of string to write
    syscall             ; call the kernel

    ; Terminate program
    mov rax, 60         ; 'exit' system call
    mov rdi, 0          ; exit with error code 0
    syscall             ; call the kernel

