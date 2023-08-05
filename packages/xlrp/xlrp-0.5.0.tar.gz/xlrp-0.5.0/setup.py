import setuptools
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
setuptools.setup(
    name="xlrp",    # 包名
    version="0.5.0",  # 版本
    author="测码范晔",   # 作者
    author_email="1538379200@qq.com",    # 邮箱
    description="生成excel测试报告",
    long_description=long_description,  # 长介绍，为编写的README
    long_description_content_type="text/markdown",  # 使用介绍文本
    url="",     # github等项目地址
    packages=setuptools.find_packages(),    # 自动查找包，手动写也可
    install_requires=['numpy>=1.22.3', 'matplotlib>=3.5.1', 'openpyxl>=3.0.9', 'pywin32', 'luckylog'],    # 安装此包所需的依赖，没有为空
    entry_points={
    },
    classifiers=(       # 其他的配置项
        "Programming Language :: Python :: 3",      # 限制pytest编程语言，版本为3
        "License :: OSI Approved :: MIT License",   # 使用MIT的开源协议(手动添加协议后修改此项)
        "Operating System :: OS Independent",   # 系统要求
    ),
)