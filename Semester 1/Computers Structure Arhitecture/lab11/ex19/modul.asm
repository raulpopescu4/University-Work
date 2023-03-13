bits 32

global reverse

segment code use32 class=code
reverse:
    ; reverse(text, len)
    ; return adress -> [esp]
    ; text -> [esp+4]
    ; len -> [esp+8]
    
    
    mov ebx, [esp+4]
    mov esi, 0
    mov edi, [esp+8]
    dec edi
    
    reverse_loop:
        mov eax, [ebx+4*esi]
        mov edx, [ebx+4*edi]
        mov [ebx+4*esi], edx
        mov [ebx+4*edi], eax
        inc esi
        dec edi
        mov eax, edi
        sub eax, esi
        cmp eax, 0
    jg reverse_loop
    ret

    ;exit (0)
    push    dword 0      ; push the parameter for exit onto the stack
    call    [exit]       ; call exit to terminate the program
    