; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  call void @"secondary"()
  %".3" = load i32, i32* @"y"
  %".4" = load i32, i32* @"y"
  %".5" = mul i32 %".3", %".4"
  store i32 %".5", i32* @"y"
  %".7" = load i32, i32* @"y"
  %".8" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".8"
  %".10" = bitcast [4 x i8]* %".8" to i32*
  %".11" = call i32 (i32*, ...) @"printf"(i32* %".10", i32 %".7")
  ret void
}

declare i32 @"printf"(i32* %".1", ...)

@"y" = global i32 0
define void @"secondary"()
{
entry:
  store i32 23, i32* @"y"
  %".3" = load i32, i32* @"y"
  %".4" = load i32, i32* @"y"
  %".5" = mul i32 %".3", %".4"
  store i32 %".5", i32* @"y"
  %".7" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".7"
  %".9" = bitcast [4 x i8]* %".7" to i32*
  %".10" = call i32 (i32*, ...) @"printf"(i32* %".9", i32 123)
  ret void
}
