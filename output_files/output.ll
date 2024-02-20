; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  store i32 15, i32* @"x"
  call void @"secondary"()
  %".4" = load i32, i32* @"x"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i32*
  %".8" = call i32 (i32*, ...) @"printf"(i32* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i32* %".1", ...)

@"x" = global i32 0
define void @"secondary"()
{
entry:
  %".2" = mul i32 15, 15
  %".3" = mul i32 15, 15
  %".4" = mul i32 15, 15
  %".5" = mul i32 15, 15
  store i32 %".5", i32* @"x"
  %"y" = alloca i32
  store i32 123123, i32* %"y"
  %".8" = load i32, i32* %"y"
  %".9" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".9"
  %".11" = bitcast [4 x i8]* %".9" to i32*
  %".12" = call i32 (i32*, ...) @"printf"(i32* %".11", i32 %".8")
  ret void
}
