# ########################################################################################################
# ########################################################################################################
# # API Created by Techrism - https://github.com/techchrism/valorant-api-docs
# #                           https://valapidocs.techchrism.me/
# #
# #
# ########################################################################################################
# ########################################################################################################
# import json
# import os
# import asyncio
# import requests
# import websocket
# import certifi
# import base64
# import ssl


# class TechrismApi():

#     def __init__(self):
#         # Setup WebSockets Use
#         self.ws = websocket.WebSocket()

#         # Certificates
#         self.certs = certifi.where()
#         # Set Location of Lockfile
#         user = "ismai"
#         self.lockfile_location = fr"C:\Users\{user}\AppData\Local\Riot Games\Riot Client\Config\lockfile"

#         # Define Structure of Lockfile to input into Dictionary
#         self.lockfile_structure = [
#             "name", "pid", "port", "password", "protocol"]
#         self.lockfile = {}
#         try:
#             # Open and extract Lockfile Information
#             with open(self.lockfile_location) as f:
#                 f = f.readlines()
#                 f = f[0].split(":")
#                 for index in range(0, len(f)):
#                     self.lockfile.update(
#                         {self.lockfile_structure[index]: f[index]})

#             # print(self.lockfile_dict["name"])

#             # self.ws = create_connection(
#             #     f"wss://riot:{self.lockfile['password']}@localhost:{self.lockfile['port']}")

#             # WebSocket URL
#             self.url = f"wss://riot:{self.lockfile['password']}@localhost:{self.lockfile['port']}"
#         except Exception as e:
#             print(e)

#     async def test(self):

#         ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#         ssl_context.check_hostname = False
#         ssl_context.verify_mode = ssl.CERT_NONE

#         print(self.lockfile)
#         local_headers = {
#             'Authorization': (
#                 'Basic ' +
#                 base64.b64encode(
#                     ('riot:' + self.lockfile['password']).encode()).decode()
#             )
#         }
#         self.ws.connect(
#             f"wss://127.0.0.1:{self.lockfile['port']}/entitlements/v1/token", sslopt=ssl_context, header=local_headers)

#         # r = requests.get(f"https://127.0.0.1:{self.lockfile['port']}/entitlements/v1/token", verify=self.certs, headers={
#         #                  "riot": f"{self.lockfile['password']}"})
#         # print("R: ", r)
#         # async with websockets.connect(self.url) as ws:
#         #     msg = await ws.recv()
#         #     print(msg)


# if __name__ == "__main__":
#     api = TechrismApi()

#     asyncio.get_event_loop().run_until_complete(api.test())
