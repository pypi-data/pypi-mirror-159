# sixbox linux版本

sixbox linux 开发说明总结， 适用于本地服务器和集群环境。

参考: https://github.com/apache/airflow/blob/f02b0b6b4054bd3038fc3fec85adef7502ea0c3c/airflow/cli/commands/db_command.py
## TODO

- [x] 修复用户无docker权限时，自动使用udocker运行提示docker/udocker/singularity is not ready，实际udocker已经安装。
- [ ] 添加sixbox uninstall命令，实现卸载sixbox（删除安装目录下所有内容并删除写入~/.bashrc 内的sixbox和udocker环境变量）
- [ ] install 命令新增下载进度实时显示(可使用tqdm显示)
- [ ] 新增日志器，使用logger包管理全局日志打印
    1. 替代现有print语句，日志设INFO, WARNNING, ERRO三个级别
    2. 管理do_call函数无法处理的报错信息，统一返回日志，不要打印python tracbace信息（用户并不需要了解代码级别的错误，这部分不暴露给用户看）
    3. 日志依据不同级别，以不同颜色打印（可选，详情逻辑自行查阅资料）
- [x] 新增export 命令，类似docker export命令，支持导出CWLdb内的CWL到用户指定的地址。
- [ ] sixbox安装目录etc目录下，新增sixbox.service文件，用于记录sixbox运行时变量或配置(区别于用户~/.sixbox/config.yaml), 这部分不提供给用户修改，由sixbox后台读写，不暴露给用户更改。
- [ ] sixbox 新增自动检查更新，大致代码逻辑可参考：
  - 1.在$(which sixbox)/etc/sixbox.service（YAML格式）内新增字段checkTime用于记录上次联网检查的时间。
  - 每次运行sixbox时检查checkTime间隔时间是否达到设置的检查周期。
  - 联网检查是否有sixbox新版本供更新（可参考pip的更新提示）
- [ ] lib 目录新增runtimes目录，用于sixbox run命令运行CWLdb内的流程，CWL流程运行时copy到runtimes目录后再运行，不要使用CWLdb内的content地址直接运行，以区分存储和运行状态，避免运行错误导致对原CWL content内容的损坏。
- [ ] 添加CWL test，merge，自动生成CWL（如转换WDL，python包）为CWL的功能到sixbox run命令。
  - 可去cwltool官网查找相关第三方包。
- [ ] 整合frictionless包到sixbox，以用于数据校验。
- [x] 添加sixbox push命令。


- [x] 参考docker lib目录设计sixbox目录
- [x] cwlc存放目录与cwl存放目录之间的交互
- [x] cwlc可以直接run
- [x] 可以从cwlc中提取cwl，并将cwl放入对应文件夹
- [x] cwl和相应参数可以生成cwlc，并将生成的cwlc放入对应文件夹
- [x] runtime功能实现（runtime运行时，是为了防止运行时的一些错误）
- [x] 写一个通用函数初始化lib目录结构，检查现有目录是否符合设定路径。代码逻辑：现将设定好的目录结构写成一个dic或yaml，之后读取libpath中目录结构，写成一个dic或这是yaml，然后比对。

## 目录结构

当前目录结构为：
```

./
├── build # pyinstaller 编译之后的二进制文件存放于此。
├── build.sh # 自动编译shell脚本
├── CHANGELOG.md # 记录项目更新日志
├── dist # 最终编译成功的二进制文件存放于此
├── docker # 存放Dockerfile
├── docs # 项目详细说明文档，包括设计稿件，各部分代码逻辑等
├── examples # 各种配置的demo示例，包括env文件模板等。
├── lib # 本地测试使用的CWLdb libPath 地址
├── LICENSE
├── main.py # 项目主程序入口
├── README.md
├── scripts # 所有辅助性小脚本，一般为一些有助于运行，自动调试等的脚手架性质的shell脚本，包括run.sh等。
├── sixbox # 主体代码
├── sixbox.spec
├── testdata # 测试数据与测试CWL，可用于开发测试
├── tests  # 自动化测试脚本，目前没有实施，后续可能要用pytest实现，避免现在手动测试。
└── test.sh # 用不容器内自动安装运行sixbox的自动化脚本
```

其中主体代码sixbox目录结构为：
```
./
├── backend # 与后端交互的所有api函数
├── cli # sixbox命令
├── hooks # pyinstaller编译所需hooks文件
├── __init__.py # 表征sixbox目录是一个python包
├── __pycache__
├── SixOclock-latest-Linux-head.sh # sixbox最终二进制编译脚本的shell部分，此代码实现用户交互式安装sixbox的功能。
└── static # sixbox安装过程或安装到到用户系统后需要的一些静态示例或者二进制文件
```


## cli的命令逻辑

sixbox目前支持以下命令：

```
usage: sixbox [-h] [-V] {config,update,install,uninstall,run,pull,cwls,commit,tag,rm} ...

sixbox is a tool for managing and running CWL workflow local and from www.sixoclock.net.

positional arguments:
  {config,update,install,uninstall,run,pull,cwls,commit,tag,rm}
                        sub-command help
    config              Modify configuration values in config.yaml. The token in the configuration file is related   
                        to the user's permissions.
    update              Updates sixbox package to the latest compatible version
    install             Installs sixbox package.
    uninstall           uninstall a package
    run                 running cwltool.
    pull                get CWL Workflow from sixoclock.net.
    cwls                Show the existing CWL Workflow in cwldb.
    commit              Commit your CWL Workflow into your cwldb.
    tag                 Modify CWL Workflow tag
    rm                  Remove CWL from CWLdb

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         Show the sixbox version number.
```

## 依赖

sixbox依赖cwltool和docker/udocker

cwltool通过主体代码中导入python包的形式引用，
udocker存放于./sixbox/static/bin 内，用户安装sixbox的时候进行安装

### cwltool

当前版本：

windows 下只有特定CWL 版本可用，且需要保证setuptools<58.0.0,以避免use_2to3无效。
```
cwltool 3.0.20210124104916
schema-salad=7.0.20210124093443
setuptools==57.5.0
```

通过pip install cwltool 安装

### udocker

udocker(https://github.com/indigo-dc/udocker) 是一个python写的运行docker容器的软件包

当前使用的版本为udocker-1.1.7.tar.gz
构建时，注意尽量使用最新的稳定版udocker，以跟踪最新的功能。

#### udocker编译

udocker采用离线安装的方式(INSTALL FROM UDOCKERTOOLS TARBALL), 因此在./sixbox/static/bin 目录下会事先准备两个udocker文件：
```
.
├── udocker  #udocker运行程序
└── udocker-1.1.7.tar.gz  #用于离线安装的udocker安装包
```
获取途径如下：
```
参考链接：https://github.com/indigo-dc/udocker/blob/v1.1.7/doc/installation_manual.md
curl -L https://github.com/jorge-lip/udocker-builds/raw/master/tarballs/udocker-1.1.7.tar.gz > udocker-1.1.7.tar.gz    #获取udocker-1.1.7.tar.gz
tar xzvf udocker-1.1.7.tar.gz udocker   #获取udocker程序
```
udocker安装方式：
```
export UDOCKER_TARBALL=$PREFIX/bin/udocker-1.1.7.tar.gz && $PREFIX/bin/udocker install
```


## 构建与测试

### 构建

参考： https://setuptools.pypa.io/en/latest/userguide/quickstart.html


#### 构建步骤

1. 使用项目根目录下的main.py 构建 sixbox可执行程序

2. 拷贝可执行程序到dist/static/bin下，打包整个目录为sixbox.tar.gz

3. 使用build.sh 生成SixOclock-latest-Linux.sh

4. 运行sh SixOclock-latest-Linux.sh 即可在指定目录安装sixbox

具体可参考./build.sh

#### 构建环境

在centos7.6 python3.6构建，基于docker容器

确保安装有所有的依赖。

```
# docker build -f docker/build_env.Dockerfile -t 666oclock/sixbox-linux.build_env:v0.1 .
docker pull 666oclock/sixbox-linux.build_env:v0.2

```

#### 自动化构建
运行构建脚本
```
cd sixbox-linux

docker run -it -v ${PWD}:/home/test -w /home/test 666oclock/sixbox-linux.build_env:v0.2 bash build.sh

```

### 测试

#### 测试环境

宿主机内测试：

```
# ./dist/sixbox commit testdata/soapnuke-filter.cwl test/soapnuke-filter:v0.1
# ./dist/sixbox run ./testdata/soapnuke-filter.cwl ./testdata/soapnuke-filter.yaml

```

容器内测试：
在安装有python2.7的ubuntu 18.04中测试sixoclock安装和功能，基于docker容器

```
docker build -t 666oclock/sixbox-linux.test_env:v0.11 -f docker/test_env.Dockerfile .
```

#### 自动化测试

运行测试脚本
可交互式进入容器内，依次执行命令bash test.sh, source ~/.bashrc, sixbox [具体待测试命令]来依次测试sixbox命令是否正常。

```
cd sixbox-linux

# 使用docker作为sixbox 容器运行环境
docker run -it -v ${PWD}:/home/test -w /home/test -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker 666oclock/sixbox-linux.test_env:v0.3 bash

bash test.sh

# 使用udocker作为sixbox 容器运行环境
docker run -u $(id -u):$(id -n)::$(id -g) --hostname sixbox_test -it -v ${PWD}/build:/home/$(whoami) -v ${PWD}:/home/test -w /home/test 666oclock/sixbox-linux.test_env:v0.3 bash
bash test.sh
```

## 发布
一个版本开发测试通过后，同步发布安装包与文档到网站。
### 发布二进制安装包

宿主机和镜像内测试通过之后，先发布安装包到beta目录，通知团队成员sixbox更新版本以协助测试

使用命令`sixbox update sixbox--beta` 以下载更新beta版本供测试。

测试通过后发布二进制安装包到sixoclock.net网站history目录，并在latest目录同步拷贝一份并重命名为`Sixbox_linux64_latest.sh`.

目前二进制安装包存放于正式服务器地址：`/data/users/6oclockPub/6oclock_pro/static/resources/dist/`

目录结构为：
```
.
├── beta # 存放预览版本二进制
│   ├── sixbox
│   │   ├── 1.0.20210520091240
│   │   ├── 1.1.20210530094243
│   │   ├── 1.1.20210531130910
│   │   └── 1.1.20210607110610
│   └── Sixbox_linux64_latest.sh
├── history # 存放sixbox各历史版本
│   ├── linux
│   │   └── sixbox
│   └── windows
├── latest # 存放sixbox最新版本的二进制
│   ├── installer.exe
│   ├── Sixbox_linux64_latest.sh
│   └── Sixbox_win64_latest.exe
├── source.list # 记录几个安装包的下载源，暂时用于sixbox windows版本在线更新时调用

```
稳定版本命令为 `Sixbox_linux64_latest.sh`
历史版本命名为 `Sixbox_linux64_版本号.sh`

`history/linux/sixbox`目录结构为：
```
./
├── 1.1.20210530094243 # 版本号
│   ├── readme # 用于说明该版本的更新日志
│   ├── sixbox # sixbox安装包，对应本地build时的dist/sixbox (是pyinstaller直接编译main.py得到的二进制文件)
│   └── Sixbox_linux64_1.1.20210530094243.sh # 最终的安装包
```

发布二进制安装包，在history/linux/sixbox下新增目录并上传对应二进制文件。同时本地通过`sixbox update sixbox`命令测试是否可以正常更新新发布的sixbox，并测试sixbox新版功能。如一切功能正常，则复制`history/linux/sixbox`目录下最新版本的Sixbox_linux64_版本号.sh到latest目录，并重命名为Sixbox_linux64_latest.sh（该文件为通过网站下载sixbox时所调用）

## 发布用户文档
新功能更新后同步更新用户使用说明到网站：https://docs.sixoclock.net/

sixbox-linux部分的内容在https://docs.sixoclock.net/clients/sixbox-linux.html中说明

先尝试在本地修改并预览six-docs仓库里的对应markdown文档（基于vue的帮助文档系统）：
```
git pull six-docs

# 进入项目目录
cd six-docs

# 安装依赖并启动服务（服务依赖nodejs，可在系统中通过anaconda安装node 和yarn，并配置yarn的源为国内源以加快包的下载速度）
yarn install # 安装依赖，一般安装一次即可
yarn docs:dev # 热启动服务，可在浏览器在线预览markdown渲染效果
```

修改仓库docs目录下对应markdown内容，实时预览修改效果。将完稿同步到Git仓库，并告知管理员进行合并和在线发布。
