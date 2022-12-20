.data
	dp: .word 67 70 72 67 70 73 72 67 70 72 70 67
.text
	main:
	addi $5 $0 2000 # 1 segundo
	addi $6 $0 28 #24 - 31 guitarra
	addi $7 $0 65 # volume
	addi $24 $0 0
	addi $25 $0 48
	
	for:
	beq $24 $25 reset
	lw $4 dp($24)
	beq $4 73 meioTempo
	beq $4 72 doisTempos
	addi $2 $0 31
	syscall
	addi $20 $0 200000 # 1
	jal fortimer
	addi $24 $24 4
	j for
	
	reset:
	addi $24 $0 0
	addi $25 $0 48
	addi $20 $0 350000
	jal fortimer
	
	for2:
	beq $24 $25 fim
	lw $4 dp($24)
	beq $4 73 meioTempo
	beq $4 72 doisTempos
	addi $2 $0 31
	syscall
	addi $20 $0 200000 # 1
	jal fortimer
	addi $24 $24 4
	j for2
	
	meioTempo:
	addi $5 $0 1000
	addi $20 $0 100000 # 1/2
	addi $2 $0 31
	syscall
	jal fortimer
	addi $24 $24 4
	j for
	
	doisTempos:
	addi $5 $0 4000
	addi $20 $0 350000 # 2
	addi $2 $0 31
	syscall
	jal fortimer
	addi $24 $24 4
	j for
	
	fortimer:
	beq $20 $0 fimtimer
	nop
	nop
	nop
	addi $20 $20 -1
	j fortimer
	fimtimer:
	jr $31
	
	fim:
	addi $2 $0 10
	syscall
