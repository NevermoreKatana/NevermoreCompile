; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %".2" = call i32 @"second"()
  %"z" = alloca i32
  store i32 %".2", i32* %"z"
  %".4" = load i32, i32* %"z"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i32*
  %".8" = call i32 (i32*, ...) @"printf"(i32* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i32* %".1", ...)

define i32 @"second"()
{
entry:
  %"x" = alloca i32
  store i32 1, i32* %"x"
  %"y" = alloca i32
  store i32 10, i32* %"y"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"counter" = alloca i32
  store i32 10, i32* %"counter"
  %".6" = load i32, i32* %"i"
  %".7" = load i32, i32* %"counter"
  %".8" = icmp ult i32 %".6", %".7"
  br i1 %".8", label %"while", label %"end_while"
while:
  %".10" = load i32, i32* %"y"
  %".11" = add i32 %".10", 1
  store i32 %".11", i32* %"y"
  %".13" = load i32, i32* %"i"
  %".14" = add i32 %".13", 1
  store i32 %".14", i32* %"i"
  %".16" = load i32, i32* %"i"
  %".17" = load i32, i32* %"counter"
  %".18" = icmp ult i32 %".16", %".17"
  br i1 %".18", label %"while", label %"end_while"
end_while:
  %".20" = load i32, i32* %"y"
  ret i32 %".20"
}
