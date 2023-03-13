from flask import Flask
from flask_restful import Resource, Api, reqparse



app = Flask("VideoAPI")
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)

videos = {
    'video1' : {'title': 'Hello World in Python'},
    'video2': {'title':'Hi Jules'}
}


class Video(Resource):

    def get(self, video_id):
        if video_id == "all":
            return videos
        return videos[video_id]
    

    def put(self, video_id):
        args = parser.parse_args()
        if not args['title']:
            return {'message': 'Title is required'}, 400
        if not isinstance(args['title'], str):
            return {'message': 'Title must be a string'}, 400

        new_video = {'title': args['title']}
        videos[video_id].update(new_video)
        return {video_id: videos[video_id]}, 201
    
    def delete(self,video_id):
        if video_id not in videos:
            pass
    
api.add_resource(Video, '/videos/<video_id>')



if __name__ == '__main__':
    app.run()