#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 【app_file】
#
#  概要:
#       FastAPI でファイルを扱う
#
from fastapi import FastAPI, File, UploadFile
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

app = FastAPI()

@app.post("/saveuploadfile/")
async def save_upload_file_tmp(fileb: UploadFile=File(...)):
    tmp_path:Path = ""
    try:
        print(type(fileb))# <class 'starlette.datastructures.UploadFile'>
        print(type(fileb.file)) #<class 'tempfile.SpooledTemporaryFile'>
        suffix = Path(fileb.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(fileb.file, tmp)
            tmp_path = Path(tmp.name)
            print(tmp_path)
    finally:
        fileb.file.close()
    return {
        "filename": fileb.filename,
        "temporary_filepath": tmp_path,
        "fileb_content_type": fileb.content_type,
    }
