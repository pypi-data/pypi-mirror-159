import setuptools

with open("README.MD",'r',encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name = "hltest",                #包名称
    version = "0.0.3",              #包版本   每次上传需要更新
    author = "GFF",                 #作者
    author_email = "gaofeifei0619@163.com",             #邮箱
    description = "测试版本",                          #项目的简单描述
    long_description = long_description,                #README.MD    项目详细介绍
    long_description_content_type = "text/markdown",    #诉索引什么类型的标记用于长描述。在这种情况下，它是Markdown。
    url = "https://github.com/",                        #是项目主页的URL。对于许多项目，这只是一个指向GitHub，GitLab，Bitbucket或类似代码托管服务的链接。
    license = "MIT License",
    packages = setuptools.find_packages(),      #是应包含在分发包中的所有Python 导入包的列表。我们可以使用 自动发现所有包和子包，而不是手动列出每个包。在这种情况下，包列表将是example_pkg，因为它是唯一存在的包。find_packages()
    classifiers = [                             #告诉索引并点一些关于你的包的其他元数据。在这种情况下，该软件包仅与Python 3兼容，根据MIT许可证进行许可，并且与操作系统无关。您应始终至少包含您的软件包所使用的Python版本，软件包可用的许可证以及您的软件包将使用的操作系统。
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",       #当前python package的使用许可证
        "Operating System :: OS Independent",
    ],
)