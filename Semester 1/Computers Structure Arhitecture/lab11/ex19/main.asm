bits 32
global start

extern reverse

extern exit, printf, fscanf, fopen, fclose, system
import exit msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll


;19. Read from file numbers.txt a string of numbers. Build a string D wich contains the readen numbers doubled and in reverse order that they were read. Display the string on the screen.
;Ex: s: 12, 3, 5, 7, 8 => 16, 14, 10, 6, 24

segment data use32 class=data
    file_name db "input.txt", 0
    file_descriptor dd 0
    acces_mode db "r", 0
    format_input db "%d", 0
    format_output db "%d ", 0
    len dd 0
    text resd 101 
    number dd 0
    

segment code use32 class=code
start:
    push acces_mode
    push file_name
    call [fopen]
    add esp, 4
    mov [file_descriptor], eax
    cmp eax, 0
    je final
    
    
    read_numbers:
        
        push number
        push format_input
        push dword[file_descriptor]
        call [fscanf]
        add esp, 4*3
        
        cmp eax, 1
        jne reverse_string
        
       
        mov eax, [number]
        add eax, eax 
        
        mov ecx, [len]
        mov [4*ecx+text], eax
        
        inc dword [len]
        
        jmp read_numbers 
        
    reverse_string:
        push dword[len]
        push text
        call reverse
        add esp, 4*2
    
    mov ecx, [len]
    mov ebx, 0
    print:
        push ecx
  
        push dword[text+4*ebx]
        push format_output
        call [printf]
        add esp, 4*2
        
        pop ecx
        inc ebx
        ; dec ecx
        ; cmp ecx, 0
    loop print
    
    final: ; close the file
    push dword[file_descriptor]
    call [fclose]
    add esp, 4

    push dword 0
    call [exit]
