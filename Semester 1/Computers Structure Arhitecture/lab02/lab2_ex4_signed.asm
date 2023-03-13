
bits 32 ;assembling for the 32 bits architecture
; the start label will be the entry point in the program
global  start 

extern  exit ; we inform the assembler that the exit symbol is foreign, i.e. it exists even if we won't be defining it

import  exit msvcrt.dll; exit is a function that ends the process, it is defined in msvcrt.dll
        ; msvcrt.dll contains exit, printf and all the other important C-runtime functions
segment  data use32 class=data ; the data segment where the variables are declared 

;(a-c)*3+b*b
	a  db 3h
	b  db 4h
    c  db 1h
    d  db 4h
    e  dw 
    f  dw 
    g  dw 
    h  dw 
segment  code use32 class=code ; code segment
start: 
	mov ax, 0;
    mov al, [b];
    mov ah, [b];
    
    mul al;
    mov cx,ax;
    
    
    mov bx, 0;
    mov bl, [a];
    sub bl, [c];
    mov ax, 3;
    
    mul bl;
    
    add ax,cx;
    
    mov cx,[g];
    
    div cx;
       
	
	push   dword 0 ;saves on stack the parameter of the function exit
	call   [exit] ; function exit is called in order to end the execution of
