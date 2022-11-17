#!/usr/bin/env bash
cd share/rhasspy/profiles/wav/
filesHi=(hi/*.wav)
cp "${filesHi[RANDOM % ${#filesHi[@]}]}" hi_message.wav
filesError=(error/*.wav)
cp "${filesError[RANDOM % ${#filesError[@]}]}" error_message.wav
