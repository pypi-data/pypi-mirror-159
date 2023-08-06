from distutils.core import setup


setup(
    name='Demo8799',  # 对外我们模块的名字
    version='1.0',  # 版本号
    description='测试本地发布模块',  # 描述
    author='dgw',  # 作者
    author_email='879967992@qq.com',
    py_modules=['Demo8799.demo1', 'Demo8799.demo2'],  # 要发布的模块
)
