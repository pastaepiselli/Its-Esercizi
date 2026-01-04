from fcntl import FASYNC

from laptop import Laptop
from smartphone import Smartphone
from service_center import ServiceCenter

thinkpad = Laptop("l1", "ThinkPad T480", "Loreno Rossi", 2024, "received", False,14.0)
iphone12 = Smartphone("s1", "Iphone 12", "Lucrezia Le Foche", 2022, "repairing", False, 256 )

repair_center = ServiceCenter()
repair_center.add(thinkpad)
repair_center.add(iphone12)