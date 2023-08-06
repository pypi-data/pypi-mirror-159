import setuptools

setuptools.setup(
    name='',
    version='',
    author='',
    author_email='',
    description='',
    long_description_content_type="""text/markdown""",
    url='',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
from setuptools import setup, find_packages

setup(
    name='lzlzhn',  # 包名
    version='2022.7.16.1920.1',  # 版本
    description="一个很会玩的第三方库,更新版本号与更新/修复个数有关",  # 包简介
    long_description='HELLO! 感谢你下载我的第三方库！十分感谢！',  # 读取文件中介绍包的详细内容
    include_package_data=True,  # 是否允许上传资源文件
    author='24K野生程序员/24K Wild Programmers',  # 作者
    author_email='liuniandexiaohuo@qq.com',  # 作者邮件
    maintainer='24K野生程序员/24K Wild Programmers',  # 维护者
    maintainer_email='liuniandexiaohuo@qq.com',  # 维护者邮件
    license='MIT License',  # 协议
    url='https://blog.csdn.net/l15668952150/article/details/124575394',  # github或者自己的网站地址
    packages=find_packages(),  # 包的目录
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',  # 设置编写时的python版本
    ],
    python_requires='>=3.6',  # 设置python版本要求
    install_requires=['pyperclip', 'PyAutoGUI', 'pygame', 'qrcode', 'MyQR']# 安装所需要的库

)