; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  %"x" = alloca i32
  store i32 1, i32* %"x"
  %"y" = alloca double
  store double 0x4002666666666666, double* %"y"
  %".4" = add i32 2, 4
  %".5" = udiv i32 24, 6
  %".6" = mul i32 %".5", 3
  %".7" = add i32 %".4", %".6"
  %".8" = udiv i32 24, 24
  %".9" = sub i32 %".7", %".8"
  %".10" = add i32 %".9", 31
  %"result" = alloca i32
  store i32 %".10", i32* %"result"
  %".12" = load i32, i32* %"result"
  %".13" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".13"
  %".15" = bitcast [4 x i8]* %".13" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".12")
  %".17" = load i32, i32* %"x"
  %".18" = mul i32 %".17", 2
  %".19" = load i32, i32* %"x"
  %".20" = mul i32 %".18", %".19"
  %".21" = load i32, i32* %"x"
  %".22" = udiv i32 %".20", %".21"
  %".23" = load i32, i32* %"x"
  %".24" = mul i32 %".22", %".23"
  %".25" = load i32, i32* %"x"
  %".26" = mul i32 %".24", %".25"
  %".27" = load i32, i32* %"x"
  %".28" = add i32 %".27", %".26"
  store i32 %".28", i32* %"result"
  %".30" = load i32, i32* %"result"
  %".31" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".31"
  %".33" = bitcast [4 x i8]* %".31" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", i32 %".30")
  %".35" = mul i32 2, 2
  %".36" = load i32, i32* %"x"
  %".37" = add i32 %".36", %".35"
  %".38" = load i32, i32* %"x"
  %".39" = udiv i32 %".38", 1
  %".40" = add i32 %".37", %".39"
  %".41" = mul i32 24, 6
  %".42" = udiv i32 %".41", 3
  %".43" = add i32 %".40", %".42"
  store i32 %".43", i32* %"result"
  %".45" = load i32, i32* %"result"
  %".46" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".46"
  %".48" = bitcast [4 x i8]* %".46" to i8*
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i32 %".45")
  %".50" = load double, double* %"y"
  %".51" = sitofp i32 2 to double
  %".52" = fmul double %".50", %".51"
  %".53" = load double, double* %"y"
  %".54" = fdiv double %".52", %".53"
  %".55" = sitofp i32 3 to double
  %".56" = fmul double %".54", %".55"
  %".57" = load double, double* %"y"
  %".58" = fadd double %".57", %".56"
  %".59" = load double, double* %"y"
  %".60" = load double, double* %"y"
  %".61" = fmul double %".59", %".60"
  %".62" = load double, double* %"y"
  %".63" = fdiv double %".61", %".62"
  %".64" = sitofp i32 8 to double
  %".65" = fmul double %".63", %".64"
  %".66" = fadd double %".58", %".65"
  %"result1" = alloca double
  store double %".66", double* %"result1"
  %".68" = load double, double* %"result1"
  %".69" = alloca [4 x i8]
  store [4 x i8] c"%f\0a\00", [4 x i8]* %".69"
  %".71" = bitcast [4 x i8]* %".69" to i8*
  %".72" = call i32 (i8*, ...) @"printf"(i8* %".71", double %".68")
  %".73" = load double, double* %"y"
  %".74" = sitofp i32 2 to double
  %".75" = fmul double %".74", %".73"
  %".76" = load double, double* %"y"
  %".77" = fmul double 0x400a666666666666, %".76"
  %".78" = load double, double* %"y"
  %".79" = fdiv double %".77", %".78"
  %".80" = sitofp i32 3 to double
  %".81" = fmul double %".79", %".80"
  %".82" = load double, double* %"y"
  %".83" = fmul double %".81", %".82"
  %".84" = fadd double %".75", %".83"
  %".85" = load double, double* %"y"
  %".86" = sitofp i32 4 to double
  %".87" = fmul double %".86", %".85"
  %".88" = sitofp i32 5 to double
  %".89" = fdiv double %".87", %".88"
  %".90" = fadd double %".84", %".89"
  store double %".90", double* %"result1"
  %".92" = load double, double* %"result1"
  %".93" = alloca [4 x i8]
  store [4 x i8] c"%f\0a\00", [4 x i8]* %".93"
  %".95" = bitcast [4 x i8]* %".93" to i8*
  %".96" = call i32 (i8*, ...) @"printf"(i8* %".95", double %".92")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)
