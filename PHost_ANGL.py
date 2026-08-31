
import wmi
import time
import os

from PONT import pont_angl
from colorama import Fore, init

init()

vid_dict = {
    "046D": "Logitech",
    "05AC": "Apple",
    "04A9": "Canon",
    "045E": "Microsoft",
    "054C": "Sony",
    "1F3A": "Onda / Générique",
    "0BDA": "Realtek",
    "18D1": "Google / Android",
    "0E8D": "MediaTek",
    "12D1": "Huawei",
    "22B8": "Motorola",
    "0489": "Foxconn / Bluetooth",
    "057E": "Nintendo",
    "0403": "Future Technology Devices Intl",
    "0409": "NEC Corporation",
    "043E": "Dell",
    "04E8": "Samsung Electronics",
    "0781": "SanDisk",
    "0930": "Pixart Imaging",
    "1532": "Razer USA Ltd.",
    "1668": "ASUS",
    "17EF": "Lenovo",
    "17F9": "TP-Link",
    "1B1C": "Corsair",
    "1C4F": "Synaptics",
    "1D6B": "Linux Foundation",
    "1E7D": "MSI",
    "1FC9": "Sony Interactive Entertainment",
    "20D6": "SteelSeries ApS",
    "24AE": "Microsoft Corporation",
    "24C6": "Roku, Inc.",
    "27C6": "Western Digital",
    "2A70": "Sony Corporation",
    "2E3C": "HTC Corporation",
    "2FD4": "Amazon Technologies",
    "319B": "AMD",
    "3297": "Garmin International",
    "3842": "Cooler Master Technology",
    "413C": "Dell",
    "1A2C": "Google, Inc.",
    "04CA": "ASUSTek COMPUTER INC.",
    "1B3F": "TP-Link Technologies",
    "0451": "Texas Instruments",
    "056E": "Elecom Co., Ltd.",
    "058F": "Alcor Micro Corp.",
    "05E3": "Genesys Logic, Inc.",
    "06CB": "Acer, Inc.",
    "093A": "Pixart Imaging",
    "0B05": "ASUSTek Computer",
    "0C45": "Microdia",
    "0D8C": "Alps Electric Co., Ltd.",
    "0E0F": "Kingston Technology",
    "0FCE": "ASUSTek Computer Inc.",
    "1058": "Western Digital Technologies",
    "174C": "Sony Ericsson Mobile Communications",
    "1915": "Sony Mobile Communications AB",
    "1B96": "Samsung Electronics Co., Ltd.",
    "1D50": "OpenMoko, Inc.",
    "2001": "D-Link Corp.",
    "2222": "HTC Corporation",
    "24AA": "Google Inc.",
    "2C7C": "Logitech",
    "2E17": "ASUSTek Computer Inc.",
    "303A": "Logitech",
    "3202": "Logitech",
    "413D": "Dell Inc.",
    "413E": "Dell Inc.",
    "413F": "Dell Inc.",
    "413B": "Dell Inc.",
    "413A": "Dell Inc.",
    "4137": "Dell Inc.",
    "4139": "Dell Inc.",
    "4138": "Dell Inc.",
    "4135": "Dell Inc.",
    "4134": "Dell Inc.",
    "4136": "Dell Inc.",
    "4132": "Dell Inc.",
    "4133": "Dell Inc.",
    "1FCF": "SteelSeries",
    "046A": "Phison Electronics Corp.",
    "05E0": "Creative Labs",
    "07AA": "Harman International",
    "0951": "Kingston Technology",
    "0CCD": "Alcor Micro Corp.",
    "0E8F": "Samsung Electronics Co., Ltd.",
    "1BCF": "Bitmain Technologies Inc.",
    "201E": "Logitech, Inc.",
    "24F5": "Harman International",
    "27B8": "Gigabyte Technology",
    "0FCE": "ASUSTek Computer Inc.",
    "04F2": "Chicony Electronics",
    "03F0": "Hewlett-Packard",
    "103C": "Hewlett-Packard",
    "1058": "Western Digital",
    "05AC": "Apple Inc.",
    "12D1": "Huawei Technologies",
    "1915": "Sony Mobile Communications",
    "04F3": "Elan Microelectronics",
    "0451": "Texas Instruments",
    "0BDA": "Realtek Semiconductor Corp.",
    "0A12": "Cambridge Silicon Radio",
    "04B4": "Fujitsu",
    "0402": "Creative Labs, Inc.",
    "045E": "Microsoft Corp.",
    "0461": "Philips",
    "04E8": "Samsung",
    "0E8F": "Samsung Electronics",
    "1D6B": "Linux Foundation / Generic",
    "17EF": "Lenovo Group Ltd.",
    "1C4F": "Synaptics, Inc.",
    "1B3F": "TP-Link",
    "05AC": "Apple Inc.",
    "0FCE": "ASUS",
    "0A5C": "Broadcom Corp.",
    "0CF3": "Huawei Device Co., Ltd.",
    "1050": "Creative Technology Ltd.",
    "046D": "Logitech, Inc.",
    "045E": "Microsoft",
    "04A3": "Samsung Techwin",
    "1BCF": "Bitmain",
    "1FCF": "SteelSeries, Inc."
}

c = wmi.WMI()
log_file_path = os.path.join(os.getcwd(), "peripherals_log.txt")


def log(message):
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def list_peripherals():
    peripherals = {}
    for p in c.Win32_PnPEntity():
        try:
            device_id = p.DeviceID
            vid = "????"
            if "VID_" in device_id:
                vid = device_id.split("VID_")[1][:4].upper()
            brand = vid_dict.get(vid, "Unknown")

            peripherals[device_id] = {
                "Name": p.Name or "Unknown",
                "Description": p.Description or "Unknown",
                "Manufacturer": getattr(p, "Manufacturer", "Unknown"),
                "Class": p.PNPClass or "Not specified",
                "Status": p.Status or "Unknown",
                "Caption": p.Caption or "N/A",
                "Hardware ID": p.DeviceID,
                "Compatible ID": getattr(p, "CompatibleID", "Unknown"),
                "Class GUID": getattr(p, "ClassGuid", "Unknown"),
                "Error Code": getattr(p, "ConfigManagerErrorCode", "Unknown"),
                "Location": getattr(p, "LocationInformation", "Unknown"),
                "Service": getattr(p, "Service", "Unknown"),
                "Brand": brand
            }
        except Exception:
            continue
    return peripherals


def show_info(info):
    lines = []
    for key, value in info.items():
        lines.append(f"{key:<15}: {value}")
    message = "\n".join(lines)
    print("\nNew peripheral detected!")
    print(message)
    log("\n[->] New peripheral detected:\n" + message)


def main():
    print(Fore.LIGHTBLACK_EX + "developed by Luuxo" + Fore.RESET)
    
    print("[SCAN] Peripheral monitoring started. Press Ctrl+C to quit.")
    old = list_peripherals()
    try:
        while True:
            time.sleep(0.1)
            current = list_peripherals()
            new_devices = set(current.keys()) - set(old.keys())
            if new_devices:
                for dev_id in new_devices:
                    show_info(current[dev_id])
            old = current

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        pont_angl()
        