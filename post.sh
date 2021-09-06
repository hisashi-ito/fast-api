#! /bin/bash
#curl -X POST "http://127.0.0.1:8000/saveuploadfile/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@input.tsv"
curl -X POST "http://127.0.0.1:8000/saveuploadfile/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@Book.xlsx"