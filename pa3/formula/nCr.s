.globl nCr
        .type   nCr, @function
nCr:
  # Your code for nCr should go here
  pushl %ebp
  movl %esp, %ebp
  subl $12, %esp
  movl 8(%ebp), %eax
  movl %eax, (%esp)
  call Factorial
  movl %eax, -4(%ebp)
  movl 12(%ebp), %eax
  movl %eax, (%esp)
  call Factorial
  movl %eax, -8(%ebp)
  movl 8(%ebp), %eax
  subl 12(%ebp), %eax
  movl %eax, (%esp)
  call Factorial
  imull -8(%ebp), %eax
  movl %eax, %ecx
  movl -4(%ebp), %eax
  movl $0, %edx
  idivl %ecx
  addl $12, %esp
  leave
  ret

.globl Factorial
        .type   Factorial, @function
Factorial:
  # Your code for Factorial should go here
  pushl %ebp
  movl %esp, %ebp
  movl 8(%ebp), %eax
  movl $1, %ebx
.L1:
  cmpl $1, %eax
  jle .L2
  imull %eax, %ebx
  decl %eax
  jmp .L1
.L2:
  movl %ebx, %eax
  popl %ebp
  ret
