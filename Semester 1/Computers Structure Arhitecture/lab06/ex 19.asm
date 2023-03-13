bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
    
    ; Being given two strings of bytes, compute all positions where the second string appears as a substring in the first string.
segment data use32 class=data
    s db 1, 5, 2, 9, 11, 5, 7, 5, 2, 9, 9, 4, 6
    ls equ $-s
    
    subs db 5, 2, 9
    lsubs equ $-subs
    
    poss resb 2


segment code use32 class=code
    start:
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov esi, s
        mov ecx, ls
        mov edx, poss
        
        sub ecx, lsubs
        cmp ecx, 0
        jl exit_program
        
        loop_program:
            mov edi, subs
            mov ebx, esi
            
            push ecx
            mov ecx, lsubs
            cld
            
            repe cmpsb
            jz substring_found
            jmp substring_not_found
            
            substring_found:
                mov ecx, lsubs
                mov edi, edx
                again:
                    stosb
                    inc al 
                loop again   
                sub al, lsubs
                mov edx, edi
            substring_not_found:
                mov esi, ebx
                inc esi
                pop ecx
                dec ecx
                inc al
                cmp ecx,0
                jnl loop_program
        exit_program:
            push    dword 0      ; push the parameter for exit onto the stack
            call    [exit]       ; call exit to terminate the program
