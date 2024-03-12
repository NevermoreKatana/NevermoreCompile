; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"i" = alloca i32
  store i32 15, i32* %"i"
  %".3" = load i32, i32* %"i"
  %".4" = icmp ugt i32 %".3", 5
  br i1 %".4", label %"for_body", label %"exit_for"
for_body:
  %".6" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".6"
  %".8" = bitcast [4 x i8]* %".6" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 11)
  %".10" = load i32, i32* %"i"
  %".11" = sub i32 %".10", 1
  store i32 %".11", i32* %"i"
  %".13" = load i32, i32* %"i"
  %".14" = icmp ugt i32 %".13", 5
  br i1 %".14", label %"for_body", label %"exit_for"
exit_for:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
