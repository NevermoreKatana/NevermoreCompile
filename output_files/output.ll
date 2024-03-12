; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"x1" = alloca i32
  store i32 15, i32* %"x1"
  %"y1" = alloca double
  store double 0x400199999999999a, double* %"y1"
  %".4" = call i32 @"test"(double 0x3ff199999999999a, i32 2)
  %"result" = alloca i32
  store i32 %".4", i32* %"result"
  %".6" = load i32, i32* %"result"
  %".7" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".7"
  %".9" = bitcast [4 x i8]* %".7" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".6")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"x" = global i32 0
define i32 @"test"(double %".1", i32 %".2")
{
entry:
  %"x_tmp" = alloca double
  store double %".1", double* %"x_tmp"
  %"y_tmp" = alloca i32
  store i32 %".2", i32* %"y_tmp"
  %".6" = load double, double* %"x_tmp"
  %".7" = alloca [4 x i8]
  store [4 x i8] c"%f\0a\00", [4 x i8]* %".7"
  %".9" = bitcast [4 x i8]* %".7" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", double %".6")
  %".11" = load i32, i32* %"y_tmp"
  %".12" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".12"
  %".14" = bitcast [4 x i8]* %".12" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".11")
  ret i32 1
}
