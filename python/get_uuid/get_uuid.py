import uuid
import pyperclip


def generate_uuid():
    uuidv4 = uuid.uuid4()
    pyperclip.copy(str(uuidv4))
    print(f"UUID: {uuidv4}")


if __name__ == "__main__":
    generate_uuid()
