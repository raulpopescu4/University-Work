bits 32 


global start        


extern exit               
import exit msvcrt.dll    
                          

;4. Given the byte A, obtain the integer number n represented on the bits 2-4 of A. Then obtain the byte B by rotating A n positions to the right. Compute the doubleword C as follows:
; the bits 8-15 of C have the value 0
; the bits 16-23 of C are the same as the bits of B
; the bits 24-31 of C are the same as the bits of A
; the bits 0-7 of C have the value 1

segment data use32 class=data
         A db 10001100b
         B db 0b
         C dd 0b
         n db 0b


segment code use32 class=code
    start:
    
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov al, [A]
        and al, 00011100b
        mov cl, 2                   ; n <- bits 2-4 of A
        shr al, cl
        mov [n], al
        
        mov cl, [n]
        mov al, [A]                 ; obtained B = 
        ror al, cl
        mov [B], al
        
        mov eax, 0
        mov eax, [B]                     ;   the bits 16-23 of C are the same as the bits of B
        mov cl, 16
        rol eax, cl
        mov ebx, eax 
        
        mov eax, 0
        mov eax, [A]
        mov cl, 24                  ; the bits 24-31 of C are the same as the bits of A
        rol eax,cl
        or ebx, eax 
        
        
        or bl, 11111111b        ; the bits 0-7 of C have the value 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        push    dword 0      
        call    [exit]       
