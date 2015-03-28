# #------------------------------------------------------------------------------ 
# # 
# #  SimConnect AI Objects and Waypoints sample 
# #  
# #    Description: 
# #                Adds Non ATC controlled simulation objects. 
# #                With the default aircraft at Seatac  (KSEA)- turn off the engine 
# #                and watch the antics. 
# #                Press z to create the objects 
# #                Press x to load them with their waypoint lists 
# #------------------------------------------------------------------------------
# 
# import prepar3d 
# 
# if __name__ == '__main__':
#     
#     try:
#         # the connection closes either when it gets destroyed or if an SIMCONNECT_RECV_ID_QUIT event is received
#         prepar3d.Connection().open('AI Objects and Waypoints', auto_close=True)
#     except prepar3d.OpenConnectionException:
#         print('Uups! Is Prepar3d running?')
#         sys.exit(1) 
#         
#     print('Connected to Prepar3d!')  
#     
#     # This allows to start the script when sim is already running even with at_sim_start=True.
#     # Should be only used for testing purpose!
#     prepar3d.EventListener().set_allow_running_sim_for_all_events(True)  
#     
#     prepar3d.InputEvent('Z', callback=lambda e, d: print('Z'), at_sim_start=True)
#     prepar3d.InputEvent('X', callback=lambda e, d: print('X'), at_sim_start=True)
#     
#     prepar3d.EventListener().listen()
