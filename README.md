# LZU-RUNNING
兰大悦跑

`lzurun.py`中的`run()`函数可实现模拟悦跑
`student_id`参数是你的校园卡号
`distance`是你想跑的距离，单位千米
`run_time`是你想跑的时间，单位分钟

使用步骤
1. 刷脸
2. 打开兰大app，进入悦跑界面
3. 调用`run()`函数，为了全量模拟，函数会睡眠`run_time`分钟

程序在发包时缺少两个参数`sjxh`和`points`
`sjxh`是手机型号，属于敏感信息，故在程序中未实现
`points`是一个每5秒记录一次移动经纬度和时间戳的列表，由于当前(2022.6.10)服务器端存在不能读取过长列表的bug，暂时不填

本项目遵循`GPLv3`协议，二次开发请开源，或付费闭源
