; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %".2" = add i32 15, 15
  %".3" = add i32 %".2", 15
  %"x" = alloca i32
  store i32 %".3", i32* %"x"
  %".5" = load i32, i32* %"x"
  %".6" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".6"
  %".8" = bitcast [4 x i8]* %".6" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".5")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
