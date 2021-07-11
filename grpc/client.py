import grpc, ciso8601
import meter_pb2_grpc as pb2_grpc
import meter_pb2 as pb2

from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.json_format import MessageToJson


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.MeasurementServiceStub(self.channel)

    def get_url(self, start, end):
        """
        Client function to call the rpc for GetServerResponse
        """
        ts_start = Timestamp()
        ts_end = Timestamp()

        ts_start.FromDatetime(ciso8601.parse_datetime(start))
        ts_end.FromDatetime(ciso8601.parse_datetime(end))

        message = pb2.MeterList(start=ts_start, end=ts_end)
        print(f'message: {message} start: {ts_start} end: {ts_end}')
        return self.stub.GetServerResponse(message)



if __name__ == '__main__':
    client = UnaryClient()
    start = "2019-01-01 00:00:00"
    end = "2019-01-01 02:00:00"

    result = client.get_url(start, end)
    print(f'{MessageToJson(result)}')
