; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"x" = alloca i32
  store i32 1, i32* %"x"
  %"y" = alloca double
  store double 0x4002666666666666, double* %"y"
  call void @"test1"(i32 2, double 0x400a666666666666)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define void @"test1"(i32 %".1", double %".2")
{
entry:
  %"x_tmp" = alloca i32
  store i32 %".1", i32* %"x_tmp"
  %"y_tmp" = alloca double
  store double %".2", double* %"y_tmp"
  %".6" = load i32, i32* %"x_tmp"
  %".7" = load i32, i32* %"x_tmp"
  %".8" = mul i32 %".6", %".7"
  %".9" = load i32, i32* %"x_tmp"
  %".10" = mul i32 %".8", %".9"
  %"x" = alloca i32
  store i32 %".10", i32* %"x"
  %".12" = load i32, i32* %"x"
  %".13" = load i32, i32* %"x"
  %".14" = mul i32 %".12", %".13"
  %".15" = load double, double* %"y_tmp"
  %".16" = sitofp i32 %".14" to double
  %".17" = fdiv double %".16", %".15"
  %"y" = alloca double
  store double %".17", double* %"y"
  %".19" = load i32, i32* %"x"
  %".20" = load double, double* %"y"
  %".21" = sitofp i32 %".19" to double
  %".22" = fcmp ogt double %".21", %".20"
  br i1 %".22", label %"if.then", label %"if.else"
if.then:
  %".24" = load i32, i32* %"x_tmp"
  %".25" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".25"
  %".27" = bitcast [4 x i8]* %".25" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %".24")
  br label %"if.end"
if.else:
  %".30" = load double, double* %"y_tmp"
  %".31" = alloca [4 x i8]
  store [4 x i8] c"%f\0a\00", [4 x i8]* %".31"
  %".33" = bitcast [4 x i8]* %".31" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", double %".30")
  br label %"if.end"
if.end:
  ret void
}
