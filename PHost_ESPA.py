
import wmi
import time
import os

from PONT import pont_espa
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
log_file_path = os.path.join(os.getcwd(), "perifericos_log.txt")


def log(message):
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def listar_perifericos():
    perifericos = {}
    for p in c.Win32_PnPEntity():
        try:
            id_dispositivo = p.DeviceID
            vid = "????"
            if "VID_" in id_dispositivo:
                vid = id_dispositivo.split("VID_")[1][:4].upper()
            marca = vid_dict.get(vid, "Desconocido")

            perifericos[id_dispositivo] = {
                "Nombre": p.Name or "Desconocido",
                "Descripción": p.Description or "Desconocido",
                "Fabricante": getattr(p, "Manufacturer", "Desconocido"),
                "Clase": p.PNPClass or "No especificada",
                "Estado": p.Status or "Desconocido",
                "Título": p.Caption or "N/A",
                "ID de Hardware": p.DeviceID,
                "ID Compatible": getattr(p, "CompatibleID", "Desconocido"),
                "GUID de Clase": getattr(p, "ClassGuid", "Desconocido"),
                "Código de Error": getattr(p, "ConfigManagerErrorCode", "Desconocido"),
                "Ubicación": getattr(p, "LocationInformation", "Desconocido"),
                "Servicio": getattr(p, "Service", "Desconocido"),
                "Marca": marca
            }
        except Exception:
            continue
    return perifericos


def mostrar_info(info):
    lines = []
    for clave, valor in info.items():
        lines.append(f"{clave:<15}: {valor}")
    message = "\n".join(lines)
    print("\n¡Nuevo periférico detectado!")
    print(message)
    log("\n[->] Nuevo periférico detectado:\n" + message)


def main():
    print(Fore.LIGHTBLACK_EX + "developed by Luuxo" + Fore.RESET)

    print("[ESCANEAR] Monitoreo de periféricos iniciado. Presiona Ctrl+C para salir.")
    antiguos = listar_perifericos()
    try:
        while True:
            time.sleep(0.1)
            actuales = listar_perifericos()
            nuevos = set(actuales.keys()) - set(antiguos.keys())
            if nuevos:
                for dev_id in nuevos:
                    mostrar_info(actuales[dev_id])
            antiguos = actuales

    except KeyboardInterrupt:
        print("\nMonitoreo detenido por el usuario.")
        pont_espa()
