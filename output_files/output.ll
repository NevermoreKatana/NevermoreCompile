; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"x" = alloca i32
  store i32 10, i32* %"x"
  %"t" = alloca i32
  store i32 15, i32* %"t"
  %"y" = alloca double
  store double 0x402e333333333333, double* %"y"
  %"z" = alloca double
  store double 0x4026333333333333, double* %"z"
  %".6" = load i32, i32* %"x"
  %".7" = load i32, i32* %"t"
  br label %"do_while_start"
do_while_start:
  %".9" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".9"
  %".11" = bitcast [4 x i8]* %".9" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 110)
  %".13" = load i32, i32* %"x"
  %".14" = icmp ult i32 %".13", %".7"
  br i1 %".14", label %"do_while_body", label %"do_while_end"
do_while_body:
  %".16" = load i32, i32* %"x"
  %".17" = add i32 %".16", 1
  store i32 %".17", i32* %"x"
  br label %"do_while_start"
do_while_end:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
