# from prepar3d._internal import simconnect
# from prepar3d._internal.simconnect import DispatchHandler
# from prepar3d._internal.id import Id
# from prepar3d.event_listener import EventListener
# 
# class RadiusData:
#     
#     def __init__(self, variables, radius, object_type=simconnect.SIMCONNECT_SIMOBJECT_TYPE.SIMCONNECT_SIMOBJECT_TYPE_AIRCRAFT):
#         self._object_type = object_type
#         self._variables = variables
#         self._radius = radius
#         self._id = Id().get('RadiusData')
#         self._data_definition_id = Id().get('DataDefintiion')
#         self._data = dict()
#         
#         EventListener()._dispatch_handler.subscribeRadiusData(self)
