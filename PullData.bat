@echo off
adb pull /sdcard/Data.txt .\Data.txt

python PullDataSendToGoogleSheet.py