; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"i" = alloca i32
  store i32 40, i32* %"i"
  %"c" = alloca i32
  store i32 60, i32* %"c"
  %".4" = load i32, i32* %"i"
  %".5" = load i32, i32* %"c"
  %".6" = load i32, i32* %"i"
  %".7" = icmp ult i32 %".4", %".5"
  br i1 %".7", label %"while", label %"end_while"
while:
  %".9" = load i32, i32* %"i"
  %".10" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".10"
  %".12" = bitcast [4 x i8]* %".10" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".9")
  %".14" = load i32, i32* %"i"
  %".15" = add i32 %".14", 1
  store i32 %".15", i32* %"i"
  %".17" = load i32, i32* %"i"
  %".18" = icmp ult i32 %".17", %".5"
  br i1 %".18", label %"while", label %"end_while"
end_while:
  store i32 %".6", i32* %"i"
  %".21" = load i32, i32* %"i"
  %".22" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".22"
  %".24" = bitcast [4 x i8]* %".22" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %".21")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
