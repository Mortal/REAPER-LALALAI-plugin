REAPER plugin for stem splitting
================================

This repository is NOT affiliated with either REAPER or LALAL.AI.

This repository implements 3rd party plugins for REAPER for quick and easy stem splitting inside REAPER.

One plugin integrates with the API of LALAL.AI (requires a paid subscription), the other with demucs (FOSS, runs locally).

Requirements
------------

- REAPER 7 (tested with version 7.33)

- API key for https://www.lalal.ai/ - or a local installation of demucs

- GNU/Linux

- Python 3.10+

- gnome-terminal

- ffmpeg

- curl

Installation
------------

- Download this repository.

- For LALAL:

  - Put your LALAL.AI API key into `~/.cache/lalalapikey`.

  - Add the script 'Split selected audio into vocals and instrumental stems with LALAL AI.py' as a custom action in REAPER.

- For demucs:

  - Add the script 'Split selected audio into vocals and instrumental stems with demucs.py' as a custom action in REAPER.

Usage
-----

1. Select a single audio media item.

2. Make a time selection of the part of the media item to split, or clear the time selection if you want to split the entire item.

3. Run the script action.
