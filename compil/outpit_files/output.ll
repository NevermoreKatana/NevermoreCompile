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
  %"result" = alloca i32
  store i32 48, i32* %"result"
  %".5" = load i32, i32* %"result"
  %".6" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".6"
  %".8" = bitcast [4 x i8]* %".6" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".5")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
