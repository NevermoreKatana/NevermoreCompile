; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %".2" = call i32 @"test"(i32 1, i32 2)
  %"result" = alloca i32
  store i32 %".2", i32* %"result"
  %".4" = load i32, i32* %"result"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"test"(i32 %".1", i32 %".2")
{
entry:
  %"x_tmp" = alloca i32
  store i32 %".1", i32* %"x_tmp"
  %"y_tmp" = alloca i32
  store i32 %".2", i32* %"y_tmp"
  %".6" = load i32, i32* %"x_tmp"
  %".7" = load i32, i32* %"y_tmp"
  %".8" = add i32 %".6", %".7"
  %"z" = alloca i32
  store i32 %".8", i32* %"z"
  %".10" = load i32, i32* %"z"
  ret i32 %".10"
}
