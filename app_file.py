#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 【app_file】
#
#  概要:
#       FastAPI でファイルを扱う
#
import pandas as pd
from fastapi import FastAPI, File, UploadFile
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/saveuploadfile/")
async def save_upload_file_tmp(file: UploadFile=File(...)):
    tmp_path:Path = ""
    try:
        suffix = Path(file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        file.file.close()

    #df = pd.read_csv(tmp_path, delimiter='\t') if str(tmp_path).endswith(".tsv") else pd.read_excel(tmp_path, sheet_name="Sheet1")

    return FileResponse(path=tmp_path, filename="test.tsv", media_type="text/plain")
