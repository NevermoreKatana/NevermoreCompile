; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  call void @"secondary"()
  %"y" = alloca i32
  store i32 0, i32* %"y"
  %".4" = load i32, i32* %"y"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i32*
  %".8" = call i32 (i32*, ...) @"printf"(i32* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i32* %".1", ...)

define void @"secondary"()
{
entry:
  %"y" = alloca i32
  store i32 23, i32* %"y"
  %".3" = load i32, i32* %"y"
  %".4" = load i32, i32* %"y"
  %".5" = mul i32 %".3", %".4"
  %".6" = mul i32 %".3", %".4"
  %".7" = load i32, i32* %"y"
  %".8" = load i32, i32* %"y"
  %".9" = mul i32 %".7", %".8"
  %".10" = mul i32 %".7", %".8"
  %"y.1" = alloca i32
  store i32 %".10", i32* %"y.1"
  %".12" = load i32, i32* %"y.1"
  %".13" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".13"
  %".15" = bitcast [4 x i8]* %".13" to i32*
  %".16" = call i32 (i32*, ...) @"printf"(i32* %".15", i32 %".12")
  ret void
}
