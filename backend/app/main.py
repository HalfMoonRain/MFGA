from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Item(BaseModel):
    FV: float # 액면금액(원금)
    n: float # 만기(년)
    R: float # 액면이자율(1년)
    YTM: float # 만기수익률(1년)
    payment_frequency: int # 이자지급횟수(회1년 , ex  2 = 6개월마다 지급, 4 = 3개월마다 지급)

@app.get("/")
def root():
    return {"Hello" : "world"}


@app.get("/calculate", summary="현재가치 계산")
def calculate(FV: float, n: int, R: float, YTM: float, payment_frequency: int):
    """
    # 이자의 연금현재가치계산과 원금의 현재가치계산을 합계하여 채권의 현재가치 출력
    """
    adjusted_R = R / payment_frequency  # 주기별 이자율
    adjusted_YTM = YTM / payment_frequency  # 주기별 수익률
    total_periods = n * payment_frequency  # 총 이자 지급 횟수
    
    interest = calculate_sum_fv_r(FV, adjusted_R, adjusted_YTM, total_periods)
    principal = calculate_fv_single(FV, adjusted_YTM, total_periods)
    return {"interest : " : interest, "principal : " : principal, "total : " : interest + principal}

def calculate_sum_fv_r(FV, adjusted_R, adjusted_YTM, periods):
    """
    ∑(FV * adjusted_R) / (1 + adjusted_YTM)^i for i in range 1 to periods
    """
    sum_value = sum((FV * adjusted_R) / (1 + adjusted_YTM)**i for i in range(1, periods + 1))
    return sum_value

def calculate_fv_single(FV, adjusted_YTM, periods):
    """
    FV / (1 + adjusted_YTM)^periods
    """
    value = FV / (1 + adjusted_YTM)**periods
    return value
