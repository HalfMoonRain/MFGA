from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Item(BaseModel):
    FV: float
    n:float
    R:float 
    YTM:float

@app.get("/")
def root():
    return {"Hello" : "world"}


@app.get("/calculate", summary="현재가치 계산")
def calculate(FV: float, n: int, R: float, YTM: float):
    """
    # 이자계산과 원금계산을 합계하여 현재가치 출력
    """
    interest = calculate_sum_fv_r(FV, R, YTM, n)
    principal = calculate_fv_single(FV, YTM, n)
    return {"interest : " : interest, "principal : " : principal, "total : " : interest + principal}

def calculate_sum_fv_r(FV, R, YTM, n):
    """
    ∑(FV * R) / (1 + YTM)^i for i in range 1 to n
    """
    sum_value = sum((FV * R) / (1 + YTM)**i for i in range(1, n + 1))
    return sum_value

def calculate_fv_single(FV, YTM, n):
    """
    FV / (1 + YTM)^n
    """
    value = FV / (1 + YTM)**n
    return value
