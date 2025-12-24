import img2pdf
import os

def convert_image_to_pdf_img2pdf(image_path, pdf_path=None):
    """
    使用img2pdf库将图片转换为PDF
    保持原始图片质量，支持多种格式
    
    参数:
    image_path: 图片路径
    pdf_path: PDF保存路径（可选）
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(image_path):
            print(f"错误：文件 {image_path} 不存在")
            return False
        
        # 设置PDF保存路径
        if pdf_path is None:
            pdf_path = os.path.splitext(image_path)[0] + '.pdf'
        
        # 获取图片信息
        file_size = os.path.getsize(image_path) / 1024  # KB
        
        print(f"正在转换: {image_path}")
        print(f"文件大小: {file_size:.2f} KB")
        
        # 转换并保存PDF
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_path))
        
        pdf_size = os.path.getsize(pdf_path) / 1024  # KB
        print(f"转换成功！")
        print(f"PDF保存位置: {pdf_path}")
        print(f"PDF文件大小: {pdf_size:.2f} KB")
        return True
        
    except Exception as e:
        print(f"转换失败: {str(e)}")
        return False

# 使用示例
if __name__ == "__main__":
    image_path = r"D:\毕业证.jpg"
    convert_image_to_pdf_img2pdf(image_path)