import grpc
from concurrent import futures
import time
import meter_pb2_grpc as pb2_grpc
import meter_pb2 as pb2


class UnaryService(pb2_grpc.MeasurementService):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        # message = request.from
        # toStr = request.to
        # result = f'Hello I am up and running received "{message}" message from you'
        # result = {'message': result, 'received': True}
        result = pb2.MeterList()
        # result.start = 
        # result.end =

        return pb2.MeterList(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MeasurementServiceServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()


# python3 -m grpc_tools.protoc --proto_path=. ./meter.proto --python_out=. --grpc_python_out=.
