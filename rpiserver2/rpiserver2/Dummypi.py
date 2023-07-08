class GPIO:
    OUT = "OUT"
    HIGH = "HIGH"
    LOW = "LOW"
    BCM = "BCM"

    def setup(gpio, mode):
        print(f"Setting up pin {gpio} a {mode}")

    def output(pin, state):
        print(f"Setting pin {pin} to {state}")

    def setmode(BCM):
        print(f"Setear el modo {BCM}")

    def setwarnings(state):
        print(f"Setear warnings en {state}")
