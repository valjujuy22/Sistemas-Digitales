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


Ejercicio 3:
copiar q en s, solo si el elem de q es par
def copia_par_array(q, s, length)
    i = 0
    while(i < length)
        if(q[i] % 2 == 0){
            s[i] = q[i]
        }
    return s

assembler:
.text:
la a0, arrayS
la a1, arrayQ
lw a2, length
jal ra, copia_par_array

li a7, 4 #printea
ecall

li a7, 93 #stopea
ecall


copia_par_array:
li t0, 0 #i = 0


while:
bge t0, a2, return
lw t1, 0(a1)

            
andi t2, t1, 1 #hago mascara a t1 (q[i]) para saber si es par
                
beq t2, x0, reemplazo # si es par lo pongo en s  
addi t0, t0, 1
addi a1, a1, 4
addi a0, a0, 4
j while

reemplazo: 
sw t1, 0(a0)
addi t0, t0, 1
addi a1, a1, 4
addi a0, a0, 4
j while
    
return:
    mv a0, t1
    ret

.data: 
arrayS: .word 0x00000003 0x00000001 0x00000004 0x00000005 
arrayQ: .word 0x00000004 0x00000002 0x00000001 0x00000001 
length: .word 0x00000004

ejercicio 4:

def binary_search (array, elem, length)
    int arriba = length - 1
    int abajo = 0
    int medio 
    while(abajo <= arriba)
        medio = abajo + (arriba - abajo)/2 # si lo hciera mal como fausto, se me podria ir de rango (32 bts)

        if(array[medio] = elem)
            return medio

        if(array[medio] < elem)
            abajo = medio + 1
        else 
            arriba = medio - 1
    return medio

assembler:

.text:
la a0, array
lw a1, target
jal ra, binary_search

li a7, 4 #printea
ecall

li a7, 93 #stopea
ecall

binary_search:
li t0, 0 #abajo
lw t1, length 
addi t1, t1, -1 #arriba = length - 1

while:
mv t2, t0 #t2 = abajo
mv t5, t1 # t5 = arriba
sub t6, t5, t0 #t5 = arriba - abajo
srli t5, t6, 1 #t5 = (arriba - abajo)/2  toma floor
add t2, t0, t5 #medio(t2) = abajo + (arriba - abajo)/2 
                

slli t3, t2, 2 # t3 = medio*4
add a0, a0, t3 # a0 = a0 + t3

lw t4, 0(a0)  # t4 = array[medio]
beq t4, a1, return  # t4 = a1 -> return

blt t4, a1, caso  # t4 < a1 -> medio_es_abajo
 
sub a0, a0, t3 # a0 = a0 - t3
addi t1, t2, -1 # arriba = medio - 1
j while

caso:
sub a0, a0, t3 # a0 = a0 - t3
addi t0, t2, 1 #abajo = medio + 1
j while
    
return:
    mv a0, t2 #devuelvo medio (t2)
    ret

.data: 
array: .word 1 3 5 7 9 11 13 15 17 19
target: .word 15
length: .word 10


ejercicio 5:

def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

assembler:
.text:
lw a0, numero
jal ra, fibonacci

li a7, 4 #printea
ecall

li a7, 93 #stopea
ecall

fibonacci:
addi sp, sp, -12

sw 
sw ra , 0(sp)

addi t0 , zero , 1
beq t0, a0, then1
beq x0, a0, then2
#else
addi a0, a0, -1
sw ra, 4(sp)
jal fibonacci
addi a0, a0, -1
jal fibonacci


jr ra


then1:
jr ra
    
then2:
jr ra

return:
    mv a0, t2 
    ret

.data: 
numero: .word 5






