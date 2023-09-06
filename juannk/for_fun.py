class BinaryDecoder:
    def __init__(self, num_bits, num_outputs):
        self.num_bits = num_bits
        self.num_outputs = num_outputs
        self.outputs = [0] * self.num_outputs

    def decode(self, binary_input):
        decimal_input = int(binary_input, 2)
        self._update_outputs(decimal_input)

    def _update_outputs(self, decimal_input):
        self.outputs = [0] * self.num_outputs
        self.outputs[decimal_input] = 1


class Decoder2to4(BinaryDecoder):
    def __init__(self):
        super().__init__(2, 4)

    def get_output(self):
        return self.outputs


class Decoder3to8(BinaryDecoder):
    def __init__(self):
        super().__init__(3, 8)

    def get_output(self):
        return self.outputs


class Decoder4to16(BinaryDecoder):
    def __init__(self):
        super().__init__(4, 16)

    def get_output(self):
        return self.outputs


# Example usage
def main():
    # 2-to-4 Decoder
    decoder2to4 = Decoder2to4()
    binary_input = input("Enter a 2-bit binary value: ")
    decoder2to4.decode(binary_input)
    output = decoder2to4.get_output()
    print("2-to-4 Decoder ({0}): {1}".format(binary_input, output))

    # 3-to-8 Decoder
    decoder3to8 = Decoder3to8()
    binary_input = input("Enter a 3-bit binary value: ")
    decoder3to8.decode(binary_input)
    output = decoder3to8.get_output()
    print("3-to-8 Decoder ({0}): {1}".format(binary_input, output))

    # 4-to-16 Decoder
    decoder4to16 = Decoder4to16()
    binary_input = input("Enter a 4-bit binary value: ")
    decoder4to16.decode(binary_input)
    output = decoder4to16.get_output()
    print("4-to-16 Decoder ({0}): {1}".format(binary_input, output))


if __name__ == '__main__':
    main()
