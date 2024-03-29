; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  call void @"test1"()
  ret void
}

declare i32 @"printf"(i8* %".1", ...)


define void @"test1"()
{
entry:
  %".2" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".2"
  %".4" = bitcast [4 x i8]* %".2" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 2)
  ret void
}
