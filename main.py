from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    print("hello world")

    # 获取所有环境变量的字典
    env_vars = os.environ
    # 打印所有的键值对
    for key, value in env_vars.items():
        print(f"{key}: {value}")
