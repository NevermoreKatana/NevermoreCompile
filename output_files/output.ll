; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  store i32 1, i32* @"x"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".4" = load i32, i32* %"i"
  %".5" = icmp ult i32 %".4", 20
  br i1 %".5", label %"for_body", label %"exit_for"
for_body:
  %".7" = load i32, i32* @"x"
  %".8" = load i32, i32* @"x"
  %".9" = add i32 %".7", %".8"
  store i32 %".9", i32* @"x"
  %".11" = load i32, i32* %"i"
  %".12" = add i32 %".11", 1
  store i32 %".12", i32* %"i"
  %".14" = load i32, i32* %"i"
  %".15" = icmp ult i32 %".14", 20
  br i1 %".15", label %"for_body", label %"exit_for"
exit_for:
  %".17" = load i32, i32* @"x"
  %".18" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".18"
  %".20" = bitcast [4 x i8]* %".18" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".17")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"x" = global i32 0