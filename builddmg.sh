#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/An Content Calculator.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/An Content Calculator.dmg" && rm "dist/An Content Calculator.dmg"
create-dmg \
  --volname "An Content Calculator" \
  --volicon "logo.ico" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "An Content Calculator.app" 175 120 \
  --hide-extension "An Content Calculator.app" \
  --app-drop-link 425 120 \
  "dist/An Content Calculator.dmg" \
  "dist/dmg/"