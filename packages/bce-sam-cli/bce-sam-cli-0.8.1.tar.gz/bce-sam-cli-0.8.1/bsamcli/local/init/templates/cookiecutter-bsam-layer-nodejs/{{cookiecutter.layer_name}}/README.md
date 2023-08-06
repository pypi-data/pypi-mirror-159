# {{ cookiecutter.layer_name }}

本项目是 Layer {{ cookiecutter.layer_name }} 的示例模板，项目结构如下：

```bash
.
├── README.md
├── lib                         <-- 存放 Layer 内容
│   └── nodejs                  <-- 示例 nodejs 依赖
│       ├── node_modules        
│       ├── package-lock.json
│       └── package.json
└── template.yaml

## 使用前提

* BSAM CLI 已成功安装

## 创建 layer

```
bsam layer init --name myLayer --compatible-runtimes nodejs10
```

可以使用简写的 options:

```
bsam layer init -n myLayer -r nodejs10
```

指定兼容多个运行时:

```
bsam layer init -n myLayer -r nodejs10 -r nodejs12 
```

指定创建在哪个目录下:

```
bsam layer init -n myLayer -r nodejs10 -r nodejs12 -o ~/cfclayers
```

## layer 打包与部署

BSAM CLI 可以将 Layer 打包部署，根据 `LayerUri` 参数获取 Layer 文件所在路径。

```yaml
...
    mylayer:
        Type: BCE::Serverless::Layer
        Properties:
            LayerUri: lib/
            ...
```

执行如下命令会把 `LayerUri` 目录下的文件打成 zip 包：

```bash
bsam package
```

接下来，您可以使用 `deploy` 命令把 layer 创建或更新到云端。

```bash
bsam deploy
```

> **关于 BSAM CLI 的更多用法，请查看该文档 https://cloud.baidu.com/doc/CFC/s/6jzmfw35p**