bits 32

extern exit
import exit msvcrt.dll

segment code use32 class=code
global convert_base2
global convert_base16
    
convert_base2:
    ; convert_base2(number(byte), base2(string))
    mov eax, 0
    mov al, [esp + 4]
    mov edi, [esp + 8]
    add edi, 7
    std
    while1:
        mov cl, 2
        div cl
        mov cl, al
        mov al, ah
        add al, '0'
        stosb
        mov eax, 0
        mov al, cl
        cmp al, 0
    jne while1
    cld
    ret 8
    
convert_base16:
     ;convert_base16(number(byte), base16(string))
    mov eax, 0
    mov al, [esp + 4]
    mov edi, [esp + 8]
    add edi, 1
    std
    while2:
        mov cl, 16
        div cl
        mov cl, al
        mov al, ah
        add al, '0'
        cmp al, '9'
        jbe lower_than_10
        add al, 'A' - '9' - 1
        lower_than_10:
        stosb
        mov eax, 0
        mov al, cl
        cmp al, 0
    jne while2
    cld
    ret 8
    
    ;exit (0)
    push    dword 0      ; push the parameter for exit onto the stack
    call    [exit]       ; call exit to terminate the program