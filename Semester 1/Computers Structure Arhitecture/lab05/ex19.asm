bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; Two byte strings A and B are given. Obtain the string R that contains only the even negative elements of the two strings
segment data use32 class=data
    A db 2, 1, 3, -3, -4, 2, -6
    la equ $ - A
    B db 4, 5, -5, 7, -6, -2, 1
    lb equ $ - B
    
    R resb 2


segment code use32 class=code
    start:
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov esi, 0
        mov edi, 0
        
        mov ecx, la
        start_loop_A:
            mov al, [A+esi]
            test al, 1
            rol al, 1
            jz check_carry_A
            check_carry_A:
                jc add_to_R_A
            jmp exit_loop_A
            add_to_R_A:
                ror al, 1
                mov [R + edi], al
                inc edi
            exit_loop_A:
                inc esi
        loop start_loop_A
        
        mov ecx, lb
        mov esi, 0
        start_loop_B:
            mov al, [B+esi]
            test al, 1
            rol al, 1
            jz check_carry_B
            check_carry_B:
                jc add_to_R_B
            jmp exit_loop_B
            add_to_R_B:
                ror al, 1
                mov [R + edi], al
                inc edi
            exit_loop_B:
                inc esi
        loop start_loop_B
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
