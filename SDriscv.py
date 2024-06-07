ejercicio 1:
maximo del arreglo
array = [3, 1, 4, 1, 5, 9, 2, 6]

def max_array(array, length)
    i = 0
    max = 0
    while i < length
        if(max < array[i])
            max = array[i]
        i++
    return max

assembler: 
por que es necesario el mv??

.text:
la a0, array
lw a1, length
jal ra, max_array

li a7, 4 #printea
ecall

li a7, 93 #stopea
ecall


max_array:
    li t0, 0 #iterador de ciclo
    lw t1, 0(a0) #maximo
    
while:
    bge t0, a1, return
    lw t2, 0(a0)
    bge t2, t1, max
    addi a0, a0, 4
    addi t0, t0, 1
    j while
        
max: 
    lw t1, 0(a0)
    addi a0, a0, 4
    addi t0, t0, 1
    j while
        
return:
    mv a0, t1
    ret


ejercicio 2:
dado q y s vectores, copia q en s

def copia_array(q, s, length)
    i = 0
    while(i < length)
        s[i] = q[i]
    return s

assembler: 
.text:
la a0, arrayS
la a1, arrayQ
lw a2, length
jal ra, copia_array

li a7, 4 #printea
ecall

li a7, 93 #stopea
ecall

copia_array:
li t0, 0 #i = 0

while:
bge t0, a2, return
lw t1, 0(a1)
sw t1, 0(a0)
addi t0, t0, 1
addi a1, a1, 4
addi a0, a0, 4
j while
        
return:
    mv a0, t1
    ret

.data: 
arrayS: .word 0x00000003 0x00000001 0x00000004 0x00000001 
arrayQ: .word 0x00000005 0x00000003 0x00000001 0x00000001 
length: .word 0x00000004