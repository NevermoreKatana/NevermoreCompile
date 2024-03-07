; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %".2" = call i32 @"calc"(i32 0, i32 3)
  %"res" = alloca i32
  store i32 %".2", i32* %"res"
  %".4" = load i32, i32* %"res"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"calc"(i32 %".1", i32 %".2")
{
entry:
  %"x_tmp" = alloca i32
  store i32 %".1", i32* %"x_tmp"
  %"y_tmp" = alloca i32
  store i32 %".2", i32* %"y_tmp"
  %".6" = load i32, i32* %"x_tmp"
  %".7" = load i32, i32* %"y_tmp"
  %".8" = mul i32 %".6", %".7"
  %".9" = mul i32 %".8", 24
  %"result" = alloca i32
  store i32 %".9", i32* %"result"
  %".11" = load i32, i32* %"result"
  ret i32 %".11"
}
