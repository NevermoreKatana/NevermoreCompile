; ModuleID = "nevermoreCompile"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry.main:
  store i32 1, i32* @"j"
  %"x" = alloca i32
  store i32 0, i32* %"x"
  %"y" = alloca i32
  store i32 2, i32* %"y"
  %"d" = alloca double
  store double 0x4002666666666666, double* %"d"
  %"z" = alloca double
  store double 0x400a666666666666, double* %"z"
  %".7" = load i32, i32* %"x"
  %".8" = load i32, i32* %"y"
  %".9" = icmp slt i32 %".7", %".8"
  br i1 %".9", label %"if.then", label %"if.end"
if.then:
  %".11" = load i32, i32* @"j"
  %".12" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".12"
  %".14" = bitcast [4 x i8]* %".12" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".11")
  br label %"if.end"
if.end:
  %".17" = load i32, i32* %"x"
  %".18" = load i32, i32* %"y"
  %".19" = icmp sgt i32 %".17", %".18"
  br i1 %".19", label %"if.then.1", label %"if.else"
if.then.1:
  %".21" = load i32, i32* @"j"
  %".22" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".22"
  %".24" = bitcast [4 x i8]* %".22" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %".21")
  br label %"if.end.1"
if.else:
  %".27" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".27"
  %".29" = bitcast [4 x i8]* %".27" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i32 22)
  br label %"if.end.1"
if.end.1:
  %".32" = load double, double* %"d"
  %".33" = load double, double* %"z"
  %".34" = fcmp olt double %".32", %".33"
  br i1 %".34", label %"if.then.2", label %"if.end.2"
if.then.2:
  %".36" = load i32, i32* @"j"
  %".37" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".37"
  %".39" = bitcast [4 x i8]* %".37" to i8*
  %".40" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".36")
  br label %"if.end.2"
if.end.2:
  %".42" = load double, double* %"d"
  %".43" = load double, double* %"z"
  %".44" = fcmp ogt double %".42", %".43"
  br i1 %".44", label %"if.then.3", label %"if.else.1"
if.then.3:
  %".46" = load i32, i32* @"j"
  %".47" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".47"
  %".49" = bitcast [4 x i8]* %".47" to i8*
  %".50" = call i32 (i8*, ...) @"printf"(i8* %".49", i32 %".46")
  br label %"if.end.3"
if.else.1:
  %".52" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".52"
  %".54" = bitcast [4 x i8]* %".52" to i8*
  %".55" = call i32 (i8*, ...) @"printf"(i8* %".54", i32 22)
  br label %"if.end.3"
if.end.3:
  %".57" = load double, double* %"d"
  %".58" = load double, double* %"z"
  %".59" = fcmp one double %".57", %".58"
  br i1 %".59", label %"if.then.4", label %"if.end.4"
if.then.4:
  %".61" = load i32, i32* @"j"
  %".62" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".62"
  %".64" = bitcast [4 x i8]* %".62" to i8*
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".64", i32 %".61")
  br label %"if.end.4"
if.end.4:
  %".67" = load double, double* %"d"
  %".68" = load double, double* %"z"
  %".69" = fcmp oeq double %".67", %".68"
  br i1 %".69", label %"if.then.5", label %"if.else.2"
if.then.5:
  %".71" = load i32, i32* @"j"
  %".72" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".72"
  %".74" = bitcast [4 x i8]* %".72" to i8*
  %".75" = call i32 (i8*, ...) @"printf"(i8* %".74", i32 %".71")
  br label %"if.end.5"
if.else.2:
  %".77" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".77"
  %".79" = bitcast [4 x i8]* %".77" to i8*
  %".80" = call i32 (i8*, ...) @"printf"(i8* %".79", i32 22)
  br label %"if.end.5"
if.end.5:
  %".82" = load i32, i32* %"x"
  %".83" = load double, double* %"z"
  %".84" = sitofp i32 %".82" to double
  %".85" = fcmp one double %".84", %".83"
  br i1 %".85", label %"if.then.6", label %"if.end.6"
if.then.6:
  %".87" = load i32, i32* @"j"
  %".88" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".88"
  %".90" = bitcast [4 x i8]* %".88" to i8*
  %".91" = call i32 (i8*, ...) @"printf"(i8* %".90", i32 %".87")
  br label %"if.end.6"
if.end.6:
  %".93" = load i32, i32* %"x"
  %".94" = load double, double* %"z"
  %".95" = sitofp i32 %".93" to double
  %".96" = fcmp oeq double %".95", %".94"
  br i1 %".96", label %"if.then.7", label %"if.else.3"
if.then.7:
  %".98" = load i32, i32* @"j"
  %".99" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".99"
  %".101" = bitcast [4 x i8]* %".99" to i8*
  %".102" = call i32 (i8*, ...) @"printf"(i8* %".101", i32 %".98")
  br label %"if.end.7"
if.else.3:
  %".104" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".104"
  %".106" = bitcast [4 x i8]* %".104" to i8*
  %".107" = call i32 (i8*, ...) @"printf"(i8* %".106", i32 22)
  br label %"if.end.7"
if.end.7:
  %".109" = load double, double* %"d"
  %".110" = load i32, i32* %"x"
  %".111" = sitofp i32 %".110" to double
  %".112" = fcmp ogt double %".109", %".111"
  br i1 %".112", label %"if.then.8", label %"if.end.8"
if.then.8:
  %".114" = load i32, i32* @"j"
  %".115" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".115"
  %".117" = bitcast [4 x i8]* %".115" to i8*
  %".118" = call i32 (i8*, ...) @"printf"(i8* %".117", i32 %".114")
  br label %"if.end.8"
if.end.8:
  %".120" = load double, double* %"z"
  %".121" = load i32, i32* %"y"
  %".122" = sitofp i32 %".121" to double
  %".123" = fcmp ogt double %".120", %".122"
  br i1 %".123", label %"if.then.9", label %"if.end.9"
if.then.9:
  %".125" = load i32, i32* @"j"
  %".126" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".126"
  %".128" = bitcast [4 x i8]* %".126" to i8*
  %".129" = call i32 (i8*, ...) @"printf"(i8* %".128", i32 %".125")
  br label %"if.end.9"
if.end.9:
  call void @"test"(i32 1, i32 2, double 0x400199999999999a, double 0x400999999999999a)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"j" = global i32 0
define void @"test"(i32 %".1", i32 %".2", double %".3", double %".4")
{
entry:
  %"x_tmp" = alloca i32
  store i32 %".1", i32* %"x_tmp"
  %"y_tmp" = alloca i32
  store i32 %".2", i32* %"y_tmp"
  %"d_tmp" = alloca double
  store double %".3", double* %"d_tmp"
  %"z_tmp" = alloca double
  store double %".4", double* %"z_tmp"
  %".10" = load i32, i32* %"x_tmp"
  %".11" = load i32, i32* %"y_tmp"
  %".12" = icmp slt i32 %".10", %".11"
  br i1 %".12", label %"if.then", label %"if.end"
if.then:
  %".14" = load i32, i32* @"j"
  %".15" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".15"
  %".17" = bitcast [4 x i8]* %".15" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %".14")
  br label %"if.end"
if.end:
  %".20" = load i32, i32* %"x_tmp"
  %".21" = load i32, i32* %"y_tmp"
  %".22" = icmp sgt i32 %".20", %".21"
  br i1 %".22", label %"if.then.1", label %"if.else"
if.then.1:
  %".24" = load i32, i32* @"j"
  %".25" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".25"
  %".27" = bitcast [4 x i8]* %".25" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %".24")
  br label %"if.end.1"
if.else:
  %".30" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".30"
  %".32" = bitcast [4 x i8]* %".30" to i8*
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".32", i32 22)
  br label %"if.end.1"
if.end.1:
  %".35" = load double, double* %"d_tmp"
  %".36" = load double, double* %"z_tmp"
  %".37" = fcmp olt double %".35", %".36"
  br i1 %".37", label %"if.then.2", label %"if.end.2"
if.then.2:
  %".39" = load i32, i32* @"j"
  %".40" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".40"
  %".42" = bitcast [4 x i8]* %".40" to i8*
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".42", i32 %".39")
  br label %"if.end.2"
if.end.2:
  %".45" = load double, double* %"d_tmp"
  %".46" = load double, double* %"z_tmp"
  %".47" = fcmp ogt double %".45", %".46"
  br i1 %".47", label %"if.then.3", label %"if.else.1"
if.then.3:
  %".49" = load i32, i32* @"j"
  %".50" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".50"
  %".52" = bitcast [4 x i8]* %".50" to i8*
  %".53" = call i32 (i8*, ...) @"printf"(i8* %".52", i32 %".49")
  br label %"if.end.3"
if.else.1:
  %".55" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".55"
  %".57" = bitcast [4 x i8]* %".55" to i8*
  %".58" = call i32 (i8*, ...) @"printf"(i8* %".57", i32 22)
  br label %"if.end.3"
if.end.3:
  %".60" = load double, double* %"d_tmp"
  %".61" = load double, double* %"z_tmp"
  %".62" = fcmp one double %".60", %".61"
  br i1 %".62", label %"if.then.4", label %"if.end.4"
if.then.4:
  %".64" = load i32, i32* @"j"
  %".65" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".65"
  %".67" = bitcast [4 x i8]* %".65" to i8*
  %".68" = call i32 (i8*, ...) @"printf"(i8* %".67", i32 %".64")
  br label %"if.end.4"
if.end.4:
  %".70" = load double, double* %"d_tmp"
  %".71" = load double, double* %"z_tmp"
  %".72" = fcmp oeq double %".70", %".71"
  br i1 %".72", label %"if.then.5", label %"if.else.2"
if.then.5:
  %".74" = load i32, i32* @"j"
  %".75" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".75"
  %".77" = bitcast [4 x i8]* %".75" to i8*
  %".78" = call i32 (i8*, ...) @"printf"(i8* %".77", i32 %".74")
  br label %"if.end.5"
if.else.2:
  %".80" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".80"
  %".82" = bitcast [4 x i8]* %".80" to i8*
  %".83" = call i32 (i8*, ...) @"printf"(i8* %".82", i32 22)
  br label %"if.end.5"
if.end.5:
  %".85" = load i32, i32* %"x_tmp"
  %".86" = load double, double* %"z_tmp"
  %".87" = sitofp i32 %".85" to double
  %".88" = fcmp one double %".87", %".86"
  br i1 %".88", label %"if.then.6", label %"if.end.6"
if.then.6:
  %".90" = load i32, i32* @"j"
  %".91" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".91"
  %".93" = bitcast [4 x i8]* %".91" to i8*
  %".94" = call i32 (i8*, ...) @"printf"(i8* %".93", i32 %".90")
  br label %"if.end.6"
if.end.6:
  %".96" = load i32, i32* %"x_tmp"
  %".97" = load double, double* %"z_tmp"
  %".98" = sitofp i32 %".96" to double
  %".99" = fcmp oeq double %".98", %".97"
  br i1 %".99", label %"if.then.7", label %"if.else.3"
if.then.7:
  %".101" = load i32, i32* @"j"
  %".102" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".102"
  %".104" = bitcast [4 x i8]* %".102" to i8*
  %".105" = call i32 (i8*, ...) @"printf"(i8* %".104", i32 %".101")
  br label %"if.end.7"
if.else.3:
  %".107" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".107"
  %".109" = bitcast [4 x i8]* %".107" to i8*
  %".110" = call i32 (i8*, ...) @"printf"(i8* %".109", i32 22)
  br label %"if.end.7"
if.end.7:
  %".112" = load double, double* %"d_tmp"
  %".113" = load i32, i32* %"x_tmp"
  %".114" = sitofp i32 %".113" to double
  %".115" = fcmp ogt double %".112", %".114"
  br i1 %".115", label %"if.then.8", label %"if.end.8"
if.then.8:
  %".117" = load i32, i32* @"j"
  %".118" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".118"
  %".120" = bitcast [4 x i8]* %".118" to i8*
  %".121" = call i32 (i8*, ...) @"printf"(i8* %".120", i32 %".117")
  br label %"if.end.8"
if.end.8:
  %".123" = load double, double* %"z_tmp"
  %".124" = load i32, i32* %"y_tmp"
  %".125" = sitofp i32 %".124" to double
  %".126" = fcmp ogt double %".123", %".125"
  br i1 %".126", label %"if.then.9", label %"if.end.9"
if.then.9:
  %".128" = load i32, i32* @"j"
  %".129" = alloca [4 x i8]
  store [4 x i8] c"%d\0a\00", [4 x i8]* %".129"
  %".131" = bitcast [4 x i8]* %".129" to i8*
  %".132" = call i32 (i8*, ...) @"printf"(i8* %".131", i32 %".128")
  br label %"if.end.9"
if.end.9:
  ret void
}
