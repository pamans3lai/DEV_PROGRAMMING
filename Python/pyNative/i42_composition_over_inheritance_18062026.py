class CPU:
    def __init__(self, model):
        self.model = model


class RAM:
    def __init__(self, size):
        self.size = size


class Computer:
    def __init__(self, cpu_model, ram_size):
        # The Computer "has" a CPU and RAM
        self.cpu = CPU(cpu_model)
        self.ram = RAM(ram_size)

    def __str__(self):
        return f"Computer with {self.cpu.model} CPU and {self.ram.size} RAM."


# penggunaan
my_pc = Computer("Inter i7", "16GB")
print(my_pc)
