; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
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
  %".7" = bitcast [4 x i8]* %".5" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"second"()
{
entry:
  %".2" = icmp sgt i32 3, 2
  br i1 %".2", label %"if.then", label %"if.end"
if.then:
  %"x" = alloca i32
  store i32 123, i32* %"x"
  br label %"if.end"
if.end:
  %".6" = load i32, i32* %"x"
  ret i32 %".6"
}
