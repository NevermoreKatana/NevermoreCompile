; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"int_pow"(i32 %".1", i32 %".2")
{
entry:
  %"result" = alloca i32
  store i32 1, i32* %"result"
  %"exponent_ptr" = alloca i32
  store i32 %".2", i32* %"exponent_ptr"
  br label %"loop"
loop:
  %"current_result" = load i32, i32* %"result"
  %"mul" = mul i32 %"current_result", %".1"
  store i32 %"mul", i32* %"result"
  %"current_exponent" = load i32, i32* %"exponent_ptr"
  %"decremented_exponent" = sub i32 %"current_exponent", 1
  store i32 %"decremented_exponent", i32* %"exponent_ptr"
  %".9" = icmp sgt i32 %"decremented_exponent", 0
  br i1 %".9", label %"loop", label %"exit"
exit:
  %".11" = load i32, i32* %"result"
  ret i32 %".11"
}

define void @"main"()
{
entry.main:
  %".2" = call i32 @"test"(i32 40)
  %"y" = alloca i32
  store i32 %".2", i32* %"y"
  %".4" = load i32, i32* %"y"
  %".5" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".5"
  %".7" = bitcast [4 x i8]* %".5" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".4")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"test"(i32 %".1")
{
entry:
  %"x_tmp" = alloca i32
  store i32 %".1", i32* %"x_tmp"
  %".4" = load i32, i32* %"x_tmp"
  %".5" = icmp eq i32 %".4", 2
  br i1 %".5", label %"if.then", label %"if.end"
if.then:
  ret i32 1
if.end:
  %".8" = load i32, i32* %"x_tmp"
  %".9" = icmp eq i32 %".8", 1
  br i1 %".9", label %"if.then.1", label %"if.end.1"
if.then.1:
  ret i32 1
if.end.1:
  %".12" = load i32, i32* %"x_tmp"
  %".13" = sub i32 %".12", 1
  %"newX" = alloca i32
  store i32 %".13", i32* %"newX"
  %".15" = load i32, i32* %"x_tmp"
  %".16" = sub i32 %".15", 2
  %"newX1" = alloca i32
  store i32 %".16", i32* %"newX1"
  %".18" = load i32, i32* %"newX"
  %".19" = call i32 @"test"(i32 %".18")
  %"result" = alloca i32
  store i32 %".19", i32* %"result"
  %".21" = load i32, i32* %"newX1"
  %".22" = call i32 @"test"(i32 %".21")
  %"result1" = alloca i32
  store i32 %".22", i32* %"result1"
  %".24" = load i32, i32* %"result"
  %".25" = load i32, i32* %"result1"
  %".26" = add i32 %".24", %".25"
  %"res" = alloca i32
  store i32 %".26", i32* %"res"
  %".28" = load i32, i32* %"res"
  ret i32 %".28"
}
