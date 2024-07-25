import platform
import pyopencl as cl
import GPUtil

gpu_found = GPUtil.getGPUs()

def remove_letters(string):
    result = ''
    for char in string:
        if char.isdigit():
            result += char
    return result

gpu_found = False
RAM = 0

with open("/proc/meminfo") as ram:
    RAM2 = ram.read()[17:26]
    RAM2 = remove_letters(RAM2)
    ram = int(RAM2) // (1024 ** 2) + 1
    del RAM2
print("CPU:", platform.processor())
print("Architecture:", platform.architecture())
print("OS:", platform.system())
print("RAM:", ram, "GB")

if gpu_found:

 def list_opencl_devices():
     platforms = cl.get_platforms()
     if not platforms:
         print("No OpenCL platforms found.")
         return
 
     for platform in platforms:
         print(f"Platform: {platform.name}")
         try:
             devices = platform.get_devices()
         except cl.RuntimeError as e:
             print(f"  Failed to get devices for platform: {e}")
             continue
 
         for device in devices:
             device_type = "GPU" if device.type == cl.device_type.GPU else "CPU"
             print(f"  {device_type} Device: {device.name}")

 def main():
     list_opencl_devices()
     platforms = cl.get_platforms()
     if not platforms:
         print("OpenCL platforms not found. Cannot proceed.")
         return
    
    # Attempt to find a GPU device
     gpu_devices = [device for platform in platforms for device in platform.get_devices(device_type=cl.device_type.GPU)]
     if not gpu_devices:
         print("No GPU devices found. Looking for CPU devices...")
         cpu_devices = [device for platform in platforms for device in platform.get_devices(device_type=cl.device_type.CPU)]
         if cpu_devices:
             print(f"Found CPU device: {cpu_devices[0].name}")
            # Initialize your context here using a CPU device
            # e.g., ctx = cl.Context(devices=cpu_devices)
         else:
             print("No CPU devices found either. Cannot proceed.")
             return
     else:
         print(f"Found GPU device: {gpu_devices[0].name}")
        # Initialize your context here using a GPU device
        # e.g., ctx = cl.Context(devices=gpu_devices)

 if __name__ == "__main__":
     main()

else: 
     print("GPU not found.")