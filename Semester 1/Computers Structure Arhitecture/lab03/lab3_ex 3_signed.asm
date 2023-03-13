bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw -10
    b db 5
    c db 4
    d db -3
    e dd 2
    x dq 5000
    

; our code starts here

;(a*2+b/2+e)/(c-d)+x/a; a-word; b,c,d-byte; e-doubleword; x-qword
segment code use32 class=code
    start:
        
        mov eax, 0
        mov ecx, 0
        mov ebx, 0
        mov edx, 0
        
        mov ax, 2
        mov cx, [a]
        imul cx        ; ecx <- a*2
        push dx
        push ax
        pop ecx
        
        add ecx, [e]
        mov eax, 0
        mov bl, 2             ; ecx <- (a*2+b/2+e)
        mov al, [b]
        div bl
        add cl, al
       
        mov ebx, 0
        mov edx, 0
        mov eax, ecx           ; ecx <- (a*2+b/2+e)/(c-d)
        mov bl, [c]
        sub bl, [d]
        div ebx
        mov ecx, eax
        
        
        
        mov eax, 0
        mov edx, 0
        mov ebx, 0
        mov eax, [x+0]
        mov ebx, [x+4]
        push ecx
        mov ecx, 0
        mov cx, [a]
        div ecx 
        pop ebx
        add ebx,eax        
                                  ; ebx <- (a*2+b/2+e)/(c-d)+x/a
        
        
        
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
