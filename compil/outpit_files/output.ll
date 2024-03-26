; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %".2" = call i32 @"calculate"(i32 1)
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

define i32 @"calculate"(i32 %".1")
{
entry:
  %"x_tmp" = alloca i32
  store i32 %".1", i32* %"x_tmp"
  %".4" = load i32, i32* %"x_tmp"
  %".5" = icmp slt i32 %".4", 2
  br i1 %".5", label %"if.then", label %"if.end"
if.then:
  ret i32 1
if.end:
  ret i32 0
}
