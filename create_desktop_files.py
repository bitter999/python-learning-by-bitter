import os
import platform

def create_numbered_text_files_on_desktop(count: int = 10) -> None:
    """
    在桌面文件夹上创建指定数量的数字命名文本文件，例如 1.txt, 2.txt, ...

    参数:
        count: 要创建的文件数量，默认为 10
    """
    # 确定桌面路径
    system = platform.system()
    if system == "Windows":
        desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
    elif system == "Darwin":  # macOS
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    else:  # Linux 及其他类 Unix
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    # 确保桌面路径存在
    if not os.path.isdir(desktop):
        raise FileNotFoundError(f"桌面目录不存在: {desktop}")

    created_files = []

    for i in range(1, count + 1):
        filename = f"{i}.txt"
        filepath = os.path.join(desktop, filename)

        # 避免覆盖已有文件，可以选择追加内容或跳过
        # 此处选择跳过（不覆盖）
        if os.path.exists(filepath):
            print(f"⚠️ 跳过已存在的文件: {filepath}")
            continue

        try:
            # 创建一个空文本文件（也可以写入一些内容）
            with open(filepath, "w", encoding="utf-8") as f:
                # 写入简单的欢迎内容（可选）
                f.write(f"这是文件 {filename}\n创建时间: 自动生成\n")
            created_files.append(filepath)
            print(f"✅ 已创建: {filepath}")
        except Exception as e:
            print(f"❌ 创建文件失败 {filepath}: {e}")

    print(f"\n完成！共创建 {len(created_files)} 个文件。")


# 如果需要立即运行，取消下面的注释：
# if __name__ == "__main__":
#     create_numbered_text_files_on_desktop()