; ModuleID = "nevermoreCompile"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry.main:
  ret void
}

declare i32 @"printf"(i32* %".1", ...)

define i32 @"second"(i32 %".1")
{
entry:
  ret i32 15
}
