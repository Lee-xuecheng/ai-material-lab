"""
AI材料科学数据处理模块
包含数据加载、清洗、特征工程等功能
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_material_data(file_path):
    """
    加载材料科学数据集
    """
    print(f"正在加载数据: {file_path}")
    try:
        data = pd.read_csv(file_path)
        print(f"数据加载成功！形状: {data.shape}")
        return data
    except Exception as e:
        print(f"数据加载失败: {e}")
        return None

def clean_data(df):
    """
    数据清洗：处理缺失值和异常值
    """
    print("开始数据清洗...")
    
    # 删除全为空的列
    df = df.dropna(axis=1, how='all')
    
    # 用中位数填充数值型缺失值
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"列 '{col}' 的缺失值已用中位数 {median_val:.2f} 填充")
    
    print(f"清洗后数据形状: {df.shape}")
    return df

def normalize_features(df, feature_columns):
    """
    特征标准化
    """
    print(f"正在标准化特征: {feature_columns}")
    
    scaler = StandardScaler()
    df[feature_columns] = scaler.fit_transform(df[feature_columns])
    
    print("特征标准化完成！")
    return df, scaler

if __name__ == "__main__":
    print("AI材料科学数据处理模块")
    print("=" * 40)
    
    # 示例用法
    # 假设有一个CSV文件
    # data = load_material_data("materials_data.csv")
    # if data is not None:
    #     data = clean_data(data)
    
    print("模块加载完成，可以导入使用！")