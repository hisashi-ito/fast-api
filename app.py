#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 【app】
#
#  概要:
#       FastAPI のレッスン
#
from fastapi import FastAPI
from typing import List, Dict
from typing import Optional

app = FastAPI()

# method and endopoint
@app.get('/')
async def hello():
    return {"text": "hello world!"}

@app.get('/get/{path}')
async def path_and_query_params(
        path: str,
        query: int,
        default_none: Optional[str] = None): # optional で型
    return {"text": f"hello, {path}, {query} and {default_none}"}
