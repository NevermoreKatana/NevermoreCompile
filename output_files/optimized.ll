; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-pc-linux-gnu"

@j = local_unnamed_addr global i32 0

define void @main() local_unnamed_addr {
entry.main:
  store i32 1, i32* @j, align 4
  %x = alloca i32, align 4
  store i32 0, i32* %x, align 4
  %y = alloca i32, align 4
  store i32 2, i32* %y, align 4
  %d = alloca double, align 8
  store double 2.300000e+00, double* %d, align 8
  %z = alloca double, align 8
  store double 3.300000e+00, double* %z, align 8
  br i1 true, label %if.then, label %entry.main.if.end_crit_edge

entry.main.if.end_crit_edge:                      ; preds = %entry.main
  br label %if.end

if.then:                                          ; preds = %entry.main
  %.12 = alloca [4 x i8], align 1
  %.12.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.12, i64 0, i64 0
  store i8 37, i8* %.12.repack, align 1
  %.12.repack40 = getelementptr inbounds [4 x i8], [4 x i8]* %.12, i64 0, i64 1
  store i8 100, i8* %.12.repack40, align 1
  %.12.repack41 = getelementptr inbounds [4 x i8], [4 x i8]* %.12, i64 0, i64 2
  store i8 10, i8* %.12.repack41, align 1
  %.12.repack42 = getelementptr inbounds [4 x i8], [4 x i8]* %.12, i64 0, i64 3
  store i8 0, i8* %.12.repack42, align 1
  %.15 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.12.repack, i32 1)
  br label %if.end

if.end:                                           ; preds = %entry.main.if.end_crit_edge, %if.then
  br i1 false, label %if.then.1, label %if.else

if.then.1:                                        ; preds = %if.end
  br label %if.end.1

if.else:                                          ; preds = %if.end
  %.27 = alloca [4 x i8], align 1
  %.27.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.27, i64 0, i64 0
  store i8 37, i8* %.27.repack, align 1
  %.27.repack1 = getelementptr inbounds [4 x i8], [4 x i8]* %.27, i64 0, i64 1
  store i8 100, i8* %.27.repack1, align 1
  %.27.repack2 = getelementptr inbounds [4 x i8], [4 x i8]* %.27, i64 0, i64 2
  store i8 10, i8* %.27.repack2, align 1
  %.27.repack3 = getelementptr inbounds [4 x i8], [4 x i8]* %.27, i64 0, i64 3
  store i8 0, i8* %.27.repack3, align 1
  %.30 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.27.repack, i32 22)
  br label %if.end.1

if.end.1:                                         ; preds = %if.else, %if.then.1
  br i1 true, label %if.then.2, label %if.end.1.if.end.2_crit_edge

if.end.1.if.end.2_crit_edge:                      ; preds = %if.end.1
  br label %if.end.2

if.then.2:                                        ; preds = %if.end.1
  %.36 = load i32, i32* @j, align 4
  %.37 = alloca [4 x i8], align 1
  %.37.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.37, i64 0, i64 0
  store i8 37, i8* %.37.repack, align 1
  %.37.repack34 = getelementptr inbounds [4 x i8], [4 x i8]* %.37, i64 0, i64 1
  store i8 100, i8* %.37.repack34, align 1
  %.37.repack35 = getelementptr inbounds [4 x i8], [4 x i8]* %.37, i64 0, i64 2
  store i8 10, i8* %.37.repack35, align 1
  %.37.repack36 = getelementptr inbounds [4 x i8], [4 x i8]* %.37, i64 0, i64 3
  store i8 0, i8* %.37.repack36, align 1
  %.40 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.37.repack, i32 %.36)
  br label %if.end.2

if.end.2:                                         ; preds = %if.end.1.if.end.2_crit_edge, %if.then.2
  br i1 false, label %if.then.3, label %if.else.1

if.then.3:                                        ; preds = %if.end.2
  br label %if.end.3

if.else.1:                                        ; preds = %if.end.2
  %.52 = alloca [4 x i8], align 1
  %.52.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.52, i64 0, i64 0
  store i8 37, i8* %.52.repack, align 1
  %.52.repack4 = getelementptr inbounds [4 x i8], [4 x i8]* %.52, i64 0, i64 1
  store i8 100, i8* %.52.repack4, align 1
  %.52.repack5 = getelementptr inbounds [4 x i8], [4 x i8]* %.52, i64 0, i64 2
  store i8 10, i8* %.52.repack5, align 1
  %.52.repack6 = getelementptr inbounds [4 x i8], [4 x i8]* %.52, i64 0, i64 3
  store i8 0, i8* %.52.repack6, align 1
  %.55 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.52.repack, i32 22)
  br label %if.end.3

if.end.3:                                         ; preds = %if.else.1, %if.then.3
  br i1 false, label %if.end.3.if.end.4_crit_edge, label %if.then.4

if.end.3.if.end.4_crit_edge:                      ; preds = %if.end.3
  br label %if.end.4

if.then.4:                                        ; preds = %if.end.3
  %.61 = load i32, i32* @j, align 4
  %.62 = alloca [4 x i8], align 1
  %.62.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.62, i64 0, i64 0
  store i8 37, i8* %.62.repack, align 1
  %.62.repack28 = getelementptr inbounds [4 x i8], [4 x i8]* %.62, i64 0, i64 1
  store i8 100, i8* %.62.repack28, align 1
  %.62.repack29 = getelementptr inbounds [4 x i8], [4 x i8]* %.62, i64 0, i64 2
  store i8 10, i8* %.62.repack29, align 1
  %.62.repack30 = getelementptr inbounds [4 x i8], [4 x i8]* %.62, i64 0, i64 3
  store i8 0, i8* %.62.repack30, align 1
  %.65 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.62.repack, i32 %.61)
  br label %if.end.4

if.end.4:                                         ; preds = %if.end.3.if.end.4_crit_edge, %if.then.4
  br i1 false, label %if.then.5, label %if.else.2

if.then.5:                                        ; preds = %if.end.4
  br label %if.end.5

if.else.2:                                        ; preds = %if.end.4
  %.77 = alloca [4 x i8], align 1
  %.77.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.77, i64 0, i64 0
  store i8 37, i8* %.77.repack, align 1
  %.77.repack7 = getelementptr inbounds [4 x i8], [4 x i8]* %.77, i64 0, i64 1
  store i8 100, i8* %.77.repack7, align 1
  %.77.repack8 = getelementptr inbounds [4 x i8], [4 x i8]* %.77, i64 0, i64 2
  store i8 10, i8* %.77.repack8, align 1
  %.77.repack9 = getelementptr inbounds [4 x i8], [4 x i8]* %.77, i64 0, i64 3
  store i8 0, i8* %.77.repack9, align 1
  %.80 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.77.repack, i32 22)
  br label %if.end.5

if.end.5:                                         ; preds = %if.else.2, %if.then.5
  br i1 false, label %if.end.5.if.end.6_crit_edge, label %if.then.6

if.end.5.if.end.6_crit_edge:                      ; preds = %if.end.5
  br label %if.end.6

if.then.6:                                        ; preds = %if.end.5
  %.87 = load i32, i32* @j, align 4
  %.88 = alloca [4 x i8], align 1
  %.88.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.88, i64 0, i64 0
  store i8 37, i8* %.88.repack, align 1
  %.88.repack22 = getelementptr inbounds [4 x i8], [4 x i8]* %.88, i64 0, i64 1
  store i8 100, i8* %.88.repack22, align 1
  %.88.repack23 = getelementptr inbounds [4 x i8], [4 x i8]* %.88, i64 0, i64 2
  store i8 10, i8* %.88.repack23, align 1
  %.88.repack24 = getelementptr inbounds [4 x i8], [4 x i8]* %.88, i64 0, i64 3
  store i8 0, i8* %.88.repack24, align 1
  %.91 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.88.repack, i32 %.87)
  br label %if.end.6

if.end.6:                                         ; preds = %if.end.5.if.end.6_crit_edge, %if.then.6
  br i1 false, label %if.then.7, label %if.else.3

if.then.7:                                        ; preds = %if.end.6
  br label %if.end.7

if.else.3:                                        ; preds = %if.end.6
  %.104 = alloca [4 x i8], align 1
  %.104.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.104, i64 0, i64 0
  store i8 37, i8* %.104.repack, align 1
  %.104.repack10 = getelementptr inbounds [4 x i8], [4 x i8]* %.104, i64 0, i64 1
  store i8 100, i8* %.104.repack10, align 1
  %.104.repack11 = getelementptr inbounds [4 x i8], [4 x i8]* %.104, i64 0, i64 2
  store i8 10, i8* %.104.repack11, align 1
  %.104.repack12 = getelementptr inbounds [4 x i8], [4 x i8]* %.104, i64 0, i64 3
  store i8 0, i8* %.104.repack12, align 1
  %.107 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.104.repack, i32 22)
  br label %if.end.7

if.end.7:                                         ; preds = %if.else.3, %if.then.7
  br i1 true, label %if.then.8, label %if.end.7.if.end.8_crit_edge

if.end.7.if.end.8_crit_edge:                      ; preds = %if.end.7
  br label %if.end.8

if.then.8:                                        ; preds = %if.end.7
  %.114 = load i32, i32* @j, align 4
  %.115 = alloca [4 x i8], align 1
  %.115.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.115, i64 0, i64 0
  store i8 37, i8* %.115.repack, align 1
  %.115.repack16 = getelementptr inbounds [4 x i8], [4 x i8]* %.115, i64 0, i64 1
  store i8 100, i8* %.115.repack16, align 1
  %.115.repack17 = getelementptr inbounds [4 x i8], [4 x i8]* %.115, i64 0, i64 2
  store i8 10, i8* %.115.repack17, align 1
  %.115.repack18 = getelementptr inbounds [4 x i8], [4 x i8]* %.115, i64 0, i64 3
  store i8 0, i8* %.115.repack18, align 1
  %.118 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.115.repack, i32 %.114)
  br label %if.end.8

if.end.8:                                         ; preds = %if.end.7.if.end.8_crit_edge, %if.then.8
  br i1 true, label %if.then.9, label %if.end.8.if.end.9_crit_edge

if.end.8.if.end.9_crit_edge:                      ; preds = %if.end.8
  br label %if.end.9

if.then.9:                                        ; preds = %if.end.8
  %.125 = load i32, i32* @j, align 4
  %.126 = alloca [4 x i8], align 1
  %.126.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.126, i64 0, i64 0
  store i8 37, i8* %.126.repack, align 1
  %.126.repack13 = getelementptr inbounds [4 x i8], [4 x i8]* %.126, i64 0, i64 1
  store i8 100, i8* %.126.repack13, align 1
  %.126.repack14 = getelementptr inbounds [4 x i8], [4 x i8]* %.126, i64 0, i64 2
  store i8 10, i8* %.126.repack14, align 1
  %.126.repack15 = getelementptr inbounds [4 x i8], [4 x i8]* %.126, i64 0, i64 3
  store i8 0, i8* %.126.repack15, align 1
  %.129 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.126.repack, i32 %.125)
  br label %if.end.9

if.end.9:                                         ; preds = %if.end.8.if.end.9_crit_edge, %if.then.9
  call void @test(i32 1, i32 2, double 2.200000e+00, double 3.200000e+00)
  ret void
}

declare i32 @printf(i8*, ...) local_unnamed_addr

define void @test(i32 %.1, i32 %.2, double %.3, double %.4) local_unnamed_addr {
entry:
  %x_tmp = alloca i32, align 4
  store i32 %.1, i32* %x_tmp, align 4
  %y_tmp = alloca i32, align 4
  store i32 %.2, i32* %y_tmp, align 4
  %d_tmp = alloca double, align 8
  store double %.3, double* %d_tmp, align 8
  %z_tmp = alloca double, align 8
  store double %.4, double* %z_tmp, align 8
  %.12 = icmp slt i32 %.1, %.2
  br i1 %.12, label %if.then, label %if.end

if.then:                                          ; preds = %entry
  %.14 = load i32, i32* @j, align 4
  %.15 = alloca [4 x i8], align 1
  %.15.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.15, i64 0, i64 0
  store i8 37, i8* %.15.repack, align 1
  %.15.repack40 = getelementptr inbounds [4 x i8], [4 x i8]* %.15, i64 0, i64 1
  store i8 100, i8* %.15.repack40, align 1
  %.15.repack41 = getelementptr inbounds [4 x i8], [4 x i8]* %.15, i64 0, i64 2
  store i8 10, i8* %.15.repack41, align 1
  %.15.repack42 = getelementptr inbounds [4 x i8], [4 x i8]* %.15, i64 0, i64 3
  store i8 0, i8* %.15.repack42, align 1
  %.18 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.15.repack, i32 %.14)
  br label %if.end

if.end:                                           ; preds = %if.then, %entry
  %.22 = icmp sgt i32 %.1, %.2
  br i1 %.22, label %if.then.1, label %if.else

if.then.1:                                        ; preds = %if.end
  %.24 = load i32, i32* @j, align 4
  %.25 = alloca [4 x i8], align 1
  %.25.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.25, i64 0, i64 0
  store i8 37, i8* %.25.repack, align 1
  %.25.repack37 = getelementptr inbounds [4 x i8], [4 x i8]* %.25, i64 0, i64 1
  store i8 100, i8* %.25.repack37, align 1
  %.25.repack38 = getelementptr inbounds [4 x i8], [4 x i8]* %.25, i64 0, i64 2
  store i8 10, i8* %.25.repack38, align 1
  %.25.repack39 = getelementptr inbounds [4 x i8], [4 x i8]* %.25, i64 0, i64 3
  store i8 0, i8* %.25.repack39, align 1
  %.28 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.25.repack, i32 %.24)
  br label %if.end.1

if.else:                                          ; preds = %if.end
  %.30 = alloca [4 x i8], align 1
  %.30.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.30, i64 0, i64 0
  store i8 37, i8* %.30.repack, align 1
  %.30.repack1 = getelementptr inbounds [4 x i8], [4 x i8]* %.30, i64 0, i64 1
  store i8 100, i8* %.30.repack1, align 1
  %.30.repack2 = getelementptr inbounds [4 x i8], [4 x i8]* %.30, i64 0, i64 2
  store i8 10, i8* %.30.repack2, align 1
  %.30.repack3 = getelementptr inbounds [4 x i8], [4 x i8]* %.30, i64 0, i64 3
  store i8 0, i8* %.30.repack3, align 1
  %.33 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.30.repack, i32 22)
  br label %if.end.1

if.end.1:                                         ; preds = %if.else, %if.then.1
  %.37 = fcmp olt double %.3, %.4
  br i1 %.37, label %if.then.2, label %if.end.2

if.then.2:                                        ; preds = %if.end.1
  %.39 = load i32, i32* @j, align 4
  %.40 = alloca [4 x i8], align 1
  %.40.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.40, i64 0, i64 0
  store i8 37, i8* %.40.repack, align 1
  %.40.repack34 = getelementptr inbounds [4 x i8], [4 x i8]* %.40, i64 0, i64 1
  store i8 100, i8* %.40.repack34, align 1
  %.40.repack35 = getelementptr inbounds [4 x i8], [4 x i8]* %.40, i64 0, i64 2
  store i8 10, i8* %.40.repack35, align 1
  %.40.repack36 = getelementptr inbounds [4 x i8], [4 x i8]* %.40, i64 0, i64 3
  store i8 0, i8* %.40.repack36, align 1
  %.43 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.40.repack, i32 %.39)
  br label %if.end.2

if.end.2:                                         ; preds = %if.then.2, %if.end.1
  %.47 = fcmp ogt double %.3, %.4
  br i1 %.47, label %if.then.3, label %if.else.1

if.then.3:                                        ; preds = %if.end.2
  %.49 = load i32, i32* @j, align 4
  %.50 = alloca [4 x i8], align 1
  %.50.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.50, i64 0, i64 0
  store i8 37, i8* %.50.repack, align 1
  %.50.repack31 = getelementptr inbounds [4 x i8], [4 x i8]* %.50, i64 0, i64 1
  store i8 100, i8* %.50.repack31, align 1
  %.50.repack32 = getelementptr inbounds [4 x i8], [4 x i8]* %.50, i64 0, i64 2
  store i8 10, i8* %.50.repack32, align 1
  %.50.repack33 = getelementptr inbounds [4 x i8], [4 x i8]* %.50, i64 0, i64 3
  store i8 0, i8* %.50.repack33, align 1
  %.53 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.50.repack, i32 %.49)
  br label %if.end.3

if.else.1:                                        ; preds = %if.end.2
  %.55 = alloca [4 x i8], align 1
  %.55.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.55, i64 0, i64 0
  store i8 37, i8* %.55.repack, align 1
  %.55.repack4 = getelementptr inbounds [4 x i8], [4 x i8]* %.55, i64 0, i64 1
  store i8 100, i8* %.55.repack4, align 1
  %.55.repack5 = getelementptr inbounds [4 x i8], [4 x i8]* %.55, i64 0, i64 2
  store i8 10, i8* %.55.repack5, align 1
  %.55.repack6 = getelementptr inbounds [4 x i8], [4 x i8]* %.55, i64 0, i64 3
  store i8 0, i8* %.55.repack6, align 1
  %.58 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.55.repack, i32 22)
  br label %if.end.3

if.end.3:                                         ; preds = %if.else.1, %if.then.3
  %.62 = fcmp ueq double %.3, %.4
  br i1 %.62, label %if.end.4, label %if.then.4

if.then.4:                                        ; preds = %if.end.3
  %.64 = load i32, i32* @j, align 4
  %.65 = alloca [4 x i8], align 1
  %.65.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.65, i64 0, i64 0
  store i8 37, i8* %.65.repack, align 1
  %.65.repack28 = getelementptr inbounds [4 x i8], [4 x i8]* %.65, i64 0, i64 1
  store i8 100, i8* %.65.repack28, align 1
  %.65.repack29 = getelementptr inbounds [4 x i8], [4 x i8]* %.65, i64 0, i64 2
  store i8 10, i8* %.65.repack29, align 1
  %.65.repack30 = getelementptr inbounds [4 x i8], [4 x i8]* %.65, i64 0, i64 3
  store i8 0, i8* %.65.repack30, align 1
  %.68 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.65.repack, i32 %.64)
  br label %if.end.4

if.end.4:                                         ; preds = %if.then.4, %if.end.3
  %.72 = fcmp oeq double %.3, %.4
  br i1 %.72, label %if.then.5, label %if.else.2

if.then.5:                                        ; preds = %if.end.4
  %.74 = load i32, i32* @j, align 4
  %.75 = alloca [4 x i8], align 1
  %.75.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.75, i64 0, i64 0
  store i8 37, i8* %.75.repack, align 1
  %.75.repack25 = getelementptr inbounds [4 x i8], [4 x i8]* %.75, i64 0, i64 1
  store i8 100, i8* %.75.repack25, align 1
  %.75.repack26 = getelementptr inbounds [4 x i8], [4 x i8]* %.75, i64 0, i64 2
  store i8 10, i8* %.75.repack26, align 1
  %.75.repack27 = getelementptr inbounds [4 x i8], [4 x i8]* %.75, i64 0, i64 3
  store i8 0, i8* %.75.repack27, align 1
  %.78 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.75.repack, i32 %.74)
  br label %if.end.5

if.else.2:                                        ; preds = %if.end.4
  %.80 = alloca [4 x i8], align 1
  %.80.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.80, i64 0, i64 0
  store i8 37, i8* %.80.repack, align 1
  %.80.repack7 = getelementptr inbounds [4 x i8], [4 x i8]* %.80, i64 0, i64 1
  store i8 100, i8* %.80.repack7, align 1
  %.80.repack8 = getelementptr inbounds [4 x i8], [4 x i8]* %.80, i64 0, i64 2
  store i8 10, i8* %.80.repack8, align 1
  %.80.repack9 = getelementptr inbounds [4 x i8], [4 x i8]* %.80, i64 0, i64 3
  store i8 0, i8* %.80.repack9, align 1
  %.83 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.80.repack, i32 22)
  br label %if.end.5

if.end.5:                                         ; preds = %if.else.2, %if.then.5
  %.87 = sitofp i32 %.1 to double
  %.88 = fcmp ueq double %.4, %.87
  br i1 %.88, label %if.end.6, label %if.then.6

if.then.6:                                        ; preds = %if.end.5
  %.90 = load i32, i32* @j, align 4
  %.91 = alloca [4 x i8], align 1
  %.91.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.91, i64 0, i64 0
  store i8 37, i8* %.91.repack, align 1
  %.91.repack22 = getelementptr inbounds [4 x i8], [4 x i8]* %.91, i64 0, i64 1
  store i8 100, i8* %.91.repack22, align 1
  %.91.repack23 = getelementptr inbounds [4 x i8], [4 x i8]* %.91, i64 0, i64 2
  store i8 10, i8* %.91.repack23, align 1
  %.91.repack24 = getelementptr inbounds [4 x i8], [4 x i8]* %.91, i64 0, i64 3
  store i8 0, i8* %.91.repack24, align 1
  %.94 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.91.repack, i32 %.90)
  br label %if.end.6

if.end.6:                                         ; preds = %if.then.6, %if.end.5
  %.99 = fcmp oeq double %.4, %.87
  br i1 %.99, label %if.then.7, label %if.else.3

if.then.7:                                        ; preds = %if.end.6
  %.101 = load i32, i32* @j, align 4
  %.102 = alloca [4 x i8], align 1
  %.102.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.102, i64 0, i64 0
  store i8 37, i8* %.102.repack, align 1
  %.102.repack19 = getelementptr inbounds [4 x i8], [4 x i8]* %.102, i64 0, i64 1
  store i8 100, i8* %.102.repack19, align 1
  %.102.repack20 = getelementptr inbounds [4 x i8], [4 x i8]* %.102, i64 0, i64 2
  store i8 10, i8* %.102.repack20, align 1
  %.102.repack21 = getelementptr inbounds [4 x i8], [4 x i8]* %.102, i64 0, i64 3
  store i8 0, i8* %.102.repack21, align 1
  %.105 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.102.repack, i32 %.101)
  br label %if.end.7

if.else.3:                                        ; preds = %if.end.6
  %.107 = alloca [4 x i8], align 1
  %.107.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.107, i64 0, i64 0
  store i8 37, i8* %.107.repack, align 1
  %.107.repack10 = getelementptr inbounds [4 x i8], [4 x i8]* %.107, i64 0, i64 1
  store i8 100, i8* %.107.repack10, align 1
  %.107.repack11 = getelementptr inbounds [4 x i8], [4 x i8]* %.107, i64 0, i64 2
  store i8 10, i8* %.107.repack11, align 1
  %.107.repack12 = getelementptr inbounds [4 x i8], [4 x i8]* %.107, i64 0, i64 3
  store i8 0, i8* %.107.repack12, align 1
  %.110 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.107.repack, i32 22)
  br label %if.end.7

if.end.7:                                         ; preds = %if.else.3, %if.then.7
  %.115 = fcmp ogt double %.3, %.87
  br i1 %.115, label %if.then.8, label %if.end.8

if.then.8:                                        ; preds = %if.end.7
  %.117 = load i32, i32* @j, align 4
  %.118 = alloca [4 x i8], align 1
  %.118.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.118, i64 0, i64 0
  store i8 37, i8* %.118.repack, align 1
  %.118.repack16 = getelementptr inbounds [4 x i8], [4 x i8]* %.118, i64 0, i64 1
  store i8 100, i8* %.118.repack16, align 1
  %.118.repack17 = getelementptr inbounds [4 x i8], [4 x i8]* %.118, i64 0, i64 2
  store i8 10, i8* %.118.repack17, align 1
  %.118.repack18 = getelementptr inbounds [4 x i8], [4 x i8]* %.118, i64 0, i64 3
  store i8 0, i8* %.118.repack18, align 1
  %.121 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.118.repack, i32 %.117)
  br label %if.end.8

if.end.8:                                         ; preds = %if.then.8, %if.end.7
  %.125 = sitofp i32 %.2 to double
  %.126 = fcmp ogt double %.4, %.125
  br i1 %.126, label %if.then.9, label %if.end.9

if.then.9:                                        ; preds = %if.end.8
  %.128 = load i32, i32* @j, align 4
  %.129 = alloca [4 x i8], align 1
  %.129.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.129, i64 0, i64 0
  store i8 37, i8* %.129.repack, align 1
  %.129.repack13 = getelementptr inbounds [4 x i8], [4 x i8]* %.129, i64 0, i64 1
  store i8 100, i8* %.129.repack13, align 1
  %.129.repack14 = getelementptr inbounds [4 x i8], [4 x i8]* %.129, i64 0, i64 2
  store i8 10, i8* %.129.repack14, align 1
  %.129.repack15 = getelementptr inbounds [4 x i8], [4 x i8]* %.129, i64 0, i64 3
  store i8 0, i8* %.129.repack15, align 1
  %.132 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.129.repack, i32 %.128)
  br label %if.end.9

if.end.9:                                         ; preds = %if.then.9, %if.end.8
  ret void
}
