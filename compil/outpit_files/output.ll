; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"x" = alloca i32
  store i32 15, i32* %"x"
  %"y" = alloca i32
  store i32 10, i32* %"y"
  %".4" = load i32, i32* %"x"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
