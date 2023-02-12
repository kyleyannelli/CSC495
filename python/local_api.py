from typing import Union
from fastapi import FastAPI

import live_audio as AmpFX
import json

app = FastAPI()


@app.get("/outputs")
def get_outputs():
    return json.dumps(AmpFX.get_output_devices())


@app.get("/inputs")
def get_inputs():
    return json.dumps(AmpFX.get_input_devices())
