import os
import shutil

# 將 .gradle 的東西 轉成 .m2
os.chdir(os.getenv("UserProfile"))
os.getcwd()

# 例外偵測
GradleFileLocation = "./.gradle/caches/modules-2/files-2.1"
if not os.path.isdir(GradleFileLocation):
    print("Cann't find cache file data.")
    exit(0)

# 創建 .m2
M2Location = "./.m2/repository"
if os.path.isdir(M2Location):
    os.makedirs(M2Location, exist_ok=True)

# os.chdir(FileLocation)
List = os.listdir(GradleFileLocation)
while len(List) > 0:
    DirectoryName = List.pop()
    # print(DirectoryName)
    TempList = os.listdir(os.path.join(GradleFileLocation, DirectoryName))

    # 這裡假設只要有檔案
    # 就代表已碰到結尾
    # 可已開始搬檔案
    for i in range(len(TempList)):
        CurrentLocation = os.path.join(GradleFileLocation, DirectoryName, TempList[i])
        if os.path.isfile(CurrentLocation):
            SplitDir = DirectoryName.split("\\")

            PackageCopyLocation = ""
            ClassDir = SplitDir[0].split(".")
            for j in range(len(ClassDir)):
                PackageCopyLocation += ClassDir[j] + "/"
            PackageCopyLocation += SplitDir[1] + "/" + SplitDir[2]
            os.makedirs(os.path.join(M2Location, PackageCopyLocation), exist_ok=True)
            shutil.copyfile(CurrentLocation, 
                os.path.join(M2Location, PackageCopyLocation, TempList[i]))
                
        else:
            List.append(os.path.join(DirectoryName, TempList[i]))