	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 13
	.globl	_main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	pushq	%rbp
Lcfi0:
	.cfi_def_cfa_offset 16
Lcfi1:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Lcfi2:
	.cfi_def_cfa_register %rbp
	subq	$80, %rsp
	movl	$0, -4(%rbp)
	movq	$1, -16(%rbp)
	movq	$0, -72(%rbp)
	movq	$0, -64(%rbp)
	movq	$0, -56(%rbp)
	movq	$0, -48(%rbp)
	movq	$0, -40(%rbp)
	movq	$0, -32(%rbp)
	movq	$0, -24(%rbp)
## BB#1:
	movq	$67, -24(%rbp)
## BB#2:
	movq	-24(%rbp), %rax
	movq	%rax, -32(%rbp)
## BB#3:
	cmpq	$0, -16(%rbp)
	je	LBB0_5
## BB#4:
	jmp	LBB0_7
LBB0_5:
	jmp	LBB0_6
LBB0_6:
	jmp	LBB0_11
LBB0_7:
	imulq	$100, -24(%rbp), %rax
	movq	%rax, -24(%rbp)
## BB#8:
	movq	-24(%rbp), %rax
	addq	$100000, %rax           ## imm = 0x186A0
	movq	%rax, -24(%rbp)
## BB#9:
	movq	-24(%rbp), %rax
	movq	%rax, -32(%rbp)
## BB#10:
	movq	-32(%rbp), %rax
	addq	$17000, %rax            ## imm = 0x4268
	movq	%rax, -32(%rbp)
LBB0_11:                                ## =>This Loop Header: Depth=1
                                        ##     Child Loop BB0_13 Depth 2
                                        ##       Child Loop BB0_14 Depth 3
	movq	$1, -56(%rbp)
## BB#12:                               ##   in Loop: Header=BB0_11 Depth=1
	movq	$2, -40(%rbp)
LBB0_13:                                ##   Parent Loop BB0_11 Depth=1
                                        ## =>  This Loop Header: Depth=2
                                        ##       Child Loop BB0_14 Depth 3
	movq	$2, -48(%rbp)
LBB0_14:                                ##   Parent Loop BB0_11 Depth=1
                                        ##     Parent Loop BB0_13 Depth=2
                                        ## =>    This Inner Loop Header: Depth=3
	movq	-40(%rbp), %rax
	movq	%rax, -64(%rbp)
## BB#15:                               ##   in Loop: Header=BB0_14 Depth=3
	movq	-48(%rbp), %rax
	imulq	-64(%rbp), %rax
	movq	%rax, -64(%rbp)
## BB#16:                               ##   in Loop: Header=BB0_14 Depth=3
	movq	-24(%rbp), %rax
	movq	-64(%rbp), %rcx
	subq	%rax, %rcx
	movq	%rcx, -64(%rbp)
## BB#17:                               ##   in Loop: Header=BB0_14 Depth=3
	cmpq	$0, -64(%rbp)
	je	LBB0_19
## BB#18:                               ##   in Loop: Header=BB0_14 Depth=3
	jmp	LBB0_21
LBB0_19:                                ##   in Loop: Header=BB0_14 Depth=3
	jmp	LBB0_20
LBB0_20:                                ##   in Loop: Header=BB0_14 Depth=3
	movq	$0, -56(%rbp)
LBB0_21:                                ##   in Loop: Header=BB0_14 Depth=3
	movq	-48(%rbp), %rax
	addq	$1, %rax
	movq	%rax, -48(%rbp)
## BB#22:                               ##   in Loop: Header=BB0_14 Depth=3
	movq	-48(%rbp), %rax
	movq	%rax, -64(%rbp)
## BB#23:                               ##   in Loop: Header=BB0_14 Depth=3
	movq	-24(%rbp), %rax
	movq	-64(%rbp), %rcx
	subq	%rax, %rcx
	movq	%rcx, -64(%rbp)
## BB#24:                               ##   in Loop: Header=BB0_14 Depth=3
	cmpq	$0, -64(%rbp)
	je	LBB0_26
## BB#25:                               ##   in Loop: Header=BB0_14 Depth=3
	jmp	LBB0_14
LBB0_26:                                ##   in Loop: Header=BB0_13 Depth=2
	jmp	LBB0_27
LBB0_27:                                ##   in Loop: Header=BB0_13 Depth=2
	movq	-40(%rbp), %rax
	addq	$1, %rax
	movq	%rax, -40(%rbp)
## BB#28:                               ##   in Loop: Header=BB0_13 Depth=2
	movq	-40(%rbp), %rax
	movq	%rax, -64(%rbp)
## BB#29:                               ##   in Loop: Header=BB0_13 Depth=2
	movq	-24(%rbp), %rax
	movq	-64(%rbp), %rcx
	subq	%rax, %rcx
	movq	%rcx, -64(%rbp)
## BB#30:                               ##   in Loop: Header=BB0_13 Depth=2
	cmpq	$0, -64(%rbp)
	je	LBB0_32
## BB#31:                               ##   in Loop: Header=BB0_13 Depth=2
	jmp	LBB0_13
LBB0_32:                                ##   in Loop: Header=BB0_11 Depth=1
	jmp	LBB0_33
LBB0_33:                                ##   in Loop: Header=BB0_11 Depth=1
	cmpq	$0, -56(%rbp)
	je	LBB0_35
## BB#34:                               ##   in Loop: Header=BB0_11 Depth=1
	jmp	LBB0_37
LBB0_35:                                ##   in Loop: Header=BB0_11 Depth=1
	jmp	LBB0_36
LBB0_36:                                ##   in Loop: Header=BB0_11 Depth=1
	movq	-72(%rbp), %rax
	addq	$1, %rax
	movq	%rax, -72(%rbp)
LBB0_37:                                ##   in Loop: Header=BB0_11 Depth=1
	movq	-24(%rbp), %rax
	movq	%rax, -64(%rbp)
## BB#38:                               ##   in Loop: Header=BB0_11 Depth=1
	movq	-32(%rbp), %rax
	movq	-64(%rbp), %rcx
	subq	%rax, %rcx
	movq	%rcx, -64(%rbp)
## BB#39:                               ##   in Loop: Header=BB0_11 Depth=1
	cmpq	$0, -64(%rbp)
	je	LBB0_41
## BB#40:                               ##   in Loop: Header=BB0_11 Depth=1
	jmp	LBB0_43
LBB0_41:
	jmp	LBB0_42
LBB0_42:
	jmp	LBB0_45
LBB0_43:                                ##   in Loop: Header=BB0_11 Depth=1
	movq	-24(%rbp), %rax
	addq	$17, %rax
	movq	%rax, -24(%rbp)
## BB#44:                               ##   in Loop: Header=BB0_11 Depth=1
	jmp	LBB0_11
LBB0_45:
	leaq	L_.str(%rip), %rdi
	movq	-72(%rbp), %rsi
	movb	$0, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -76(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	addq	$80, %rsp
	popq	%rbp
	retq
	.cfi_endproc

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"h=%ld\n"


.subsections_via_symbols
