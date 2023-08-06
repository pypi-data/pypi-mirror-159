from pathlib import Path

from django.http import FileResponse
from log_api import settings
from rest_framework.views import APIView
from tailhead import tail


def tail_logs(log_file: Path, tail_lines):
    yield b"\n".join(tail(log_file.open("rb"), tail_lines))


class DownloadView(APIView):
    def get(self, request):
        log_name: str = self.request.query_params.get("name")
        tail_lines: int = self.request.query_params.get(
            "tail", settings.LOG_READER_MAX_READ_LINES
        )
        if log_name and log_name.count(".") != 1:
            log_name += ".log"
        else:
            log_name = settings.LOG_READER_DEFAULT_FILE

        file = settings.LOG_READER_DIR_PATH / log_name
        response = FileResponse(tail_logs(file, tail_lines))
        response["Content-Type"] = "application/octet-stream"
        response["Content-Disposition"] = f'attachment;filename="{log_name}"'
        return response
