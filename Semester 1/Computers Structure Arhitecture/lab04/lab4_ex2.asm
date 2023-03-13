bits 32 ; assembling for the 32 bits architecture


global start        


extern exit              
import exit msvcrt.dll   
                          

; 18. Given the word A, compute the doubleword B as follows:
; the bits 0-3 of B have the value 0;
; the bits 4-7 of B are the same as the bits 8-11 of A
; the bits 8-9 and 10-11 of B are the invert of the bits 0-1 of A (so 2 times) ;
; the bits 12-15 of B have the value 1
; the bits 16-31 of B are the same as the bits 0-15 of B.
segment data use32 class=data
    A dw 0001110011000100b
    B dd 0b


segment code use32 class=code
    start:
    
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov ax, [A]
        mov cl, 4                                ; 4-7 11110000 of bl                ; the bits 0-3 of B have the value 0
        ror ax, cl                               ; 8-11 of ax 0000111100000000       ; the bits 4-7 of B are the same as the bits 8-11 of A
        and ax, 0000000011110000b
        mov bl, al
        
        mov eax, 0
        mov ax, [A]
        and ax, 0000000000000011b                    ; 0-1 of A inverted 11           ; the bits 8-9 and 10-11 of B are the invert of the bits 0-1 of A (so 2 times)
        mov cl, 2                                    ; 8-11 of bx 
        shl ax, cl
        mov cx, [A]
        and cx, 0000000000000011b
        or ax, cx
        not ax
        and ax, 0000000000001111b
        mov cl, 8
        shl ax, cl
        or bx, ax 
        
        mov eax, 0
        mov ecx, 0
        or ax, 1111b                            ; the bits 12-15 of B have the value 1
        mov cl, 12
        shl ax, cl
        or bx, ax
        
        mov eax, 0
        mov ecx, 0
        or ax, bx                             ; the bits 16-31 of B are the same as the bits 0-15 of B.
        mov cl, 16
        shl eax, cl
        or ebx, eax 
        
        
        
        
    
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
