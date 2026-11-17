# hello.py —— 第 1 天唯一需要跑通的文件
# 用法：python hello.py

def greet(name: str) -> str:
    """一个函数：接收名字，返回一句话。"""
    return f"你好，{name}！从今天起，你是一个在写代码的人。"


def main() -> None:
    print(greet("同学"))  # 改成你自己的名字试试

    # 一个循环：重复三遍
    for day in range(1, 4):
        print(f"第 {day} 天：开始了")


if __name__ == "__main__":
    main()
