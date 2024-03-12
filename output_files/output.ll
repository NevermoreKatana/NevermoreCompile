; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %".2" = call i32 @"second"()
  %"x" = alloca i32
  store i32 %".2", i32* %"x"
  %".4" = load i32, i32* %"x"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"second"()
{
entry:
  %"x" = alloca i32
  store i32 10, i32* %"x"
  %"y" = alloca i32
  store i32 12, i32* %"y"
  %".4" = load i32, i32* %"x"
  %".5" = load i32, i32* %"y"
  %".6" = load i32, i32* %"x"
  %".7" = icmp ult i32 %".4", %".5"
  br i1 %".7", label %"while", label %"end_while"
while:
  %".9" = load i32, i32* %"x"
  %".10" = add i32 %".9", 1
  store i32 %".10", i32* %"x"
  %".12" = load i32, i32* %"x"
  %".13" = icmp ult i32 %".12", %".5"
  br i1 %".13", label %"while", label %"end_while"
end_while:
  store i32 %".6", i32* %"x"
  ret i32 1
}
