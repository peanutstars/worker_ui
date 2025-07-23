from flask import Flask, request, jsonify, render_template
from core.log import Log
from core.model import ApiRequestResponse

print = Log.info


app = Flask(__name__)
   
# @app.route('/')
# def index():
#     # templates/index.html 파일을 렌더링
#     return render_template('index.html')

@app.route('/')
def index():
    # templates/index.html 파일을 렌더링
    return render_template('index2.html')

# /v1/api/job 엔드포인트: POST 요청 처리 및 JSON 데이터 응답
@app.route('/v1/api/request', methods=['POST'])
def handle_job_post_and_respond():
    api_response = ApiRequestResponse()
    
    # 클라이언트가 보낸 요청 본문 데이터 로깅 (선택 사항)
    try:
        client_data = request.get_json(silent=True) # silent=True는 JSON 파싱 실패 시 None 반환
        if client_data:
            print(f"클라이언트로부터 받은 데이터 (POST 본문): {client_data}")
            print(f"클라이언트 Request: {client_data.get('request')}")
            api_response.request = client_data.get('request')
        else:
            print("클라이언트로부터 JSON 데이터가 수신되지 않았거나 형식이 올바르지 않습니다.")
            print(f"Content-Type: {request.headers.get('Content-Type')}")
            print(f"Request Data: {request.get_data(as_text=True)}") # JSON이 아닌 경우 원본 데이터 확인
    except Exception as e:
        api_response.message = f'Error in parsing: {e}'
        print(f"{api_response.message}")
    
    if api_response.request == "job":   
        # 클라이언트에게 전달할 JSON 데이터 정의
        data = {
            "tasks": [
                {
                    "cancelable": True,
                    "expectDuration": 15,
                    "instant": False,
                    "nextFail": "",
                    "nextOk": "",
                    "properties": "{\"position\":\"charger_station_A\"}",
                    "taskId": "undock.0001",
                    "taskName": "Undock from Charger",
                    "taskType": "undock"
                },
                {
                    "cancelable": False,
                    "expectDuration": 60,
                    "instant": True,
                    "nextFail": "error_state_B",
                    "nextOk": "success_state_C",
                    "properties": "{\"mapName\":\"main_warehouse\",\"position\":\"packing_area\",\"btName\":\"route_to_packing\"}",
                    "taskId": "gotoposition.0001",
                    "taskName": "Move to Packing Area",
                    "taskType": "gotoposition"
                }
            ]
        }
        api_response.success = True
        api_response.value = data
    else:
        api_response.success = False
        if not api_response.message:
            api_response.message = f"unknown request[{api_response.request}]"

    print(f"클라이언트에 보낼 JSON 데이터: {api_response.to_json()}")

    # jsonify를 사용하여 Python 딕셔너리를 JSON 형식의 HTTP 응답으로 변환
    return jsonify(api_response.data()), 200 # HTTP 상태 코드 200 (OK)과 함께 전송

if __name__ == '__main__':
    Log.info(f'Start !!')
    app.run(host='0.0.0.0', port=5000, debug=True)