""" The commons const for all tests """
from homeassistant.components.climate.const import (  # pylint: disable=unused-import
    PRESET_BOOST,
    PRESET_COMFORT,
    PRESET_ECO,
    PRESET_NONE,
    PRESET_ACTIVITY,
)
from custom_components.versatile_thermostat.const import (
    CONF_NAME,
    CONF_HEATER,
    CONF_HEATER_2,
    CONF_HEATER_3,
    CONF_HEATER_4,
    CONF_THERMOSTAT_CLIMATE,
    CONF_THERMOSTAT_SWITCH,
    CONF_THERMOSTAT_TYPE,
    CONF_AC_MODE,
    CONF_TEMP_SENSOR,
    CONF_EXTERNAL_TEMP_SENSOR,
    CONF_CYCLE_MIN,
    CONF_TEMP_MAX,
    CONF_TEMP_MIN,
    CONF_PROP_FUNCTION,
    PROPORTIONAL_FUNCTION_TPI,
    CONF_TPI_COEF_INT,
    CONF_TPI_COEF_EXT,
    CONF_MINIMAL_ACTIVATION_DELAY,
    CONF_SECURITY_DELAY_MIN,
    CONF_SECURITY_MIN_ON_PERCENT,
    CONF_SECURITY_DEFAULT_ON_PERCENT,
    CONF_USE_WINDOW_FEATURE,
    CONF_USE_MOTION_FEATURE,
    CONF_USE_POWER_FEATURE,
    CONF_USE_PRESENCE_FEATURE,
    CONF_WINDOW_SENSOR,
    CONF_WINDOW_DELAY,
    CONF_WINDOW_AUTO_OPEN_THRESHOLD,
    CONF_WINDOW_AUTO_CLOSE_THRESHOLD,
    CONF_WINDOW_AUTO_MAX_DURATION,
    CONF_MOTION_SENSOR,
    CONF_MOTION_DELAY,
    CONF_MOTION_OFF_DELAY,
    CONF_MOTION_PRESET,
    CONF_NO_MOTION_PRESET,
    CONF_POWER_SENSOR,
    CONF_MAX_POWER_SENSOR,
    CONF_DEVICE_POWER,
    CONF_PRESET_POWER,
    CONF_PRESENCE_SENSOR,
    PRESET_AWAY_SUFFIX,
    CONF_CLIMATE,
)

MOCK_TH_OVER_SWITCH_USER_CONFIG = {
    CONF_NAME: "TheOverSwitchMockName",
    CONF_THERMOSTAT_TYPE: CONF_THERMOSTAT_SWITCH,
    CONF_TEMP_SENSOR: "sensor.mock_temp_sensor",
    CONF_EXTERNAL_TEMP_SENSOR: "sensor.mock_ext_temp_sensor",
    CONF_CYCLE_MIN: 5,
    CONF_TEMP_MIN: 15,
    CONF_TEMP_MAX: 30,
    CONF_DEVICE_POWER: 1,
    CONF_USE_WINDOW_FEATURE: True,
    CONF_USE_MOTION_FEATURE: True,
    CONF_USE_POWER_FEATURE: True,
    CONF_USE_PRESENCE_FEATURE: True,
}

MOCK_TH_OVER_4SWITCH_USER_CONFIG = {
    CONF_NAME: "TheOver4SwitchMockName",
    CONF_THERMOSTAT_TYPE: CONF_THERMOSTAT_SWITCH,
    CONF_TEMP_SENSOR: "sensor.mock_temp_sensor",
    CONF_EXTERNAL_TEMP_SENSOR: "sensor.mock_ext_temp_sensor",
    CONF_CYCLE_MIN: 8,
    CONF_TEMP_MIN: 15,
    CONF_TEMP_MAX: 30,
    CONF_DEVICE_POWER: 1,
    CONF_USE_WINDOW_FEATURE: True,
    CONF_USE_MOTION_FEATURE: True,
    CONF_USE_POWER_FEATURE: True,
    CONF_USE_PRESENCE_FEATURE: True,
}

MOCK_TH_OVER_CLIMATE_USER_CONFIG = {
    CONF_NAME: "TheOverClimateMockName",
    CONF_THERMOSTAT_TYPE: CONF_THERMOSTAT_CLIMATE,
    CONF_TEMP_SENSOR: "sensor.mock_temp_sensor",
    CONF_EXTERNAL_TEMP_SENSOR: "sensor.mock_ext_temp_sensor",
    CONF_CYCLE_MIN: 5,
    CONF_TEMP_MIN: 15,
    CONF_TEMP_MAX: 30,
    CONF_DEVICE_POWER: 1,
    # Keep default values which are False
}

MOCK_TH_OVER_SWITCH_TYPE_CONFIG = {
    CONF_HEATER: "switch.mock_switch",
    CONF_PROP_FUNCTION: PROPORTIONAL_FUNCTION_TPI,
}

MOCK_TH_OVER_4SWITCH_TYPE_CONFIG = {
    CONF_HEATER: "switch.mock_4switch0",
    CONF_HEATER_2: "switch.mock_4switch1",
    CONF_HEATER_3: "switch.mock_4switch2",
    CONF_HEATER_4: "switch.mock_4switch3",
    CONF_PROP_FUNCTION: PROPORTIONAL_FUNCTION_TPI,
}

MOCK_TH_OVER_SWITCH_TPI_CONFIG = {
    CONF_TPI_COEF_INT: 0.3,
    CONF_TPI_COEF_EXT: 0.1,
}

MOCK_TH_OVER_CLIMATE_TYPE_CONFIG = {
    CONF_CLIMATE: "climate.mock_climate",
    CONF_AC_MODE: False,
}

MOCK_PRESETS_CONFIG = {
    PRESET_ECO + "_temp": 16,
    PRESET_COMFORT + "_temp": 17,
    PRESET_BOOST + "_temp": 18,
}

MOCK_WINDOW_CONFIG = {
    CONF_WINDOW_SENSOR: "binary_sensor.window_sensor",
    CONF_WINDOW_DELAY: 10,
}

MOCK_WINDOW_AUTO_CONFIG = {
    CONF_WINDOW_AUTO_OPEN_THRESHOLD: 1.0,
    CONF_WINDOW_AUTO_CLOSE_THRESHOLD: 0.0,
    CONF_WINDOW_AUTO_MAX_DURATION: 5.0,
}

MOCK_MOTION_CONFIG = {
    CONF_MOTION_SENSOR: "input_boolean.motion_sensor",
    CONF_MOTION_DELAY: 10,
    CONF_MOTION_OFF_DELAY: 30,
    CONF_MOTION_PRESET: PRESET_COMFORT,
    CONF_NO_MOTION_PRESET: PRESET_ECO,
}

MOCK_POWER_CONFIG = {
    CONF_POWER_SENSOR: "sensor.power_sensor",
    CONF_MAX_POWER_SENSOR: "sensor.power_max_sensor",
    CONF_PRESET_POWER: 10,
}

MOCK_PRESENCE_CONFIG = {
    CONF_PRESENCE_SENSOR: "person.presence_sensor",
    PRESET_ECO + PRESET_AWAY_SUFFIX + "_temp": 16,
    PRESET_COMFORT + PRESET_AWAY_SUFFIX + "_temp": 17,
    PRESET_BOOST + PRESET_AWAY_SUFFIX + "_temp": 18,
}

MOCK_ADVANCED_CONFIG = {
    CONF_MINIMAL_ACTIVATION_DELAY: 10,
    CONF_SECURITY_DELAY_MIN: 5,
    CONF_SECURITY_MIN_ON_PERCENT: 0.4,
    CONF_SECURITY_DEFAULT_ON_PERCENT: 0.3,
}

MOCK_DEFAULT_FEATURE_CONFIG = {
    CONF_USE_WINDOW_FEATURE: False,
    CONF_USE_MOTION_FEATURE: False,
    CONF_USE_POWER_FEATURE: False,
    CONF_USE_PRESENCE_FEATURE: False,
}
