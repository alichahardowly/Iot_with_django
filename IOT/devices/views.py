from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SmartDevice
import paho.mqtt.publish as publish

MQTT_BROKER = "broker.hivemq.com"  

@api_view(['GET'])
def device_list(request):
    devices = SmartDevice.objects.all()
    data = [{"id": d.id, "name": d.name, "status": d.status} for d in devices]
    return Response(data)

@api_view(['POST'])
def toggle_device(request, device_id):
    try:
        device = SmartDevice.objects.get(id=device_id)
        device.status = not device.status  
        device.save()
    
        publish.single(device.topic, "ON" if device.status else "OFF", hostname=MQTT_BROKER)
        
        return Response({"message": f"{device.name} {'on' if device.status else 'off'} "})
    except SmartDevice.DoesNotExist:
        return Response({"error": "devicer not fond"}, status=404)
