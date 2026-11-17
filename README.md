# learning-log

这是我的第一个代码仓库。它不装任何项目，只记录"我每天学了什么"。

## 当前进度（第 1 天）

- [x] 1. Python 3.14.7 已装
- [x] 2. Git 2.56.1 已装，`git --version` 有输出
- [x] 3. VS Code 1.146.0 已装，`code --version` 有输出
- [ ] 4. 建好虚拟环境，命令行前面出现 `(.venv)`
- [ ] 5. `python hello.py` 能跑出结果
- [ ] 6. 代码推上 GitHub，网页上能看到 hello.py

**第 6 条是今天唯一的真成果，前五条只是准备。**

## 命令清单 · Git Bash 版（你现在用的就是这个）

```bash
# 进到本文件夹
cd "/c/Users/宋汶轩/Doubao/chats/2026-11-17/new-chat/learning-log"

# 4. 建虚拟环境并激活（bash 语法，注意是 source）
python -m venv .venv
source .venv/Scripts/activate

# 换国内源，否则装包会超时
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 5. 跑通第一段代码
python hello.py
```

看到提示符前面出现 `(.venv)`，第 4 条就过了。

## 命令清单 · PowerShell 版（如果以后换成 PowerShell）

```powershell
cd "C:\Users\宋汶轩\Doubao\chats\2026-11-17\new-chat\learning-log"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
python hello.py
```

> 如果 PowerShell 报"无法加载文件，因为在此系统上禁止运行脚本"，执行这一行：
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

## 两套语法的对照（混用必报错）

| 动作 | Git Bash | PowerShell |
| --- | --- | --- |
| 盘符路径 | `/c/Users/...` | `C:\Users\...` |
| 激活虚拟环境 | `source .venv/Scripts/activate` | `.\.venv\Scripts\Activate.ps1` |
| 反斜杠写法 | 用 `/` | 用 `\` |

## 提交到 Git（第 1 天）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

git init
git status          # 确认列表里没有 .venv，只有 hello.py / README.md / 卡点.md / .gitignore
git add .
git commit -m "第1天：跑通 hello.py，环境搭好了"
git branch -M main
```

## 推上 GitHub（今天最后一关）

1. 打开 github.com 注册，进 Settings → Emails 确认邮箱已验证
2. 右上角 New repository → 名字填 `learning-log` → **不要勾 Add a README** → Create
3. 回到终端：

```bash
git remote add origin https://github.com/你的用户名/learning-log.git
git push -u origin main
```

第一次 push 会弹浏览窗口让你登录 GitHub，登录完就推上去了。
如果它让你在终端里输"密码"，那不是密码、是 token；换成浏览器登录最省事。

## 每天的习惯

1. `git commit`，提交信息写"今天学了什么"，不要写 `update`
2. 往 `卡点.md` 追加一行：时间 + 报错原文 + 怎么解的
3. 写一行明天第一件事

## 第 2 天

看 MIT《Missing Semester》2026 版第 1 讲（Shell 入门），边看边在 Git Bash 里敲。
网址：https://missing-semester-cn.github.io/
