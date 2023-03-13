bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fread, fclose, printf
import exit msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    format db "The number of odd digits is %d", 0
    file_name db "ex4.txt", 0
    access_mode db "r", 0
    
    file_descriptor dd -1
    len equ 100  
    text times len db 0 
    
    

    ;A text file is given. Read the content of the file, count the number of odd digits and display the result on the screen. The name of text file is defined in the data segment.
segment code use32 class=code
    start:
        push dword access_mode     
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor], eax
         
        cmp eax, 0
        je exitprogram
        
        push dword [file_descriptor]
        push dword len
        push dword 1
        push dword text        
        call [fread]
        add esp, 4*4
        
        mov ecx, eax
        jecxz exitprogram
        cld
        mov esi, text
        mov ebx, 0
        
        check_odd:
            lodsb
            sub al, '0'+0
            and al, 00000001b
            cmp al, 1
            jne no_increase
            inc ebx
        
        
        no_increase:
            loop check_odd
            
        push dword ebx
        push dword format
        call [printf]
        add esp, 4 * 2
        exitprogram:
            push dword [file_descriptor]
            call [fclose]
            add esp, 4
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
