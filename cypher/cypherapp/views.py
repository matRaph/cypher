import string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

lista = string.ascii_lowercase + string.ascii_uppercase+ string.digits + string.punctuation + ' '
lista = [i for i in lista]

class Cifrar(APIView):
    
    def cifrar(self, message, password):
        cifrado = ""
        senha_atual = int(password[0])
        for i in range(len(message)):
            char = message[i]
            index = lista.index(char)
            if index + senha_atual >= len(lista):
                index = (index + senha_atual) - len(lista)
                cifrado += lista[index]
            else:
                cifrado += lista[index + senha_atual]
            
            if senha_atual == int(password[1]):
                senha_atual = int(password[2])
            elif senha_atual == int(password[2]):
                senha_atual = int(password[0])
            else:
                senha_atual = int(password[1])
            
        return Response(cifrado, status=status.HTTP_200_OK)
    
    def get(self, request, format=None):
        message = request.query_params.get('message', None)
        password = request.query_params.get('password', None)
        if message is not None and password is not None:
            if len(password) == 3:
                return self.cifrar(message, password)
            else:
                return Response("Password must be 3 characters", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Message and password are required", status=status.HTTP_400_BAD_REQUEST)
        
class Decifrar(APIView):
        
        def decifrar(self, message, password):
            decifrado = ""
            senha_atual = int(password[0])
            for i in range(len(message)):
                char = message[i]
                index = lista.index(char)
                if index - senha_atual < 0:
                    index = len(lista) - (senha_atual - index)
                    decifrado += lista[index]
                
                else:
                    decifrado += lista[index - senha_atual]
                
                if senha_atual == int(password[1]):
                    senha_atual = int(password[2])
                elif senha_atual == int(password[2]):
                    senha_atual = int(password[0])
                else:
                    senha_atual = int(password[1])
                
            return Response(decifrado, status=status.HTTP_200_OK)
        
        def get(self, request, format=None):
            message = request.query_params.get('message', None)
            password = request.query_params.get('password', None)
            if message is not None and password is not None:
                if len(password) == 3:
                    return self.decifrar(message, password)
                else:
                    return Response("Password must be 3 characters", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Message and password are required", status=status.HTTP_400_BAD_REQUEST)