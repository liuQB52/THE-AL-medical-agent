#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FastAPI 主应用配置
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from api.routes import router as api_router
from utils.logger import setup_logger

logger = setup_logger(__name__)

# 创建FastAPI应用
app = FastAPI(
    title="THE AL Medical Agent",
    description="医学PET-CT AI诊断系统",
    version="1.0.0",
)

# CORS中间件配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件
static_path = Path(__file__).parent.parent / "static"
if static_path.exists():
    app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

# 包含API路由
app.include_router(api_router, prefix="/api")


@app.get("/")
async def root():
    """根路由"""
    return {
        "message": "Welcome to THE AL Medical Agent",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy", "version": "1.0.0"}


logger.info("FastAPI应用已初始化")
