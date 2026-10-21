가볍고 안정적인 Python 3.9 슬림 버전을 기반 이미지로 사용합니다.

FROM python:3.9-slim

컨테이너 내 작업 디렉토리를 /app으로 설정합니다.

WORKDIR /app

파이썬 라이브러리 설치를 위해 requirements.txt 파일을 복사합니다.

COPY requirements.txt .

pip를 이용해 필수 패키지를 캐시 없이 설치합니다.

RUN pip install --no-cache-dir -r requirements.txt

나머지 모든 소스 코드를 컨테이너의 /app 디렉토리로 복사합니다.

COPY . .

Cloud Run 표준 포트인 8080을 외부로 개방합니다.

EXPOSE 8080

uvicorn 웹 서버를 통해 FastAPI 애플리케이션을 구동합니다.

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
