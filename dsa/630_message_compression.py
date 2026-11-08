import zlib


class MessageCompressor:

    def compress_message(self, message):

        original_data = message.encode("utf-8")

        compressed_data = zlib.compress(original_data)

        print("Original Size:", len(original_data), "bytes")
        print("Compressed Size:", len(compressed_data), "bytes")

        return compressed_data

    def decompress_message(self, compressed_data):

        original_data = zlib.decompress(compressed_data)

        message = original_data.decode("utf-8")

        print("\nDecompressed Message:")
        print(message)


compressor = MessageCompressor()

message = "AI and Machine Learning " * 20

compressed = compressor.compress_message(message)

compressor.decompress_message(compressed)
