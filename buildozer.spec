[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (used for APK package)
package.domain = org.test

# (str) Source code directory
source.dir = .

# (list) Source file extensions to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (str) Application entry point
entrypoint = main.py

# (list) List of requirements (comma-separated)
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Android NDK API to use
android.api = 33

# (str) Minimum Android API your APK will support
android.minapi = 21

# ✅ (str) Android build tools version (must match what’s installed in GitHub Actions)
android.build_tools = 34.0.0

# (str) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (optional)
# android.ndk_path = 

# (str) Android SDK directory (optional)
# android.sdk_path = 

# (list) Permissions for your app
android.permissions = CAMERA,INTERNET

# (bool) Copy libraries instead of linking (recommended for newer Android)
android.copy_libs = 1

# (bool) Enable Android logcat during debug
log_level = 2

# (str) Package format to generate: 'apk', 'aab', 'all'
android.packaging = apk

# (str) Output directory (default: bin)
# dist.dir =

# (bool) Compile with Cython
use_setup_py = 0
