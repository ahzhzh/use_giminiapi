import os
import google.generativeai as genai

from giminiapi_chatbot import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

response = model.generate_content([
  "input: 램이란?",
  "output: 사용자가 자유롭게 내용을 읽고 쓰고 지울 수 있는 기억장치.",
  "input: 메인보드란?",
  "output: 모든 하드웨어를 프로세서와 연결하고, 전원이 공급하는 전기를 분배",
  "input: 사운드카드란?",
  "output: 소리를 저장하고 출력하는 기능을 수행",
  "input: cpu란?",
  "output: 컴퓨터의 두뇌 역할을 하는 장치",
  "input: 그래픽카드란?",
  "output: 그래픽 정보를 컴퓨팅하는 방법을 간단히 제공",
  "input: 하드디스크란?",
  "output: 파일과 데이터를 장기적으로 저장하는 데 필요한 저장 장치",
  "input: 과자",
  "output: 먹을거",
  "input: 수영",
  "output: 운동",
  "input: cpu란?",
  "output: CPU는 컴퓨터의 두뇌 역할을 하는 장치입니다. 컴퓨터의 모든 연산을 처리하고 명령을 실행하는 중앙 처리 장치입니다.",
  "input: 축구",
  "output: 운동",
  "input: amd 라이젠 버전 종류",
  "output: 라이젠 9, 7, 5가 있다",
  "input: 인텔 cpu 버전 종류",
  "output: 인텔 코어 i9, i7, i5가 있다",
  "input: 인텔 cpu 장점",
  "output: 성능과 안정성이 좋다",
  "input: 인텔 cpu 단점",
  "output: 가격이 상대적으로 높다",
  "input: 라이젠cpu 장점",
  "output: 가성비가 좋다",
  "input: 라이젠cpu단점",
  "output: 호환성과 최적화에 문제가 있을 수 있다",
  "input: 배고프다",
  "output: 밥먹어",
  "input: 졸리다",
  "output: 잠자",
  "input: 안녕하세요",
  "output: 안녕하세요",
  "input: 음성인식봇",
  "output: 만드는방법",
  "input: cpu란?",
  "output: ",
])

print(response.text)