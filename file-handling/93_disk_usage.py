import shutil

total, used, free = shutil.disk_usage("C:\\")

gb = 1024 ** 3

print("Total space:", round(total / gb, 2), "GB")
print("Used space:", round(used / gb, 2), "GB")
print("Free space:", round(free / gb, 2), "GB")