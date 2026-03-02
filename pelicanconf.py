AUTHOR = 'Conner Lavineway'
SITENAME = 'Conner Lavineways Portfolio'
SITEURL = ""
THEME = "Flex"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

TIMEZONE = 'America/Winnipeg'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

STATIC_PATHS = ['images']  # Tell Pelican to copy the images directory
SITELOGO = 'images/Profile-Pic.jpg'

DISPLAY_PAGES_ON_MENU = False

DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True
PATH = "content"