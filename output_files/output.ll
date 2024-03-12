; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"x" = alloca i32
  store i32 15, i32* %"x"
  %"y" = alloca double
  store double 0x4004000000000000, double* %"y"
  %".4" = load i32, i32* %"x"
  call void @"second"(i32 %".4", double 0x3ff0000000000000)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define void @"second"(i32 %".1", double %".2")
{
entry:
  %"x_tmp" = alloca i32
  store i32 %".1", i32* %"x_tmp"
  %"y_tmp" = alloca double
  store double %".2", double* %"y_tmp"
  %".6" = load i32, i32* %"x_tmp"
  %".7" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".7"
  %".9" = bitcast [4 x i8]* %".7" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".6")
  %".11" = load double, double* %"y_tmp"
  %".12" = alloca [4 x i8]
  store [4 x i8] c"%f\0a\00", [4 x i8]* %".12"
  %".14" = bitcast [4 x i8]* %".12" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", double %".11")
  ret void
}
