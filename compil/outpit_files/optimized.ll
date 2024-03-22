; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-pc-linux-gnu"

define void @main() local_unnamed_addr {
entry.main:
  %x = alloca i32, align 4
  store i32 1, i32* %x, align 4
  %y = alloca double, align 8
  store double 2.300000e+00, double* %y, align 8
  %.13 = alloca [4 x i8], align 1
  %.13.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.13, i64 0, i64 0
  store i8 37, i8* %.13.repack, align 1
  %.13.repack1 = getelementptr inbounds [4 x i8], [4 x i8]* %.13, i64 0, i64 1
  store i8 100, i8* %.13.repack1, align 1
  %.13.repack2 = getelementptr inbounds [4 x i8], [4 x i8]* %.13, i64 0, i64 2
  store i8 10, i8* %.13.repack2, align 1
  %.13.repack3 = getelementptr inbounds [4 x i8], [4 x i8]* %.13, i64 0, i64 3
  store i8 0, i8* %.13.repack3, align 1
  %.16 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.13.repack, i32 48)
  %.31 = alloca [4 x i8], align 1
  %.31.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.31, i64 0, i64 0
  store i8 37, i8* %.31.repack, align 1
  %.31.repack4 = getelementptr inbounds [4 x i8], [4 x i8]* %.31, i64 0, i64 1
  store i8 100, i8* %.31.repack4, align 1
  %.31.repack5 = getelementptr inbounds [4 x i8], [4 x i8]* %.31, i64 0, i64 2
  store i8 10, i8* %.31.repack5, align 1
  %.31.repack6 = getelementptr inbounds [4 x i8], [4 x i8]* %.31, i64 0, i64 3
  store i8 0, i8* %.31.repack6, align 1
  %.34 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.31.repack, i32 3)
  %.46 = alloca [4 x i8], align 1
  %.46.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.46, i64 0, i64 0
  store i8 37, i8* %.46.repack, align 1
  %.46.repack7 = getelementptr inbounds [4 x i8], [4 x i8]* %.46, i64 0, i64 1
  store i8 100, i8* %.46.repack7, align 1
  %.46.repack8 = getelementptr inbounds [4 x i8], [4 x i8]* %.46, i64 0, i64 2
  store i8 10, i8* %.46.repack8, align 1
  %.46.repack9 = getelementptr inbounds [4 x i8], [4 x i8]* %.46, i64 0, i64 3
  store i8 0, i8* %.46.repack9, align 1
  %.49 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.46.repack, i32 54)
  %.69 = alloca [4 x i8], align 1
  %.69.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.69, i64 0, i64 0
  store i8 37, i8* %.69.repack, align 1
  %.69.repack10 = getelementptr inbounds [4 x i8], [4 x i8]* %.69, i64 0, i64 1
  store i8 102, i8* %.69.repack10, align 1
  %.69.repack11 = getelementptr inbounds [4 x i8], [4 x i8]* %.69, i64 0, i64 2
  store i8 10, i8* %.69.repack11, align 1
  %.69.repack12 = getelementptr inbounds [4 x i8], [4 x i8]* %.69, i64 0, i64 3
  store i8 0, i8* %.69.repack12, align 1
  %.72 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.69.repack, double 2.670000e+01)
  %.93 = alloca [4 x i8], align 1
  %.93.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.93, i64 0, i64 0
  store i8 37, i8* %.93.repack, align 1
  %.93.repack13 = getelementptr inbounds [4 x i8], [4 x i8]* %.93, i64 0, i64 1
  store i8 102, i8* %.93.repack13, align 1
  %.93.repack14 = getelementptr inbounds [4 x i8], [4 x i8]* %.93, i64 0, i64 2
  store i8 10, i8* %.93.repack14, align 1
  %.93.repack15 = getelementptr inbounds [4 x i8], [4 x i8]* %.93, i64 0, i64 3
  store i8 0, i8* %.93.repack15, align 1
  %.96 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.93.repack, double 0x403D35C28F5C28F5)
  ret void
}

declare i32 @printf(i8*, ...) local_unnamed_addr
