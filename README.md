# learning-log

这是我的第一个代码仓库。它不装任何项目，只记录"我每天学了什么"。

## 第 1 天：2026-11-17 ✅ 完成

| # | 验收项 | 状态 |
| --- | --- | --- |
| 1 | Python 3.14.7 | ✅ |
| 2 | Git 2.56.1，`git --version` 有输出 | ✅ |
| 3 | VS Code 1.146.0，`code --version` 有输出 | ✅ |
| 4 | 建好虚拟环境，提示符前出现 `(.venv)` | ✅ |
| 5 | `python hello.py` 跑出结果 | ✅ |
| 6 | 推上 GitHub，网页上能看到 hello.py | ✅ https://github.com/SWX317/learning-log |

第一次提交：`8ace074`，branch `main`，4 个文件。

## 每次开工的正确姿势

```bash
cd ~/Doubao/chats/2026-11-17/new-chat/learning-log
pwd      # 确认在不在对的地方
ls       # 确认 hello.py 在不在
source .venv/Scripts/activate   # 提示符出现 (.venv) 才算好
```

三个注意点（都是第 1 天真实踩过的）：

- **别手打带中文的路径**：粘进 Git Bash 会被转码，看着一样但进不去。用 `~` 写法。
- **`cd` 后面必须有空格**，`cd~/...` 会被当成一个命令名。
- **敲命令前切英文输入法**：`.` 和 `--` 被换成全角符号就会报奇怪的错。

## 网络与推送（重要）

这台机器直连 `github.com:443` 不通，必须开代理。已经配好：

```bash
git config --global --get http.proxy   # 应输出 http://127.0.0.1:1088
```

- 开梯子时：上面这条直接就能 push
- 关梯子后如果 push 失败：先开梯子；或者临时去掉代理 `git config --global --unset http.proxy`
- 备用通道：`C:\Users\宋汶轩\.ssh\config` 里已把 `github.com` 指向 `ssh.github.com:443`（这条链路不挂梯子也是通的），将来可以改用 SSH

## 日常节奏

每天三条，缺一条都不算完成：

1. `git add .` + `git commit -m "今天学了什么"`（提交信息写内容，不要写 `update`）
2. 往 `卡点.md` 追加一行：日期 + 报错原文 + 怎么解的
3. 在下面「明天第一件事」里写一行

## 明天第一件事

（每天开工前先看这一行）

- 2026-11-18：看 MIT《Missing Semester》第 1 讲（Shell 入门），网址 https://missing-semester-cn.github.io/ ，边看边在 Git Bash 里敲。
