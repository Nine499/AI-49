import uuid
import pyperclip


def generate_uuid():
    # 生成Version 4 UUID
    uuid_obj = uuid.uuid4()
    uuid_str = str(uuid_obj)

    # 写入剪贴板
    pyperclip.copy(uuid_str)

    # 输出结果
    print(f"UUID: {uuid_str}")


if __name__ == "__main__":
    generate_uuid()
