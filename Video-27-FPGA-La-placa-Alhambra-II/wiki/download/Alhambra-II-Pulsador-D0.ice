{
  "version": "1.2",
  "package": {
    "name": "",
    "version": "",
    "description": "",
    "author": "",
    "image": ""
  },
  "design": {
    "board": "alhambra-ii",
    "graph": {
      "blocks": [
        {
          "id": "13f39244-cb80-4b39-b2a7-ec0e977a7047",
          "type": "basic.output",
          "data": {
            "name": "LED",
            "pins": [
              {
                "index": "0",
                "name": "LED0",
                "value": "45"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 472,
            "y": 216
          }
        },
        {
          "id": "c3fb54bb-bd67-4073-b3a3-fef894f58ea1",
          "type": "basic.input",
          "data": {
            "name": "Pulsador",
            "pins": [
              {
                "index": "0",
                "name": "D0",
                "value": "2"
              }
            ],
            "virtual": false,
            "clock": false
          },
          "position": {
            "x": 264,
            "y": 216
          }
        },
        {
          "id": "6449fa94-5c28-4c21-b5ec-871a3fbb993d",
          "type": "basic.info",
          "data": {
            "info": "## Ejemplo de conexión de un Pulsador externo\n\nCada vez que se aprieta el pulsador D0 se encience el LED0",
            "readonly": true
          },
          "position": {
            "x": 192,
            "y": 88
          },
          "size": {
            "width": 544,
            "height": 80
          }
        }
      ],
      "wires": [
        {
          "source": {
            "block": "c3fb54bb-bd67-4073-b3a3-fef894f58ea1",
            "port": "out"
          },
          "target": {
            "block": "13f39244-cb80-4b39-b2a7-ec0e977a7047",
            "port": "in"
          }
        }
      ]
    }
  },
  "dependencies": {}
}