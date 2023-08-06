from django.conf import settings


LOG_READER_DIR_PATH = getattr(
    settings, "LOG_READER_DIR_PATH", getattr(settings, "BASE_DIR") / "logs"
)
LOG_READER_DEFAULT_FILE = getattr(settings, "LOG_READER_DEFAULT_FILE", "django.log")
LOG_READER_MAX_READ_LINES = getattr(settings, "LOG_READER_MAX_READ_LINES", 1000)
