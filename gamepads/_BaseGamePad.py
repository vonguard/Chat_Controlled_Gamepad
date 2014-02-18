import uinput, time

NAME_DEFAULT = "python-uinput"
BUSTYPE_DEFAULT = 0
VENDOR_DEFAULT = 0
PRODUCT_DEFAULT = 0
VERSION_DEFAULT = 0

CLICK_PADDING = 0.3

class BaseGamePad(object):
    commandMapping = {}
    events = ()
    name = NAME_DEFAULT
    bustype = BUSTYPE_DEFAULT
    vendor = VENDOR_DEFAULT
    product = PRODUCT_DEFAULT
    version = VERSION_DEFAULT

    def connect(self):
        self.device = uinput.Device(self.events, self.name,
                                    self.bustype, self.vendor, self.product,
                                    self.version)

    def translateInputMessage(self, message):
        if message in self.commandMapping:
            return self.commandMapping[message]

    def _clickButton(self, button):
        self.device.emit(button, 1)
        time.sleep(CLICK_PADDING)
        self.device.emit(button, 0)
        time.sleep(CLICK_PADDING)

    def runCommand(self, command):
        raise NotImplementedError()
