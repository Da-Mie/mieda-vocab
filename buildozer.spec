[app]
# 应用名称 (手机桌面上显示的)
title = 咩哒单词

# 包名 (建议全小写)
package.name = miedavocab
package.domain = org.mieda

# 源代码目录
source.dir = .

# 源代码包含的文件后缀 (这里包含了 ttf)
source.include_exts = py,png,jpg,kv,atlas,ttf,db,xlsx,xls,csv

# 版本号
version = 0.1

# -------------------------------------------------------------------
# 关键修改：依赖列表
# 已移除 pandas, numpy, sqlite3 (因为 sqlite3 是标准库，pandas 太大)
# 保留了 excel 处理所需的 openpyxl 和 xlrd
# -------------------------------------------------------------------
requirements = python3,kivy==2.3.0,kivymd,openpyxl,xlrd,openssl

# 屏幕方向
orientation = portrait
fullscreen = 0

# 启动图背景色 (靛青色)
android.presplash_color = #3F51B5

# -------------------------------------------------------------------
# 权限设置
# -------------------------------------------------------------------
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# API 设置 (适配较新的 Android)
android.api = 33
android.minapi = 21
android.ndk = 25b

# -------------------------------------------------------------------
# 架构设置 (非常重要！让 App 能在现代手机上运行)
# -------------------------------------------------------------------
android.archs = arm64-v8a, armeabi-v7a

# 是否使用私有存储
android.private_storage = True

# 入口点
android.entrypoint = org.kivy.android.PythonActivity

# 是否显示 Log (调试用)
[buildozer]
log_level = 2
warn_on_root = 0