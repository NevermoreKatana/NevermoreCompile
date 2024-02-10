; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = getelementptr [3 x i8], [3 x i8]* @"format_str", i32 0, i32 0
  %".3" = bitcast [3 x i8]* @"format_str" to i8*
  %"x" = alloca i32
  store i32 0, i32* %"x"
  %"y" = alloca i32
  store i32 5, i32* %"y"
  br label %"loop_start"
loop_start:
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 15)
  %".8" = load i32, i32* %"x"
  %".9" = icmp ult i32 %".8", 5
  br i1 %".9", label %"loop_body", label %"loop_end"
loop_body:
  %".11" = load i32, i32* %"x"
  %".12" = add i32 %".11", 1
  store i32 %".12", i32* %"x"
  %".14" = icmp ult i32 %".12", 5
  br label %"loop_start"
loop_end:
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 123123)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"format_str" = global [3 x i8] c"%d\0a"