from imports import Flask, Api, Response, Resource
from baymax import run_baymax

app = Flask(__name__)
api = Api(app)


######################
#get run_baymax()
######################
class GetAll(Resource):
    def get(self):
        try:
            return Response(
                response=(run_baymax()+"I'm working"),
                status=200,
                mimetype="application/json",
            )
        except Exception as e:
            print(e)
            return Response(
                response=(e),
                status=404,
                mimetype="application/json",
            )

######################
##api call
######################
api.add_resource(GetAll, "/")

if __name__ == "__main__":
    app.run(debug=True)