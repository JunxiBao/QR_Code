import qrcode

# 获取用户输入的字符串
input_string = input("请输入要生成二维码的字符串：")

# 创建二维码
qr = qrcode.QRCode(
    version=1,  # 控制二维码的大小，范围是1到40，数字越大越复杂
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 控制二维码的容错率
    box_size=1,  # 控制二维码每个小格子的像素数
    border=0,  # 控制二维码边框的宽度（单位为格子数）
)

# 添加数据到二维码
qr.add_data(input_string)
qr.make(fit=True)

# 生成图片
img = qr.make_image(fill='yellow', back_color='blue')

# 保存图片文件
img.save("QR.png")

print("二维码已生成并保存在当前目录下的 'QR.png' 文件中。感谢使用！")
