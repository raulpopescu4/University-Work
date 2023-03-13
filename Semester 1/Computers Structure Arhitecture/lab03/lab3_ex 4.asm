bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 2
    b db 10
    c dw 4400
    e dd 562342
    x dq 41523532354
    

; (a+b*c+2/c)/(2+a)+e+x; a,b-byte; c-word; e-doubleword; x-qword
segment code use32 class=code
    start:
    
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov ax, [c]
        mov bl, [b]
        mul bx                ; ecx <- b*c 
        push dx
        push ax
        pop ecx
        
        mov eax, 0
        mov ebx, 0
        mov edx, 0
        mov al, 2                  ; ecx <- (a+b*c+2/c)
        mov bx, [c] 
        div bx
        add ecx, eax 
        mov ebx, 0
        mov bl, [a]
        add ecx, ebx
        
        mov eax, 0
        mov ebx, 0
        mov edx, 0
        mov ebx, [e]
        add ecx, ebx
        mov eax, [x+0]
        mov edx, [x+4]
        add eax, ecx
        adc edx, 0
        
        
        
        
