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
from fastapi import Query, Path # Query,Path
from pydantic import BaseModel
from fastapi import Body

app = FastAPI()

class ItemOut(BaseModel):
    strings: str
    aux: int = 1
    text: str

# method and endopoint
@app.get('/', response_model=ItemOut)
async def response(strings: str, integer: int):
    return {"text": "hello world!", "strings": strings, "integer": integer}

#async def hello():
#    return {"text": "hello world!"}

@app.get('/get/{path}')
async def path_and_query_params(
        path: str,
        query: int,
        default_none: Optional[str] = None): # optional で型
    return {"text": f"hello, {path}, {query} and {default_none}"}

# 第一引数はデフォルト値を指定。デフォルト値なし (required)にしたい場合は、...を渡す
@app.get('/validation/{path}')
async def validation(
        string: str = Query(None, min_length=2, max_length=5, regex=r'[a-c]+.'),
        integer: int = Query(..., gt=1, le=3),  # required
        alias_query: str = Query('default', alias='alias-query'),
        path: int = Path(10)):
    return  {"string": string, "integer": integer, "alias-query": alias_query, "path": path}

# POST method の場合
class Data(BaseModel):
    """class Data(BaseModel)"""
    string: str
    default_none: Optional[int] = None
    lists: List[int]

# post
#
# 以下のjson を受ける
#
# {
#     "string": "string",
#     "default_none": 0,
#     "lists": [1, 2]
# }
#
@app.post('/post')
async def declare_request_body(data: Data):
    return {"text: hello {}, {}. {}".format(data.string, data.default_none, data.lists)}

# post/embed
#
# 以下のjson を受ける
#
# {
#     "data": {
#         "string": "string",
#         "default_none": 0,
#         "lists": [1, 2]
#     } 
# }
#
@app.post('/post/embed')
async def declare_embedded_request_body(data: Data = Body(..., embed=True)):
    return {"text: hello {}, {}. {}".format(data.string, data.default_none, data.lists)}
 

# post/nest
#
# 以下のjsonを受ける
#
# {
#     "subData": {
#         "strings": "string",
#         "integer": 0
#     },
#     "subDataList": [
#         {"strings": "string0", "integer": 0},
#         {"strings": "string1", "integer": 1},
#         {"strings": "string2", "integer": 2}
#     ]
# }
#

# subData の型ヒント
class subDict(BaseModel):
    string: str
    integer: int

class NestedData(BaseModel):
    subData: subDict
    subDataList: List[subDict]

@app.post('/post/nested')
async def declare_nested_request_body(data: NestedData):
    return {"text": f"hello, {data.subData}, {data.subDataList}"}

    
