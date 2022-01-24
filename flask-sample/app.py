from flask import Flask, request, Response
from flask_restx import Resource, Api, fields
from flask import abort
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
api = Api(app)

# 영화 정보 데이터가 들어갈 모델을 설정
movie_data = api.model(
    'Movie Data',
    {   
        "name": fields.String(description="movie name", required=True),
        "desc": fields.String(description="movie description", required=True),
        "img_url": fields.String(description="image URL", required=True),
    }
)

movie_info = {}
movieCount = 0

@api.route('/movies')
class Movies(Resource):
# 등록된 모든 영화 정보 조회
    def get(self):
        return {
            'movieCount' : movieCount,
            'data' : movie_info,
        }

@api.route('/movies/<int:id>')
class MoivesResource(Resource):
# id에 해당하는 영화에 대한 정보 조회
    def get(self, id):
        if not id in movie_info.keys():
            abort(404, description=f"Movie {id} doesn't exists")
        data = movie_info[id]

        return {
            'data': data
        }
    
# id에 영화 제목, 설명, 사진url에 대한 정보를 입력
    @api.expect(movie_data)
    def post(self, id):
        if id in movie_info.keys():
            abort(409, description=f"Movie {id} already exists")
        
        movie_info[id] = dict()
        params = request.get_json()
        movie_info[id] = params
        global movieCount
        movieCount += 1
        
        return Response(status=200)
		
# id에 해당하는 영화 정보를 변경
    @api.expect(movie_data)
    def put(self, id):
        if not id in movie_info.keys():
            abort(404, description=f"Movie {id} doesn't exists")
        
        del movie_info[id]
        params = request.get_json()
        movie_info[id] = params

        return Response(status=201)
	
# id에 해당하는 영화 정보를 삭제
    def delete(self, id):
        if not id in movie_info.keys():
            abort(404, description=f"Movie {id} doesn't exists")

        del movie_info[id]

        global movieCount
        movieCount -= 1
        
        return Response(status=200)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)