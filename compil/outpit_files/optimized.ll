; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-pc-linux-gnu"

define void @main() local_unnamed_addr {
entry.main:
  tail call void @test1(i32 2, double 3.300000e+00)
  ret void
}

declare i32 @printf(i8*, ...) local_unnamed_addr

define void @test1(i32 %.1, double %.2) local_unnamed_addr {
entry:
  %x_tmp = alloca i32, align 4
  store i32 %.1, i32* %x_tmp, align 4
  %y_tmp = alloca double, align 8
  store double %.2, double* %y_tmp, align 8
  %.8 = mul i32 %.1, %.1
  %.10 = mul i32 %.8, %.1
  %.14 = mul i32 %.10, %.10
  %.16 = sitofp i32 %.14 to double
  %.17 = fdiv double %.16, %.2
  %.21 = sitofp i32 %.10 to double
  %.22 = fcmp olt double %.17, %.21
  br i1 %.22, label %if.then, label %if.else

if.then:                                          ; preds = %entry
  %.25 = alloca [4 x i8], align 1
  %.25.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.25, i64 0, i64 0
  store i8 37, i8* %.25.repack, align 1
  %.25.repack4 = getelementptr inbounds [4 x i8], [4 x i8]* %.25, i64 0, i64 1
  store i8 100, i8* %.25.repack4, align 1
  %.25.repack5 = getelementptr inbounds [4 x i8], [4 x i8]* %.25, i64 0, i64 2
  store i8 10, i8* %.25.repack5, align 1
  %.25.repack6 = getelementptr inbounds [4 x i8], [4 x i8]* %.25, i64 0, i64 3
  store i8 0, i8* %.25.repack6, align 1
  %.28 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.25.repack, i32 %.1)
  br label %if.end

if.else:                                          ; preds = %entry
  %.31 = alloca [4 x i8], align 1
  %.31.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.31, i64 0, i64 0
  store i8 37, i8* %.31.repack, align 1
  %.31.repack1 = getelementptr inbounds [4 x i8], [4 x i8]* %.31, i64 0, i64 1
  store i8 102, i8* %.31.repack1, align 1
  %.31.repack2 = getelementptr inbounds [4 x i8], [4 x i8]* %.31, i64 0, i64 2
  store i8 10, i8* %.31.repack2, align 1
  %.31.repack3 = getelementptr inbounds [4 x i8], [4 x i8]* %.31, i64 0, i64 3
  store i8 0, i8* %.31.repack3, align 1
  %.34 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.31.repack, double %.2)
  br label %if.end

if.end:                                           ; preds = %if.else, %if.then
  ret void
}
