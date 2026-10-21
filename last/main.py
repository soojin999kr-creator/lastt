from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uvicorn

# FastAPI 애플리케이션 초기화
app = FastAPI()

# CORS 설정: 구글 앱스 스크립트 및 외부 웹 클라이언트에서의 원활한 통신을 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 클라이언트로부터 전달받을 요청 데이터 구조 정의 (Pydantic 모델)
class SortRequest(BaseModel):
    data: list[int]

# 서버 정상 작동 여부를 확인하기 위한 루트 엔드포인트
@app.get("/")
def read_root():
    return {"status": "running", "message": "Insertion Sort Cloud Run Server is active!"}

# 단순 삽입 정렬(Insertion Sort) 알고리즘 수행 엔드포인트
@app.post("/insertion_sort")
def insertion_sort(request: SortRequest):
    arr = list(request.data)
    n = len(arr)
    steps = []
    
    # 정렬 시작 전 초기 데이터 상태를 첫 번째 단계로 저장
    steps.append(list(arr))
    
    # 단순 삽입 정렬 알고리즘 핵심 로직
    for i in range(1, n):
        key = arr[i] # 현재 비교할 기준 원소
        j = i - 1
        
        # 정렬된 앞부분의 원소들을 뒤에서부터 탐색하며 key보다 큰 값들을 오른쪽으로 한 칸씩 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # 적절한 위치에 key 원소 삽입
        arr[j + 1] = key
        
        # 매 단계마다 변하는 배열의 상태를 기록
        steps.append(list(arr))
            
    # 최종 정렬된 배열, 단계별 상태 목록, 시간 복잡도, 상태 메시지 반환
    return {
        "sorted_data": arr,
        "steps": steps,
        "complexity": "O(n^2)",
        "status": "단순 삽입 정렬 완료"
    }

# Cloud Run 환경에서 제공하는 PORT 환경 변수를 읽어와 서버 실행 (기본값: 8080)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
