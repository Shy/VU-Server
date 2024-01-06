# This file was automatically generated using `generate_pyton_classes.py` script.
# Please don't make any direct modifications to this file as they will be overwritten and lost in the next cycle.
# Instead please make modification in the respective .yaml file.
# Generated on 2023-10-06 23:18


class dial_bus_config:
    GAUGE_HUB_MAX_DEVICES = 100
    GAUGE_HUB_UID_LENGTH = 12
    GAUGE_I2C_ADDRESS_BOOTLOADER = 0x08
    GAUGE_I2C_ADDRESS_PROVISIONING = 0x09
    GAUGE_I2C_ADDRESS_GENERAL_CALL = 0x00
    GAUGE_I2C_ADDRESS_FIRST = 0x0A
    GAUGE_I2C_ADDRESS_LAST = (GAUGE_I2C_ADDRESS_FIRST+GAUGE_HUB_MAX_DEVICES)
    GAUGE_COMMS_POS_CMD = 0
    GAUGE_COMMS_POS_DATA_LEN = 1
    GAUGE_COMMS_POS_DATA = GAUGE_COMMS_POS_DATA_LEN+2
    GAUGE_COMMS_RX_SIZE = 1100
    GAUGE_I2C_DEVICE_READY_RETRIES = 15
    GAUGE_DIAL_PROTOCOL_VERSION = "v1"
    GAUGE_I2C_JUMP_TO_BTL_KEY1 = 0x53
    GAUGE_I2C_JUMP_TO_BTL_KEY2 = 0x4B

class dial_commands:
    DG_HUB_CMD_FIRST = 0x00
    DG_HUB_TO_DEV_GET_UID = 0x01
    DG_HUB_TO_DEV_HUB_UID = 0x02
    DG_HUB_TO_DEV_SET_ADDRESS = 0x03
    DG_HUB_TO_DEV_SET_DAC = 0x04
    DG_HUB_TO_DEV_GET_DAC = 0x05
    DG_HUB_TO_DEV_CYCLE_GAUGE = 0x06
    DG_HUB_TO_DEV_PWR_LED_ENABLE = 0x07
    DG_HUB_TO_DEV_PWR_LED_DISABLE = 0x08
    DG_HUB_TO_DEV_ACT_LED_ENABLE = 0x09
    DG_HUB_TO_DEV_ACT_LED_DISABLE = 0x0A
    DG_HUB_TO_DEV_VERIFY_UID = 0x0B
    DG_HUB_TO_DEV_GET_PROPERTIES = 0x0C
    DG_HUB_TO_DEV_SET_PERCENT = 0x0D
    DG_HUB_TO_DEV_GET_PERCENT = 0x0E
    DG_HUB_TO_DEV_SET_DIAL_MAX = 0x0F
    DG_HUB_TO_DEV_SET_DIAL_HALF = 0x10
    DG_HUB_TO_DEV_GET_VERSION = 0x11
    DG_HUB_TO_DEV_SET_RGB_BACKLIGHT = 0x12
    DG_HUB_TO_DEV_GET_RGB_BACKLIGHT = 0x13
    DG_HUB_TO_DEV_DISPLAY_CLEAR = 0x14
    DG_HUB_TO_DEV_DISPLAY_GOTO_XY = 0x15
    DG_HUB_TO_DEV_DISPLAY_IMG_DATA = 0x16
    DG_HUB_TO_DEV_DISPLAY_SHOW_IMG = 0x17
    DG_HUB_TO_DEV_RX_BUFFER_SIZE = 0x18
    DG_HUB_TO_DEV_KEEP_ALIVE = 0x19
    DG_HUB_TO_DEV_SERVER_ABSENT = 0x1A
    DG_HUB_TO_DEV_SERVER_PRESENT = 0x1B
    DG_HUB_TO_DEV_DIAL_EASING_STEP = 0x1C
    DG_HUB_TO_DEV_DIAL_EASING_PERIOD = 0x1D
    DG_HUB_TO_DEV_BACKLIGHT_EASING_STEP = 0x1E
    DG_HUB_TO_DEV_BACKLIGHT_EASING_PERIOD = 0x1F
    DG_HUB_TO_DEV_GET_EASING_CONFIG = 0x20
    DG_HUB_TO_DEV_BUILD_INFO = 0x21
    DG_HUB_TO_DEV_FW_INFO = 0x22
    DG_HUB_TO_DEV_HW_INFO = 0x23
    DG_HUB_TO_DEV_PROTOCOL_INFO = 0x24
    DG_HUB_TO_DEV_BTL_JUMP_TO_BOOTLOADER = 0xF0
    DG_HUB_TO_DEV_BTL_BOOTLOADER_INFO = 0xF1
    DG_HUB_TO_DEV_BTL_GET_CRC = 0xF2
    DG_HUB_TO_DEV_BTL_ERASE_APP = 0xF3
    DG_HUB_TO_DEV_FWUP_PACKAGE = 0xF4
    DG_HUB_TO_DEV_FWUP_FINISHED = 0xF5
    DG_HUB_TO_DEV_BTL_EXIT = 0xF6
    DG_HUB_TO_DEV_BTL_RESTART_UPLOAD = 0xF7
    DG_HUB_TO_DEV_BTL_READ_STATUS_CODE = 0xF8
    DG_HUB_TO_DEV_RESET_CFG = 0xFA
    DG_HUB_CMD_LAST = None

class device_types:
    DG_DEVICE_TYPE_FIRST = 0x00
    DG_DEVICE_TYPE_ANALOG_GAUGE = 0x01
    DG_DEVICE_TYPE_EINK_GAUGE = 0x02
    DG_DEVICE_TYPE_LAST = None