; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"x" = alloca double
  store double 0x3ff199999999999a, double* %"x"
  %"y" = alloca i32
  store i32 1, i32* %"y"
  %".4" = load double, double* %"x"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%f\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %".4")
  %".9" = alloca [4 x i8]
  store [4 x i8] c"%f\0a\00", [4 x i8]* %".9"
  %".11" = bitcast [4 x i8]* %".9" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", double 0x3ff3333333333333)
  %".13" = load i32, i32* %"y"
  %".14" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".14"
  %".16" = bitcast [4 x i8]* %".14" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %".13")
  %".18" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".18"
  %".20" = bitcast [4 x i8]* %".18" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 2)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
