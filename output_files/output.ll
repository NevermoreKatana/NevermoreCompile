; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"z" = alloca i32
  store i32 2, i32* %"z"
  %"c" = alloca i32
  store i32 10, i32* %"c"
  store i32 1, i32* @"x"
  %".6" = load i32, i32* %"i"
  %".7" = load i32, i32* %"c"
  %".8" = icmp ult i32 %".6", %".7"
  br i1 %".8", label %"while", label %"end_while"
while:
  %".10" = load i32, i32* %"i"
  %".11" = load i32, i32* %"z"
  %".12" = icmp slt i32 %".10", %".11"
  br i1 %".12", label %"if.then", label %"if.else"
end_while:
  ret void
if.then:
  call void @"mult"()
  br label %"if.end"
if.else:
  call void @"plus"()
  br label %"if.end"
if.end:
  %".18" = load i32, i32* @"x"
  %".19" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".19"
  %".21" = bitcast [4 x i8]* %".19" to i32*
  %".22" = call i32 (i32*, ...) @"printf"(i32* %".21", i32 %".18")
  %".23" = load i32, i32* %"i"
  %".24" = add i32 %".23", 1
  store i32 %".24", i32* %"i"
  %".26" = load i32, i32* %"i"
  %".27" = load i32, i32* %"c"
  %".28" = icmp ult i32 %".26", %".27"
  br i1 %".28", label %"while", label %"end_while"
}

declare i32 @"printf"(i32* %".1", ...)

@"x" = global i32 0
define void @"plus"()
{
entry:
  %".2" = load i32, i32* @"x"
  %".3" = add i32 %".2", 1
  store i32 %".3", i32* @"x"
  ret void
}

define void @"mult"()
{
entry:
  %".2" = load i32, i32* @"x"
  %".3" = mul i32 %".2", 10
  store i32 %".3", i32* @"x"
  ret void
}
