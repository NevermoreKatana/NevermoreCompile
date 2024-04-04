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
  %"pi" = alloca double
  store double 0x400921fb54442d18, double* %"pi"
  %".3" = load double, double* %"pi"
  %".4" = fdiv double %".3", 0x4066800000000000
  store double %".4", double* @"coef"
  %".6" = call double @"sin"(i32 250000)
  %"test" = alloca double
  store double %".6", double* %"test"
  %".8" = load double, double* %"test"
  %".9" = alloca [4 x i8]
  store [4 x i8] c"%f\0a\00", [4 x i8]* %".9"
  %".11" = bitcast [4 x i8]* %".9" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", double %".8")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"coef" = global double              0x0

define double @"absf"(double %".1")
{
entry:
  %"result" = fsub double              0x0, %".1"
  %".3" = fcmp ult double %".1",              0x0
  %".4" = select  i1 %".3", double %"result", double %".1"
  ret double %".4"
}

define i32 @"factorial"(i32 %".1")
{
entry:
  %"x_tmp" = alloca i32
  store i32 %".1", i32* %"x_tmp"
  %".4" = load i32, i32* %"x_tmp"
  %".5" = icmp eq i32 %".4", 0
  br i1 %".5", label %"if.then", label %"if.else"
if.then:
  ret i32 1
if.else:
  %".8" = load i32, i32* %"x_tmp"
  %".9" = sub i32 %".8", 1
  %"newX" = alloca i32
  store i32 %".9", i32* %"newX"
  %".11" = load i32, i32* %"newX"
  %".12" = call i32 @"factorial"(i32 %".11")
  %"newF" = alloca i32
  store i32 %".12", i32* %"newF"
  %".14" = load i32, i32* %"x_tmp"
  %".15" = load i32, i32* %"newF"
  %".16" = mul i32 %".14", %".15"
  %"res" = alloca i32
  store i32 %".16", i32* %"res"
  %".18" = load i32, i32* %"res"
  ret i32 %".18"
if.end:
  ret i32 0
}

define double @"sin"(i32 %".1")
{
entry:
  %"degrees_tmp" = alloca i32
  store i32 %".1", i32* %"degrees_tmp"
  %".4" = load i32, i32* %"degrees_tmp"
  %".5" = load double, double* @"coef"
  %".6" = sitofp i32 %".4" to double
  %".7" = fmul double %".6", %".5"
  %"angleRad" = alloca double
  store double %".7", double* %"angleRad"
  %"sinValue" = alloca double
  store double              0x0, double* %"sinValue"
  %"minusOdin" = alloca i32
  store i32 -1, i32* %"minusOdin"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".12" = load i32, i32* %"i"
  %".13" = icmp ult i32 %".12", 10
  br i1 %".13", label %"for_body", label %"exit_for"
for_body:
  %".15" = load i32, i32* %"minusOdin"
  %".16" = load i32, i32* %"i"
  %".17" = call i32 @"int_pow"(i32 %".15", i32 %".16")
  %"sign" = alloca i32
  store i32 %".17", i32* %"sign"
  %".19" = load i32, i32* %"sign"
  %".20" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".20"
  %".22" = bitcast [4 x i8]* %".20" to i8*
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 %".19")
  %".24" = load i32, i32* %"i"
  %".25" = mul i32 2, %".24"
  %".26" = add i32 %".25", 1
  %"factrParm" = alloca i32
  store i32 %".26", i32* %"factrParm"
  %".28" = load i32, i32* %"factrParm"
  %".29" = call i32 @"factorial"(i32 %".28")
  %"factr" = alloca i32
  store i32 %".29", i32* %"factr"
  %".31" = load double, double* %"angleRad"
  %".32" = load i32, i32* %"factrParm"
  %".33" = call double @"double_pow"(double %".31", i32 %".32")
  %"pow" = alloca double
  store double %".33", double* %"pow"
  %".35" = load double, double* %"pow"
  %".36" = load i32, i32* %"factr"
  %".37" = sitofp i32 %".36" to double
  %".38" = fdiv double %".35", %".37"
  %"term" = alloca double
  store double %".38", double* %"term"
  %".40" = load i32, i32* %"sign"
  %".41" = load double, double* %"term"
  %".42" = sitofp i32 %".40" to double
  %".43" = fmul double %".42", %".41"
  %".44" = load double, double* %"sinValue"
  %".45" = fadd double %".44", %".43"
  store double %".45", double* %"sinValue"
  %".47" = load i32, i32* %"i"
  %".48" = add i32 %".47", 1
  store i32 %".48", i32* %"i"
  %".50" = load i32, i32* %"i"
  %".51" = icmp ult i32 %".50", 10
  br i1 %".51", label %"for_body", label %"exit_for"
exit_for:
  %".53" = load double, double* %"sinValue"
  ret double %".53"
}
