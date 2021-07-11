import grpc
from concurrent import futures
import time
import meter_pb2_grpc as pb2_grpc
import meter_pb2 as pb2
from google.protobuf.json_format import MessageToDict
from service import get_measurement
import traceback


class UnaryService(pb2_grpc.MeasurementService):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        print(f"GetServerResponse Request: {MessageToDict(request)}")

        result = pb2.MeterList(start=request.start, end=request.end)
        try:
            meter_list = get_measurement(result.start.seconds, result.end.seconds)
            # print(f"get_measurement {meter_list}")
            result.list.extend(meter_list)
        except Exception as ex:
            print(f'GetServerResponse Exception {ex}')
            traceback.print_stack()

        print(f"GetServerResponse Length: {len(result.list)}")

        return result


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MeasurementServiceServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server starting")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()


# python3 -m grpc_tools.protoc --proto_path=. ./meter.proto --python_out=. --grpc_python_out=.
