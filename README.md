REAPER plugin for stem splitting with LALAL.AI
==============================================

This repository is NOT affiliated with either REAPER or LALAL.AI.

This repository implements a 3rd party plugin for REAPER, integrating with the API of LALAL.AI for quick and easy stem splitting inside REAPER.

Requirements
------------

- REAPER 7 (tested with version 7.33)

- API key for https://www.lalal.ai/

- GNU/Linux

- Python 3.10+

- gnome-terminal

- ffmpeg

- curl

Installation
------------

- Download this repository.

- Put your LALAL.AI API key into `~/.cache/lalalapikey`.

- Add the script 'Split selected audio into vocals and instrumental stems with LALAL AI.py' as a custom action in REAPER.

Usage
-----

1. Select a single audio media item.

2. Make a time selection of the part of the media item to split, or clear the time selection if you want to split the entire item.

3. Run the script action.
