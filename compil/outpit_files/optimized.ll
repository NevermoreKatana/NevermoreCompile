; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-pc-linux-gnu"

define void @main() local_unnamed_addr {
entry.main:
  %.5 = alloca [4 x i8], align 1
  %.5.repack = getelementptr inbounds [4 x i8], [4 x i8]* %.5, i64 0, i64 0
  store i8 37, i8* %.5.repack, align 1
  %.5.repack2 = getelementptr inbounds [4 x i8], [4 x i8]* %.5, i64 0, i64 1
  store i8 100, i8* %.5.repack2, align 1
  %.5.repack3 = getelementptr inbounds [4 x i8], [4 x i8]* %.5, i64 0, i64 2
  store i8 10, i8* %.5.repack3, align 1
  %.5.repack4 = getelementptr inbounds [4 x i8], [4 x i8]* %.5, i64 0, i64 3
  store i8 0, i8* %.5.repack4, align 1
  %.8 = call i32 (i8*, ...) @printf(i8* noundef nonnull %.5.repack, i32 1)
  ret void
}

declare i32 @printf(i8*, ...) local_unnamed_addr

define i32 @calculate(i32 %.1) local_unnamed_addr {
entry:
  %.5 = icmp slt i32 %.1, 2
  %. = zext i1 %.5 to i32
  ret i32 %.
}

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.start.p0i8(i64 immarg, i8* nocapture) #0

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.end.p0i8(i64 immarg, i8* nocapture) #0

attributes #0 = { argmemonly nofree nosync nounwind willreturn }
