# Simulated smart home devices

devices = {
    "lights": False,
    "fan": False
}


def turn_on(device):
    device = device.lower()

    if device in devices:
        devices[device] = True
        return f"{device.capitalize()} turned on."

    return f"{device.capitalize()} not found."


def turn_off(device):
    device = device.lower()

    if device in devices:
        devices[device] = False
        return f"{device.capitalize()} turned off."

    return f"{device.capitalize()} not found."


def get_status():
    status = []

    for device, state in devices.items():
        state_text = "ON" if state else "OFF"
        status.append(f"{device.capitalize()}: {state_text}")

    return status