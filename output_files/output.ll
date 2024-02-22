; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  store i32 2, i32* @"x"
  %".3" = load i32, i32* @"x"
  %".4" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".4"
  %".6" = bitcast [4 x i8]* %".4" to i32*
  %".7" = call i32 (i32*, ...) @"printf"(i32* %".6", i32 %".3")
  ret void
}

declare i32 @"printf"(i32* %".1", ...)

@"x" = global i32 0
define void @"secondary"()
{
entry:
  %".2" = load i32, i32* @"x"
  %".3" = load i32, i32* @"x"
  %".4" = mul i32 %".2", %".3"
  store i32 %".4", i32* @"x"
  ret void
}
