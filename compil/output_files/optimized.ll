; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %".2" = call i32 @"test6"(i32 1, i32 3)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)






define i32 @"test6"(i32 %".1", i32 %".2")
{
entry:
  %"y_tmp" = alloca i32
  store i32 %".1", i32* %"y_tmp"
  %"z_tmp" = alloca i32
  store i32 %".2", i32* %"z_tmp"
  %".6" = load i32, i32* %"y_tmp"
  %".7" = load i32, i32* %"z_tmp"
  %".8" = add i32 %".6", %".7"
  %"res" = alloca i32
  store i32 %".8", i32* %"res"
  %".10" = load i32, i32* %"res"
  %".11" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".11"
  %".13" = bitcast [4 x i8]* %".11" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 %".10")
  ret i32 0
}
