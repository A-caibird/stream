from fastapi import FastAPI
from fastapi.responses import StreamingResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import asyncio
import json
import uvicorn
import os
from pydantic import BaseModel

app = FastAPI()

# 配置CORS，允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置为特定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 检查静态文件目录是否存在，如果不存在则创建
if not os.path.exists("static"):
    os.makedirs("static")

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")


class Query(BaseModel):
    prompt: str


# 模拟AI处理函数
async def fake_ai_processing(prompt: str):
    # 这里模拟AI生成文本的过程
    response = f"您的问题是: {prompt}\n\n"

    # 添加模拟的AI回答
    chunks = [
        "我是一个AI助手，",
        "我可以帮助您解答问题，",
        "提供信息，",
        "或者完成各种任务。",
        "您可以问我任何问题，",
        "我会尽力提供有用的回答。",
        "流式输出让您可以看到我思考的过程，",
        "就像人类思考一样，逐步形成答案。",
    ]

    for chunk in chunks:
        yield json.dumps({"text": chunk}) + "\n"
        await asyncio.sleep(0.3)  # 模拟生成延迟


@app.post("/api/chat")
async def stream_chat(query: Query):
    return StreamingResponse(
        fake_ai_processing(query.prompt), media_type="application/json"
    )


@app.get("/")
async def read_root():
    # 重定向到静态目录中的index.html
    return RedirectResponse(url="/static/index.html")


if __name__ == "__main__":
    print("服务已启动，请访问: http://localhost:8000")
    print("请确保index.html文件已放置在./static目录下")
    uvicorn.run(app, host="0.0.0.0", port=8000)
