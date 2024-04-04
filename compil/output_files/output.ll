; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"int_pow"(i32 %".1", i32 %".2")
{
entry:
  %"result" = alloca i32
  store i32 1, i32* %"result"
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
  %".9" = icmp sgt i32 %"decremented_exponent", 0
  br i1 %".9", label %"loop", label %"exit"
exit:
  %".11" = load i32, i32* %"result"
  ret i32 %".11"
}

define void @"main"()
{
entry.main:
  %".2" = call double @"sqrt"(i32 120, double 0x3ff0000000000000, double 0x3f1a36e2eb1c432d)
  %"z" = alloca double
  store double %".2", double* %"z"
  %".4" = load double, double* %"z"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%f\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %".4")
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

define double @"sqrt"(i32 %".1", double %".2", double %".3")
{
entry:
  %"number_tmp" = alloca i32
  store i32 %".1", i32* %"number_tmp"
  %"guess_tmp" = alloca double
  store double %".2", double* %"guess_tmp"
  %"tolerance_tmp" = alloca double
  store double %".3", double* %"tolerance_tmp"
  %".8" = load double, double* %"guess_tmp"
  %".9" = load double, double* %"guess_tmp"
  %".10" = fmul double %".8", %".9"
  %".11" = load i32, i32* %"number_tmp"
  %".12" = sitofp i32 %".11" to double
  %".13" = fsub double %".10", %".12"
  %"neguess" = alloca double
  store double %".13", double* %"neguess"
  %".15" = load double, double* %"neguess"
  %".16" = call double @"absf"(double %".15")
  store double %".16", double* %"neguess"
  %".18" = load double, double* %"neguess"
  %".19" = load double, double* %"tolerance_tmp"
  %".20" = fcmp olt double %".18", %".19"
  br i1 %".20", label %"if.then", label %"if.else"
if.then:
  %".22" = load double, double* %"guess_tmp"
  ret double %".22"
if.else:
  %".24" = load i32, i32* %"number_tmp"
  %".25" = load double, double* %"guess_tmp"
  %".26" = sitofp i32 %".24" to double
  %".27" = fdiv double %".26", %".25"
  %".28" = load double, double* %"guess_tmp"
  %".29" = fadd double %".27", %".28"
  %"newGuess" = alloca double
  store double %".29", double* %"newGuess"
  %".31" = load double, double* %"newGuess"
  %".32" = sitofp i32 2 to double
  %".33" = fdiv double %".31", %".32"
  store double %".33", double* %"newGuess"
  %"n" = alloca i32
  %".35" = load i32, i32* %"number_tmp"
  store i32 %".35", i32* %"n"
  %"t" = alloca double
  %".37" = load double, double* %"tolerance_tmp"
  store double %".37", double* %"t"
  %".39" = load i32, i32* %"n"
  %".40" = load double, double* %"newGuess"
  %".41" = load double, double* %"t"
  %".42" = call double @"sqrt"(i32 %".39", double %".40", double %".41")
  ret double %".42"
if.end:
  ret double              0x0
}
