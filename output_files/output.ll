; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = getelementptr [3 x i8], [3 x i8]* @"format_str", i32 0, i32 0
  %".3" = bitcast [3 x i8]* @"format_str" to i8*
  store i32 0, i32* @"x"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"z" = alloca i32
  store i32 5, i32* %"z"
  %".7" = load i32, i32* %"i"
  %".8" = load i32, i32* %"z"
  %".9" = icmp ult i32 %".7", %".8"
  br i1 %".9", label %"while", label %"end_while"
while:
  %".11" = load i32, i32* @"x"
  %".12" = add i32 %".11", 1
  store i32 %".12", i32* @"x"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 123)
  %".15" = load i32, i32* %"i"
  %".16" = add i32 %".15", 1
  store i32 %".16", i32* %"i"
  %".18" = load i32, i32* %"i"
  %".19" = load i32, i32* %"z"
  %".20" = icmp ult i32 %".18", %".19"
  br i1 %".20", label %"while", label %"end_while"
end_while:
  %".22" = load i32, i32* @"x"
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".22")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"format_str" = global [3 x i8] c"%d\0a"
@"x" = global i32 0