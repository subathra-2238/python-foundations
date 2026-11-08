import json


class MessageSerializer:

    def serialize(self, message):

        serialized_data = json.dumps(message)

        print("Serialized Message:")
        print(serialized_data)

        return serialized_data

    def deserialize(self, data):

        message = json.loads(data)

        print("\nDeserialized Message:")
        print(message)

        return message


serializer = MessageSerializer()

message = {
    "id": 101,
    "sender": "Subathra",
    "content": "Hello from AI department",
    "priority": "High"
}

data = serializer.serialize(message)

serializer.deserialize(data)
