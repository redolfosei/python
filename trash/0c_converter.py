class Converter:
    def __init__(self,unit,lenght):
        pass
    
    
self.unit_value = {
            'inches':{
                'inches': 1,'centimeters':2.54,'feet':0.083,'kilometers':0.000025,'meters':0.025,
                'yards':0.02777778,'millimeters':25.4,'miles':0.00001578,
            },
            'feet':{
                'feet': 1,'centimeters':30.48,'inches':12,'kilometers':0.0003,'meters':0.3048,
                'yards':0.3333,'millimeters':304.8,'miles':0.000189,
            },
            'yards':{
                'yards': 1,'centimeters':91.44,'feet':3,'kilometers':0.00091,'meters':0.91,
                'inches':36,'millimeters':914.4,'miles':0.000568,
            },
            'miles':{
                'miles':1,'centimeters':160934.4,'feet':5280,'kilometers':1.60934,'meters':1609.344,
                'yards':1760,'millimeters':1.609344e+6,'inches':63360,
            },
            'kilometers':{
                'kilometers':1,'centimeters':100000,'feet':3280.84,'inches':39370.08,'meters':1000,
                'yards':1093.613,'millimeters':1e+6,'miles':0.6213712,
            },
            'meters':{
                'meters':1,'centimeters':100,'feet':3.28084,'kilometers':0.001,'inches':39.37008,
                'yards':1.093613,'millimeters':1000,'miles':0.00062137,
            },
            'centimeters':{
                'centimeters':1,'inches':0.39370,'feet':0.0328084,'kilometers':0.00001,'meters':0.01,
                'yards':0.01093613,'millimeters':10,'miles':6.213712e-6,
            },
            'millimeters':{
                'millimeters':1,'centimeters':0.1,'feet':0.00328084,'kilometers':1e-6,'meters':0.001,
                'yards':0.00109361,'inches':0.03937008,'miles':6.213712e-7,
            },
        }