bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
   
; Two byte strings S1 and S2 are given, having the same length. Obtain the string D in the following way: each element found on the even positions of D is the sum of the corresponding elements from S1 and S2, and each element found on the odd positions of D is the difference of the corresponding elements from S1 and S2.
segment data use32 class=data
    s1 db 5, 3, 2, 8, 4
    s2 db 4, 2, 7, 9, 2
    l equ $-s2
    d resb 1


segment code use32 class=code
    start:
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov ecx, l 
        mov esi, 0

        start_loop:
            mov al, 0
            mov bl, 0
            mov al, [s1 + esi]
            mov bl, [s2 + esi]
            test esi, 1
            
            jnz if_odd_number
            jz if_even_number
            
            if_odd_number:
                sub al,bl
                mov [d+esi], al
                jmp end_if
            
            if_even_number:
                add al,bl
                mov [d+esi], al
                jmp end_if
            
            
            end_if:
                inc esi
        loop start_loop
        
            
            
    
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
