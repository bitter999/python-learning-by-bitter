import base64

# 1. 图片路径（可以是绝对路径或相对路径）
image_path = r"D:\Desktop\admin\learning-cyber\py-learing\my_project\images\test.png"

# 2. 以二进制读取图片文件
with open(image_path, "rb") as img_file:
    # 3. 将二进制数据编码为 Base64，再转成字符串
    base64_str = base64.b64encode(img_file.read()).decode("utf-8")

# 4. 构建 Data URL（如果是 PNG 图片，将 jpeg 改为 png）
data_url = f"data:image/jpeg;base64,{base64_str}"

# 5. 生成包含图片的 HTML 字符串
html = f'''
<html>
<body>
    <img src="{data_url}" alt="嵌入图片" width="400">
</body>
</html>
'''

# 6. 将 HTML 写入文件
with open("embedded_image.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ 已生成 embedded_image.html，图片已完全嵌入！")