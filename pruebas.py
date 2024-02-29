import convert

x = {
  "nombre": "Juan",
  "edad": 30,
  "ciudad": "Ciudad de México",
  "casado": False,
  "hobbies": ["correr", "leer", "jugar fútbol"],
  "dirección": {
    "calle": "Calle Principal",
    "número": 123,
    "colonia": "Centro"
  }
}
x1 = {
  "nombre": "Juan",
  "edad": 30,
  "ciudad": "Ciudad de México",
  "casado": False,
  "hobbies": ["correr", "leer", "jugar fútbol"],
  "dirección": {
    "calle": "Calle Principal",
    "número": 123,
    "colonia": "Centro"
  }
}
x3 = {
  "empresa": "Acme Corporation",
  "empleados": [
    {
      "nombre": "Ana",
      "edad": 35,
      "cargo": "Gerente"
    },
    {
      "nombre": "Pedro",
      "edad": 28,
      "cargo": "Desarrollador"
    },
    {
      "nombre": "María",
      "edad": 30,
      "cargo": "Diseñadora"
    }
  ],
  "ubicación": {
    "ciudad": "Ciudad de México",
    "país": "México"
  }
}

json_x = convert.create('index.json',x)

json_x1 = convert.update('index1.json',x1,x3)

json_x2 = convert.read('index1.json')
print(json_x2)