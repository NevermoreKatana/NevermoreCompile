; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = getelementptr [3 x i8], [3 x i8]* @"format_str", i32 0, i32 0
  %".3" = bitcast [3 x i8]* @"format_str" to i8*
  %"c" = alloca i32
  store i32 10, i32* %"c"
  %"t" = alloca i32
  store i32 15, i32* %"t"
  %".6" = icmp slt i32 1, 2
  br i1 %".6", label %"if.then", label %"if.end"
if.then:
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 1)
  %".9" = icmp slt i32 15, 10
  br i1 %".9", label %"if_else.then", label %"if_else.else"
if.end:
  ret void
if_else.then:
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 2)
  br label %"if_else.end"
if_else.else:
  %".13" = icmp slt i32 1, 2
  br i1 %".13", label %"if.then.1", label %"if.end.1"
if_else.end:
  br label %"if.end"
if.then.1:
  %".15" = load i32, i32* %"c"
  %".16" = icmp ult i32 %".15", 15
  br i1 %".16", label %"while", label %"end"
if.end.1:
  br label %"if_else.end"
while:
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 3)
  %".19" = load i32, i32* %"c"
  %".20" = add i32 %".19", 1
  store i32 %".20", i32* %"c"
  %".22" = load i32, i32* %"c"
  %".23" = icmp ult i32 %".22", 15
  br i1 %".23", label %"while", label %"end"
end:
  br label %"if.end.1"
}

declare i32 @"printf"(i8* %".1", ...)

@"format_str" = global [3 x i8] c"%d\0a"