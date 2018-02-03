@echo off
adb pull /sdcard/Data.txt .\Data.txt

python ChangeDataToCSV.py
