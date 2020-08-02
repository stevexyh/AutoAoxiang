# 翱翔门户自动登录脚本
## `AutoAoxiang`
## ⚠️警告: 仅可在确保自身情况正常、信息属实的情况下可使用此脚本, 一切后果由使用者自己承担, 作者概不负责。
## ⚠️警告: 若使用者健康情况异常, 务必立即停止使用此自动化脚本。

### `2020.2.21`
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
├── _config.yml
├── autoNCP.py
├── build_version
│   ├── autoNCP_mac_v1.0
│   └── autoNCP_win_v1.0.exe
├── functions
│   ├── __init__.py
│   ├── formatString.py
│   ├── getInfo.py
│   ├── location.py
│   └── loginAoxiang.py
└── requirements.txt
```

---

### 使用方法
### 1. `autoNCP.py` 自动提交疫情报告 
- 直接运行 `autoNCP.py`
- 如果缺少包, 运行 `pip install -r requirements.txt`
- 目前版本运行时不可关闭窗口, 否则程序终止  


### 2. `autoNCP.py` 服务器或后台定时提交疫情报告  
- `nohup ./autoNCP.py server &`  


---
### `CHANGELOG`
`2020.2.21`
`V1.2`
- 增加了缓存学号密码地点功能
- 此网页post不需要给汉字编码，修复了提交位置乱码的严重错误

`2020.2.17`
`V1.1`
- 增加定时自动运行功能
- 增加log功能

`2020.2.16`
`V1.0`
- 添加了颜色显示效果

---
## LICENSE
```
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
```

---
[GitHub](https://github.com/Steve-Xyh/AutoAoxiang)