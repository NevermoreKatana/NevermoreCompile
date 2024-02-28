; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %".2" = call i32 @"second"()
  %"x" = alloca i32
  store i32 %".2", i32* %"x"
  %".4" = load i32, i32* %"x"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i32*
  %".8" = call i32 (i32*, ...) @"printf"(i32* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i32* %".1", ...)

define i32 @"second"()
{
entry:
  ret i32 125
}
