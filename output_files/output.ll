; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  store i32 15, i32* @"x"
  call void @"secondary"()
  %".4" = load i32, i32* @"x"
  %".5" = alloca [3 x i8]
  store [3 x i8] c"%d\00", [3 x i8]* %".5"
  %".7" = bitcast [3 x i8]* %".5" to i32*
  %".8" = call i32 (i32*, ...) @"printf"(i32* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i32* %".1", ...)

@"x" = global i32 0
define void @"secondary"()
{
entry:
  %".2" = mul i32 15, 15
  store i32 %".2", i32* @"x"
  %"y" = alloca i32
  store i32 123123, i32* %"y"
  %".5" = load i32, i32* %"y"
  %".6" = alloca [3 x i8]
  store [3 x i8] c"%d\00", [3 x i8]* %".6"
  %".8" = bitcast [3 x i8]* %".6" to i32*
  %".9" = call i32 (i32*, ...) @"printf"(i32* %".8", i32 %".5")
  ret void
}
