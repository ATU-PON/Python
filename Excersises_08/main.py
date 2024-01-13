from devices import Firewall
from devices import Switch

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()

# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Create a Switch instance
switch1 = Switch("switch1")
# Verify a CRC
switch1.calculate_crc("dummy data")