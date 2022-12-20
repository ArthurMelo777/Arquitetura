.include "cenario.asm"

.text
main:	lui $8 0x1001
	lui $24 0x1003
	jal load
	
	addi $2 $0 10
	syscall

load:	lw $9 0($8)
	sw $9 0($24)
	sw $9 0($8)
	addi $8 $8 4
	addi $24 $24 4
	addi $10 $10 1
	bne $10 8192 load
	jr $31