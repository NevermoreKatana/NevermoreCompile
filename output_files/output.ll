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
  %".5" = load i32, i32* %"x"
  %".6" = icmp ult i32 %".5", 25
  br i1 %".6", label %"loop_body", label %"exit"
loop_body:
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 15)
  %".9" = load i32, i32* %"x"
  %".10" = add i32 %".9", 1
  store i32 %".10", i32* %"x"
  %".12" = load i32, i32* %"x"
  %".13" = icmp ult i32 %".12", 25
  br i1 %".13", label %"loop_body", label %"exit"
exit:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"format_str" = global [3 x i8] c"%d\0a"