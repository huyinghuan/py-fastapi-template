import argparse
import uvicorn
from app.config import init_config
from app import server

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="示例命令行参数解析")
    parser.add_argument("--port", type=int, help="环境变量文件", default=8000)
    parser.add_argument(
        "--conf", type=str, help="配置文件", default="conf/conf.yaml")
    # load the environment variables from `.env` file
    args = parser.parse_args()
    init_config(args.conf)
    
    uvicorn.run(
        app=server, port=args.port)
