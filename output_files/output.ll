; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = getelementptr [3 x i8], [3 x i8]* @"format_str", i32 0, i32 0
  %".3" = bitcast [3 x i8]* @"format_str" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 7)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"format_str" = global [3 x i8] c"%d\0a"