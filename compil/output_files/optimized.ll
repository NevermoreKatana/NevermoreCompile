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
  %".6" = call double @"sin"(i32 90)
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
  %".19" = load i32, i32* %"i"
  %".20" = mul i32 2, %".19"
  %".21" = add i32 %".20", 1
  %"factrParm" = alloca i32
  store i32 %".21", i32* %"factrParm"
  %".23" = load i32, i32* %"factrParm"
  %".24" = call i32 @"factorial"(i32 %".23")
  %"factr" = alloca i32
  store i32 %".24", i32* %"factr"
  %".26" = load double, double* %"angleRad"
  %".27" = load i32, i32* %"factrParm"
  %".28" = call double @"double_pow"(double %".26", i32 %".27")
  %"pow" = alloca double
  store double %".28", double* %"pow"
  %".30" = load double, double* %"pow"
  %".31" = load i32, i32* %"factr"
  %".32" = sitofp i32 %".31" to double
  %".33" = fdiv double %".30", %".32"
  %"term" = alloca double
  store double %".33", double* %"term"
  %".35" = load i32, i32* %"sign"
  %".36" = load double, double* %"term"
  %".37" = sitofp i32 %".35" to double
  %".38" = fmul double %".37", %".36"
  %".39" = load double, double* %"sinValue"
  %".40" = fadd double %".39", %".38"
  store double %".40", double* %"sinValue"
  %".42" = load i32, i32* %"i"
  %".43" = add i32 %".42", 1
  store i32 %".43", i32* %"i"
  %".45" = load i32, i32* %"i"
  %".46" = icmp ult i32 %".45", 10
  br i1 %".46", label %"for_body", label %"exit_for"
exit_for:
  %".48" = load double, double* %"sinValue"
  ret double %".48"
}
