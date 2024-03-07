; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"i1" = alloca i32
  store i32 1, i32* %"i1"
  %"d" = alloca double
  store double 0x4000cccccccccccd, double* %"d"
  %"d1" = alloca double
  store double 0x4002666666666666, double* %"d1"
  %".6" = icmp slt i32 3, 5
  br i1 %".6", label %"if.then", label %"if.end"
if.then:
  %".8" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".8"
  %".10" = bitcast [4 x i8]* %".8" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 7)
  br label %"if.end"
if.end:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
