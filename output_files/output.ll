; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %".2" = getelementptr [3 x i8], [3 x i8]* @"format_str_int", i32 0, i32 0
  %".3" = bitcast [3 x i8]* @"format_str_int" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 77777)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"format_str_int" = global [3 x i8] c"%d\0a"