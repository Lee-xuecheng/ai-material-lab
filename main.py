"""
AI材料科学实验平台主程序
"""
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_processing import load_material_data, clean_data

def main():
    print("=" * 50)
    print("AI材料科学实验平台")
    print("=" * 50)
    
    # 示例：加载数据
    print("1. 数据模块测试...")
    
    # 这里可以添加实际的数据处理流程
    # data = load_material_data("data/raw/materials.csv")
    # processed_data = clean_data(data)
    
    print("✅ 程序启动成功！")
    print("提示：请编辑 main.py 添加你的实验代码")

if __name__ == "__main__":
    main()