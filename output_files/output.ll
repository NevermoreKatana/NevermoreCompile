; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = getelementptr [3 x i8], [3 x i8]* @"format_str", i32 0, i32 0
  %".3" = bitcast [3 x i8]* @"format_str" to i8*
  %"x" = alloca i32
  store i32 15, i32* %"x"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"z" = alloca i32
  store i32 15, i32* %"z"
  %".7" = load i32, i32* %"i"
  %".8" = load i32, i32* %"z"
  %".9" = icmp ult i32 %".7", %".8"
  br i1 %".9", label %"while", label %"end_while"
while:
  %".11" = load i32, i32* %"x"
  %".12" = add i32 %".11", 1
  store i32 %".12", i32* %"x"
  %".14" = load i32, i32* %"x"
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".14")
  %".16" = load i32, i32* %"i"
  %".17" = add i32 %".16", 1
  store i32 %".17", i32* %"i"
  %".19" = load i32, i32* %"i"
  %".20" = load i32, i32* %"z"
  %".21" = icmp ult i32 %".19", %".20"
  br i1 %".21", label %"while", label %"end_while"
end_while:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"format_str" = global [3 x i8] c"%d\0a"