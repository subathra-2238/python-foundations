class MessagePartitioner:

    def __init__(self, partition_count):
        self.partition_count = partition_count
        self.partitions = {
            i: [] for i in range(partition_count)
        }

    def add_message(self, key, message):

        partition_id = hash(key) % self.partition_count

        self.partitions[partition_id].append(message)

        print(
            f"{message} -> Partition {partition_id}"
        )

    def show_partitions(self):

        print("\nPartition Details:")

        for partition_id, messages in self.partitions.items():
            print(f"Partition {partition_id}: {messages}")


partitioner = MessagePartitioner(3)

partitioner.add_message("AI", "Message 101")
partitioner.add_message("Robotics", "Message 102")
partitioner.add_message("AI", "Message 103")
partitioner.add_message("IoT", "Message 104")
partitioner.add_message("Robotics", "Message 105")

partitioner.show_partitions()
