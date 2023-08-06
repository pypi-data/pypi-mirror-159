# import yaml
#
# from src.mdm.consulta import Consulta
#
# if __name__ == '__main__':
#     consultas = open("configuracion/consultas.yaml", "r", encoding="utf-8")
#     consultas = yaml.safe_load(consultas)
#     consulta = Consulta(consultas)

import requests

# curl -X POST "http://192.168.56.1/sdmx_172/ws/NODE_API/api/Security/Authenticate"
# -H  "accept: */*" -H  "Content-Type: application/json"
# -H "nodeId: 01" -d "{\"username\": \"admin\",  \"password\": \"\", }"

url = 'http://192.168.56.1/sdmx_172/ws/NODE_API/api/Security/Authenticate'
headers = {'Content-Type': 'application/json', 'nodeid': '01'}
data = {'username': 'admin', 'password': ''}

auth = requests.request(method='POST', url=url, headers=headers, data=data)
print(auth.headers)
print(auth.content)