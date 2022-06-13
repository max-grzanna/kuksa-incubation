# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from sdv.edge.comfort.hvac.v1 import (
    hvac_pb2 as sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2,
)


class HvacStub(object):
    """*
    @brief Example HVAC service for controlling the heating, ventilation, and air
    conditioning elements of the vehicle cabin.
    This definition is designed here according to the draft of the comfort seats
    service definition of the COVESA Vehicle Service Catalog (VSC) (see
    https://github.com/COVESA/vehicle_service_catalog) as a definition of an
    HVAC service is currently missing in VSC.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAcStatus = channel.unary_unary(
            "/sdv.edge.comfort.hvac.v1.Hvac/SetAcStatus",
            request_serializer=sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetAcStatusRequest.SerializeToString,
            response_deserializer=sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetAcStatusReply.FromString,
        )
        self.SetTemperature = channel.unary_unary(
            "/sdv.edge.comfort.hvac.v1.Hvac/SetTemperature",
            request_serializer=sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetTemperatureRequest.SerializeToString,
            response_deserializer=sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetTemperatureReply.FromString,
        )


class HvacServicer(object):
    """*
    @brief Example HVAC service for controlling the heating, ventilation, and air
    conditioning elements of the vehicle cabin.
    This definition is designed here according to the draft of the comfort seats
    service definition of the COVESA Vehicle Service Catalog (VSC) (see
    https://github.com/COVESA/vehicle_service_catalog) as a definition of an
    HVAC service is currently missing in VSC.
    """

    def SetAcStatus(self, request, context):
        """* Set the desired ac status

        Returns gRPC status codes:
        * OK - AcStatus set
        * INVALID_ARGUMENT - The requested AcStatus is not supported by the service instance
        * INTERNAL - A HVAC service internal error happened - see error message for details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SetTemperature(self, request, context):
        """* Set the desired cabin temperature

        Returns gRPC status codes:
        * OK - Desired temperature set
        * OUT_OF_RANGE - The specified temperature is not supported in this vehicle
        * INTERNAL - A HVAC service internal error happened - see error message for details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_HvacServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SetAcStatus": grpc.unary_unary_rpc_method_handler(
            servicer.SetAcStatus,
            request_deserializer=sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetAcStatusRequest.FromString,
            response_serializer=sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetAcStatusReply.SerializeToString,
        ),
        "SetTemperature": grpc.unary_unary_rpc_method_handler(
            servicer.SetTemperature,
            request_deserializer=sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetTemperatureRequest.FromString,
            response_serializer=sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetTemperatureReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "sdv.edge.comfort.hvac.v1.Hvac", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Hvac(object):
    """*
    @brief Example HVAC service for controlling the heating, ventilation, and air
    conditioning elements of the vehicle cabin.
    This definition is designed here according to the draft of the comfort seats
    service definition of the COVESA Vehicle Service Catalog (VSC) (see
    https://github.com/COVESA/vehicle_service_catalog) as a definition of an
    HVAC service is currently missing in VSC.
    """

    @staticmethod
    def SetAcStatus(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sdv.edge.comfort.hvac.v1.Hvac/SetAcStatus",
            sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetAcStatusRequest.SerializeToString,
            sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetAcStatusReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SetTemperature(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sdv.edge.comfort.hvac.v1.Hvac/SetTemperature",
            sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetTemperatureRequest.SerializeToString,
            sdv_dot_edge_dot_comfort_dot_hvac_dot_v1_dot_hvac__pb2.SetTemperatureReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
