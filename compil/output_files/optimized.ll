; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"int_pow"(i32 %".1", i32 %".2")
{
entry:
  %"result" = alloca i32
  store i32 1, i32* %"result"
  %".5" = icmp eq i32 %".2", 0
  br i1 %".5", label %"entry.if", label %"entry.endif"
entry.if:
  ret i32 1
entry.endif:
  %"exponent_ptr" = alloca i32
  store i32 %".2", i32* %"exponent_ptr"
  br label %"loop"
loop:
  %"current_result" = load i32, i32* %"result"
  %"mul" = mul i32 %"current_result", %".1"
  store i32 %"mul", i32* %"result"
  %"current_exponent" = load i32, i32* %"exponent_ptr"
  %"decremented_exponent" = sub i32 %"current_exponent", 1
  store i32 %"decremented_exponent", i32* %"exponent_ptr"
  %".12" = icmp sgt i32 %"decremented_exponent", 0
  br i1 %".12", label %"loop", label %"exit"
exit:
  %".14" = load i32, i32* %"result"
  ret i32 %".14"
}

define double @"double_pow"(double %".1", i32 %".2")
{
entry:
  %".4" = icmp eq i32 %".2", 0
  br i1 %".4", label %"entry.if", label %"entry.endif"
entry.if:
  ret double 0x3ff0000000000000
entry.endif:
  %"result" = alloca double
  store double 0x3ff0000000000000, double* %"result"
  %"base" = alloca double
  store double %".1", double* %"base"
  %"exponent_ptr" = alloca i32
  store i32 %".2", i32* %"exponent_ptr"
  br label %"loop"
loop:
  %"current_result" = load double, double* %"result"
  %"current_base" = load double, double* %"base"
  %"mul" = fmul double %"current_result", %"current_base"
  store double %"mul", double* %"result"
  %"current_exponent" = load i32, i32* %"exponent_ptr"
  %"decremented_exponent" = sub i32 %"current_exponent", 1
  store i32 %"decremented_exponent", i32* %"exponent_ptr"
  %".13" = icmp sgt i32 %"decremented_exponent", 0
  br i1 %".13", label %"loop", label %"exit"
exit:
  %".15" = load double, double* %"result"
  ret double %".15"
}

define void @"main"()
{
entry.main:
  %".2" = call i32 @"sqrt"(i32 25, i32 1)
  %"result" = alloca i32
  store i32 %".2", i32* %"result"
  %".4" = load i32, i32* %"result"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"abs"(i32 %".1")
{
entry:
  %"result" = sub i32 0, %".1"
  %".3" = icmp slt i32 %".1", 0
  %".4" = select  i1 %".3", i32 %"result", i32 %".1"
  ret i32 %".4"
}

define double @"absf"(double %".1")
{
entry:
  %"result" = fsub double              0x0, %".1"
  %".3" = fcmp ult double %".1",              0x0
  %".4" = select  i1 %".3", double %"result", double %".1"
  ret double %".4"
}

define i32 @"sqrt"(i32 %".1", i32 %".2")
{
entry:
  %"number_tmp" = alloca i32
  store i32 %".1", i32* %"number_tmp"
  %"guess_tmp" = alloca i32
  store i32 %".2", i32* %"guess_tmp"
  %"tolerance" = alloca double
  store double 0x3f1a36e2eb1c432d, double* %"tolerance"
  %".7" = load i32, i32* %"guess_tmp"
  %".8" = call i32 @"int_pow"(i32 %".7", i32 2)
  %"nguess" = alloca i32
  store i32 %".8", i32* %"nguess"
  %".10" = load i32, i32* %"nguess"
  %".11" = load i32, i32* %"number_tmp"
  %".12" = sub i32 %".10", %".11"
  store i32 %".12", i32* %"nguess"
  %".14" = load i32, i32* %"nguess"
  %".15" = call i32 @"abs"(i32 %".14")
  store i32 %".15", i32* %"nguess"
  %".17" = load i32, i32* %"nguess"
  %".18" = load double, double* %"tolerance"
  %".19" = sitofp i32 %".17" to double
  %".20" = fcmp olt double %".19", %".18"
  br i1 %".20", label %"if.then", label %"if.else"
if.then:
  %".22" = load i32, i32* %"guess_tmp"
  ret i32 %".22"
if.else:
  %".24" = load i32, i32* %"number_tmp"
  %".25" = load i32, i32* %"guess_tmp"
  %".26" = udiv i32 %".24", %".25"
  %"newGuess" = alloca i32
  store i32 %".26", i32* %"newGuess"
  %".28" = load i32, i32* %"newGuess"
  %".29" = load i32, i32* %"guess_tmp"
  %".30" = add i32 %".28", %".29"
  store i32 %".30", i32* %"newGuess"
  %".32" = load i32, i32* %"newGuess"
  %".33" = udiv i32 %".32", 2
  store i32 %".33", i32* %"newGuess"
  %"n" = alloca i32
  %".35" = load i32, i32* %"number_tmp"
  store i32 %".35", i32* %"n"
  %".37" = load i32, i32* %"n"
  %".38" = load i32, i32* %"newGuess"
  %".39" = call i32 @"sqrt"(i32 %".37", i32 %".38")
  ret i32 %".39"
if.end:
  ret i32 0
}
