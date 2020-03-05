# 翱翔门户自动登录脚本
## `AutoAoxiang`
## ⚠️警告: 仅可在确保自身情况正常、信息属实的情况下可使用此脚本, 一切后果由使用者自己承担, 作者概不负责。
## ⚠️警告: 若使用者健康情况异常, 务必立即停止使用此自动化脚本。

### `2020.2.21 by Steve X`
### `V1.2`
### - ⚠️修复了提交位置乱码的严重错误, 请所有人更新。

---
### 简介
- 用于自动完成一些用翱翔门户登录的内容
- 目前可实现自动提交每日疫情报告, 其他功能陆续开发中

### 文件结构
```
AutoAoxiang
├── README.md
├── autoNCP.py
├── functions
│   ├── formatString.py
│   └── loginAoxiang.py
└── packages.txt
```
---
### 使用方法
### 1. `autoNCP.py` 自动提交疫情报告 
- 直接运行 `autoNCP.py`
- 如果缺少包, 运行 `pip install -r packages.txt`
- 目前版本运行时不可关闭窗口, 否则程序终止  


### 2. `autoNCP.py` 服务器或后台定时提交疫情报告  
- `nohup ./autoNCP.py server &`  


---
### `CHANGELOG`
`2020.2.21 by Steve X`
`V1.2`
- 增加了缓存学号密码地点功能
- 此网页post不需要给汉字编码，修复了提交位置乱码的严重错误

`2020.2.17 by Steve X`
`V1.1`
- 增加定时自动运行功能
- 增加log功能

`2020.2.16 by Steve X`
`V1.0`
- 添加了颜色显示效果

---
`Developed by Steve X`
[GitHub](https://github.com/Steve-Xyh/AutoAoxiang)