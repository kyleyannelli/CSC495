#!/bin/sh
cd python
python3 -m uvicorn local_api:app --port 30108 --reload
