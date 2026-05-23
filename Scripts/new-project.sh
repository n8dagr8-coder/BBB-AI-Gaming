#!/bin/bash

read -p "Project name: " PROJECT

DIR=~/BBB/Projects/$PROJECT

mkdir -p "$DIR"/{docs,src,assets,notes,backups}

cat > "$DIR/README.md" << EON
# $PROJECT

## Purpose

## Status

## Next Steps

## Notes
EON

echo ""
echo "Project created:"
echo "$DIR"
