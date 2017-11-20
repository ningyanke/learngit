
### Atom编辑器

#### 1.下载
>[官方网站](https://atom.io/)可自动生成自己系统对应版本的编辑器软件,然后点击下载

#### 2.安装
>我使用的是Ubuntu系统,直接使用软件中心安装，或者在命令行中输入
>`dkpg -i xxxx.deb`

#### 3.配置
>3.1配置中文语言
>选取`install`,输入`Chinese`选取最高的插件安装
>![atom1](./picture/atom1.png)
>
>3.2安装`markdown`支持包
>
>1)`markdown-preview-plus`
>Atom自带的`Markdown`预览插件`markdown-preview`功能比较简,`markdown-preview-plus`对其做了功能扩展和增强。
>>* 支持预览实时渲染(`Ctrl + Shift + M`)
>>* 支持`Latex公式`(`Ctrl + Shift + X`)

>使用该插件前,需要先禁用`markdown-preview`.点击`disable`禁用
>![atom2](./picture/atom2.png)
>
>`Enable`新插件
>![atom3](./picture/atom3.png)
>
>2)`markdown-scroll-sync`同步滚屏
>
>同步滚动是`Markdown`编辑器的必备功能,方便翻阅文档修改时能快速定位到预览的位置.
>markdown-scroll-sync不仅支持同步滚动,在光标位置发生变更时也会同步滚动，这个功能在很多Markdown编辑器中不具备.
>同样在`install`中搜索安装
>
>3）`language-markdown`
>一般的Markdown编辑器提供了代码着色等基本功能`language-markdown`除了能给代码着色，还提供了快捷的代码片段生成等功能
>
>4）`markdown-image-paste`
>图片功能支持的好坏直接决定了我是否选择使用一个`Markdown`编辑器.也有不少编辑器和在线的图床绑定,但是这种方式受限于网络.虽然`Markdown`支持插入本地图片,但是每次插入新图片都是一堆重复操作：截图－命名－保存－插入.`markdown-image-paste`将这些操作一步完成：

>>* 使用截图工具将图片复制到系统剪切板。
>>* 在Markdown新起一行输入文件名。
>>* `Ctrl + V`会自动把图片保存到Markdown文件相同目录下(因此要求Markdown文件应该先保存)，并命名为刚输入的文件名，同时在刚才输入文件名行处生成`img`标签。

>5)`markdown-table-editor`
>表格编辑,具有强大的功能

>6)`markdown-preview-opener`
> 这个控件可以让打开的`.md`文件默认显示预览视图

>3.3设置文本缩进
>
>![atom4](./picture/atom4.png)

[文章出处](http://www.cnblogs.com/fanzhidongyzby/p/6637084.html)
