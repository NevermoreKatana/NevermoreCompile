; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-pc-linux-gnu"

define void @main() local_unnamed_addr {
entry.main:
  %.11.i = alloca [4 x i8], align 1
  %0 = getelementptr inbounds [4 x i8], [4 x i8]* %.11.i, i64 0, i64 0
  call void @llvm.lifetime.start.p0i8(i64 4, i8* nonnull %0)
  store i8 37, i8* %0, align 1
  %.11.i.repack1 = getelementptr inbounds [4 x i8], [4 x i8]* %.11.i, i64 0, i64 1
  store i8 100, i8* %.11.i.repack1, align 1
  %.11.i.repack2 = getelementptr inbounds [4 x i8], [4 x i8]* %.11.i, i64 0, i64 2
  store i8 10, i8* %.11.i.repack2, align 1
  %.11.i.repack3 = getelementptr inbounds [4 x i8], [4 x i8]* %.11.i, i64 0, i64 3
  store i8 0, i8* %.11.i.repack3, align 1
  %.14.i = call i32 (i8*, ...) @printf(i8* noundef nonnull %0, i32 4)
  call void @llvm.lifetime.end.p0i8(i64 4, i8* nonnull %0)
  ret void
}

declare i32 @printf(i8*, ...) local_unnamed_addr

define i32 @test6(i32 %.1, i32 %.2) local_unnamed_addr {
entry:
  %.8 = add i32 %.1, %.2
  %.11 = alloca [4 x i8], align 1
  %.11.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.11, i64 0, i64 0
  store i8 37, i8* %.11.repack, align 1
  %.11.repack1 = getelementptr inbounds [4 x i8], [4 x i8]* %.11, i64 0, i64 1
  store i8 100, i8* %.11.repack1, align 1
  %.11.repack2 = getelementptr inbounds [4 x i8], [4 x i8]* %.11, i64 0, i64 2
  store i8 10, i8* %.11.repack2, align 1
  %.11.repack3 = getelementptr inbounds [4 x i8], [4 x i8]* %.11, i64 0, i64 3
  store i8 0, i8* %.11.repack3, align 1
  %.14 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.11.repack, i32 %.8)
  ret i32 0
}

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.start.p0i8(i64 immarg, i8* nocapture) #0

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.end.p0i8(i64 immarg, i8* nocapture) #0

attributes #0 = { argmemonly nofree nosync nounwind willreturn }
