from reaper_python import *


def get_time_selection() -> tuple[float, float] | None:
    isSet, isLoop, startOut, endOut, allowautoseek = RPR_GetSet_LoopTimeRange(
        False, False, 0.0, 0.0, False
    )
    if startOut == endOut:
        return None
    return startOut, endOut


def script_get_single_selected_media_item() -> "MediaItem":
    count = RPR_CountSelectedMediaItems(None)
    if not count:
        raise SystemExit("Please select a media item")
    if count > 1:
        raise SystemExit("Please select a single media item")
    return RPR_GetSelectedMediaItem(None, 0)


MAX_STRBUF = 4 * 1024 * 1024


def range_intersect(
    a: tuple[float, float] | None, b: tuple[float, float]
) -> tuple[float, float]:
    if a is None:
        return b
    p, q = a
    r, s = b
    return max(p, r), min(q, s)
