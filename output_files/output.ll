; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = getelementptr [3 x i8], [3 x i8]* @"format_str", i32 0, i32 0
  %".3" = bitcast [3 x i8]* @"format_str" to i8*
  %"x" = alloca i32
  store i32 30, i32* %"x"
  %".5" = load i32, i32* %"x"
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".5")
  store i32 40, i32* %"x"
  %".8" = load i32, i32* %"x"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".8")
  store i32 4000, i32* %"x"
  %".11" = load i32, i32* %"x"
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".11")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"format_str" = global [3 x i8] c"%d\0a"
@"z" = global i32 0