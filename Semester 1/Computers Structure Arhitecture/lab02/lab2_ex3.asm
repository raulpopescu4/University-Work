
bits 32 ;assembling for the 32 bits architecture
; the start label will be the entry point in the program
global  start 

extern  exit ; we inform the assembler that the exit symbol is foreign, i.e. it exists even if we won't be defining it

import  exit msvcrt.dll; exit is a function that ends the process, it is defined in msvcrt.dll
        ; msvcrt.dll contains exit, printf and all the other important C-runtime functions
segment  data use32 class=data ; the data segment where the variables are declared 
	a  db 1h
	b  db 4h
    c  db 4h
    d  dw 4h
    
segment  code use32 class=code ; code segment
start: 
	mov ax, 0;
    mov al, [a];
    mov ah, [a];
    
    mul al;
    mov cl,al;
    
    
    mov bx, 0;
    mov bl, [b];
    sub bl, 1;
    mov al, 2;
    
    mul bl;
    
    sub al,cl;
    sub al,[d];
       
	
	push   dword 0 ;saves on stack the parameter of the function exit
	call   [exit] ; function exit is called in order to end the execution of
