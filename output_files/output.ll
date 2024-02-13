; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = getelementptr [3 x i8], [3 x i8]* @"format_str", i32 0, i32 0
  %".3" = bitcast [3 x i8]* @"format_str" to i8*
  %"result" = alloca i32
  store i32 1097, i32* %"result"
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 1097)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"format_str" = global [3 x i8] c"%d\0a"