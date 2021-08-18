#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 【app】
#
#  概要:
#       FastAPI のレッスン
#
from fastapi import FastAPI

app = FastAPI()

# method and endopoint
@app.get('/')
async def hello():
    return {"text": "hello world!"}
