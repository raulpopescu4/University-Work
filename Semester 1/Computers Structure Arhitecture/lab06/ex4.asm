bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; A byte string s is given. Build the byte string d such that every byte d[i] is equal to the count of ones in the corresponding byte s[i] of s
segment data use32 class=data
    s db  5, 25, 55, 127
    l equ $-s
    d resb 1


segment code use32 class=code
    start:
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
           
        mov esi, s
        mov edi, d
        cld
        mov ecx, l
        parsing_loop:
            lodsb
            mov ebx, ecx
            mov ecx, 8
            mov edx, 0
            value_loop:
                shr al, 1
                adc dl, 0 
            loop value_loop
            mov ecx, ebx
            mov al, dl
            stosb
        loop parsing_loop
        
        
    
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
