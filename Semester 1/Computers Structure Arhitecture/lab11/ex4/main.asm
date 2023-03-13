bits 32

global start        

extern exit, printf
extern convert_base2
extern convert_base16              
import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    s db 3, 7, 13, 35, 64, 78
    len equ ($ - s)
    
    base2 times 8 db '0'
    finish db 0
    
    base16 times 2 db '0'
    finish2 db 0
    
    format_output db "%d -> base 2: %s; base 16: %s", 10, 13, 0

;4. A string of numbers is given. Show the values in base 16 and base 2.
segment code use32 class=code
    start:
        mov ebx, 0
        mov ecx, len
        cmp ecx, 0
        je final
        
        parse_string:
            ; call convert_base2
            mov eax, 0
            mov al, [s + ebx]
            push base2
            push eax
            call convert_base2
            
            ; call convert_base16
            mov eax, 0
            mov al, [s + ebx]
            push base16
            push eax
            call convert_base16
            
            ; print
            mov eax, 0
            mov al, [s + ebx]
            push base16
            push base2
            push eax
            push dword format_output
            call [printf]
            add esp, 2 * 4
            
            
            
            inc ebx
            cmp ebx, len
        jne parse_string
        
        final:
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
