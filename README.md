# 轻版馆边缘计算型Markdown至HTML转换器

本项目可以部署在Cloudflare Workers上，用户通过GET方法提供URL参数，或者通过POST方法向本程序提交Markdown数据，可使本程序从互联网上的任意位置下载Markdown格式的文件或数据，并按照用户提供参数的指定方式转换为HTML代码返回响应。

如果需要自行部署此项目，请在Cloudflare Workers上创建一个支持Python语言的Worker，然后将本项目的代码部署上去。

## 使用方法

### 获取外部Markdown文件

```
GET https://md.lightnovel.moe/?partial=0&style=none&from=<url>
```

#### `partial`参数（未实现）

- `partial`为`0`时（默认），输出完整页面的HTML代码，此时`style`参数生效；
- `partial`为`1`时，仅输出按照Markdown数据的内容转换得到的HTML代码。

#### `style`参数（未实现）

- `none`（默认）：无风格，会以浏览器原本的样式显示；
- `bootstrap`（未支持）：使用Bootstrap的CSS样式；
- `github`（未支持）：使用Github的Markdown渲染风格；
- `lightnovel`（未支持）：根据轻版馆实际业务需要进行风格渲染。

#### `from`参数

必须是一个合法的URL字符串。此参数应当写在尾部。

### 直接提交Markdown数据（未实现）

```
POST https://md.lightnovel.moe/?partial=0&style=none
```

#### `partial`参数（未实现）

- `partial`为`0`时（默认），输出完整页面的HTML代码，此时`style`参数生效；
- `partial`为`1`时，仅输出按照Markdown数据的内容转换得到的HTML代码。

#### `style`参数（未实现）

- `none`（默认）：无风格，会以浏览器原本的样式显示；
- `bootstrap`（未支持）：使用Bootstrap的CSS样式；
- `github`（未支持）：使用Github的Markdown渲染风格；
- `lightnovel`（未支持）：根据轻版馆实际业务需要进行风格渲染。

## 更新日志

### 0.1.0 Alpha 20241212

仅实现了通过URL获取外部Markdown文件并转换的功能。`partial`和`style`参数对应的功能未实现，输出结果总是`partial=1`的情形，这不是文档计划的默认情况。为确保用户应用对本服务后续版本的兼容性，使用时应带上这一参数。