{
  "version": "1.1",
  "package": {
    "name": "",
    "version": "",
    "description": "",
    "author": "",
    "image": ""
  },
  "design": {
    "board": "icezum",
    "graph": {
      "blocks": [
        {
          "id": "79fa0b2e-5b82-46cb-9dcc-4bb88c9040ad",
          "type": "basic.input",
          "data": {
            "name": "Boton",
            "pins": [
              {
                "index": "0",
                "name": "D13",
                "value": "144"
              }
            ],
            "virtual": false,
            "clock": false
          },
          "position": {
            "x": 272,
            "y": 72
          }
        },
        {
          "id": "e853e03a-c5c6-4186-ab6f-0f340409e01d",
          "type": "basic.output",
          "data": {
            "name": "Debug",
            "pins": [
              {
                "index": "0",
                "name": "D0",
                "value": "119"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 544,
            "y": 72
          }
        },
        {
          "id": "eb9f6617-3172-4b2e-853a-578087b572a1",
          "type": "basic.output",
          "data": {
            "name": "LED",
            "pins": [
              {
                "index": "0",
                "name": "LED0",
                "value": "95"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 544,
            "y": 144
          }
        }
      ],
      "wires": [
        {
          "source": {
            "block": "79fa0b2e-5b82-46cb-9dcc-4bb88c9040ad",
            "port": "out"
          },
          "target": {
            "block": "e853e03a-c5c6-4186-ab6f-0f340409e01d",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "79fa0b2e-5b82-46cb-9dcc-4bb88c9040ad",
            "port": "out"
          },
          "target": {
            "block": "eb9f6617-3172-4b2e-853a-578087b572a1",
            "port": "in"
          }
        }
      ]
    },
    "state": {
      "pan": {
        "x": -42,
        "y": 95.5
      },
      "zoom": 1
    }
  },
  "dependencies": {}
}