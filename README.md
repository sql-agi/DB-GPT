# DB-GPT: 使用自然语言管理数据库，彻底改变传统的web管理后端界面


<div align="center">
  <p>
    <a href="https://github.com/sql-agi/DB-GPT">
        <img alt="stars" src="https://img.shields.io/github/stars/sql-agi" />
    </a>
    <a href="https://github.com/sql-agi/DB-GPT">
        <img alt="forks" src="https://img.shields.io/github/forks/sql-agi/db-gpt" />
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img alt="License: MIT" src="https://img.shields.io/github/license/sql-agi/db-gpt" />
    </a>
     <a href="https://github.com/sql-agi/DB-GPT/releases">
      <img alt="Release Notes" src="https://img.shields.io/github/v/release/sql-agi/DB-GPT" />
    </a>
    <a href="https://github.com/sql-agi/DB-GPT/issues">
      <img alt="Open Issues" src="https://img.shields.io/github/issues-raw/sql-agi/DB-GPT" />
    </a>
  </p>
 👋 加入我们的 <a href="img/WECHAT.md" target="_blank">WeChat</a>
</div>

## Introduction
🤖 DB-GPT是一个开源的数据应用程序开发框架，旨在利用大型语言模型（LLM）技术通过自然语言与数据库进行交互，取代了传统的web管理后端。

目前，我们只能访问查询权限。为了满足更复杂的业务需求，包括创建、读取、更新和删除（CRUD）功能，我们目前正在进行内部测试，并期待着在未来能给大家带来更多的惊喜。

🚀🚀🚀 在Data 3.0时代，我们的产品致力于利用模型和数据库技术，使企业和开发人员能够用更少的代码构建自定义应用程序。让开发人员更专注于复杂的C端业务从而取代传统的web管理后台系统。

## 快速上手
找一个项目存储的目录，然后执行以下命令
```shell
git clone https://github.com/sql-agi/DB-GPT
cd DB-GPT
conda create --name db-gpt python=3.9
conda activate db-gpt
```
然后将环境切换到db-gpt并执行以下命令
```shell
pip install -r requirements.txt
```

配置.env文件，可以参考 templates.env_tample
主要配置包括三个属性：OPENAI_API_KEY、OPENAI_PI_BASE、MYSQL_URL

### Web & CLi
我们提供了一种基于 [Gradio]（ https://gradio.app ）网络版演示和命令行演示如下：

#### web demo
![web-demo](img/web.jpg)

然后在存储库中运行[web_demo.py]：

```shell
python web_demo.py
```

程序会运行一个 Web Server，并输出地址。在浏览器中打开输出的地址即可使用。最新版 Demo 实现了打字机效果，速度体验大大提升。注意，由于国内 Gradio 的网络访问较为缓慢，启用 demo.queue().launch(share=True, inbrowser=True) 时所有网络会经过 Gradio 服务器转发，导致打字机体验大幅下降，现在默认启动方式已经改为 share=False，如有需要公网访问的需求，可以重新修改为 share=True 启动。

#### cli demo
![cli-demo](img/cli_01.jpg)

![cli-demo](img/cli_02.jpg)

在存储库中运行[cli_demo.py]（cli_demo.py）：

```shell
python cli_demo.py
```

该程序将在命令行上进行交互式对话。输入指令并按命令行上的Enter键生成回复，然后输入“quit”终止程序。

### API Deploy

Run [api.py](api.py)： in the repository:

```shell
python api.py
```
默认情况下在端口8000上本地部署，通过POST方法调用

```shell
curl -X POST "http://127.0.0.1:8000/chat/db" \
     -H "Content-Type: application/json" \
     -d '{"input": "你好"}'
```
得到的返回值为

```shell
{
    "reply": "你好！请问有什么可以帮助您的？"
}
```

## 未来计划
🔥🔥🔥前端：我们致力于开发更优秀的前端UI界面，进一步支持更多类型的数据库以及LLM（其中包含开源大模型），以提升用户体验和系统灵活性。
🔥🔥🔥后端：我们将进一步深度测试更复杂的CRUD场景，增加区分（切换）环境、设置角色权限等功能从而保证LLM操作的准确性和稳定性。
🔥🔥🔥总结：希望更多的用户体验并提供反馈，我们会根据用户的反馈进一步优化我们的产品，并希望感兴趣的小伙伴加入我们的开源团队。

## 联系我们

### 项目交流群
<img src="img/qr_code_wechat.jpg" alt="二维码" width="300" />

🎉 Chat_DB 项目微信交流群，如果你也对本项目感兴趣，欢迎加入群聊参与讨论交流。

### 公众号

<img src="img/qr_code_account.jpg" alt="二维码" width="300" />

🎉 Chat_DB 项目官方公众号，欢迎扫码关注。

## 🤗 Reference project
https://github.com/langchain-ai/langchain