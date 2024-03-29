; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"x" = alloca i32
  store i32 13, i32* %"x"
  %".3" = load i32, i32* %"x"
  %".4" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".4"
  %".6" = bitcast [4 x i8]* %".4" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".3")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
