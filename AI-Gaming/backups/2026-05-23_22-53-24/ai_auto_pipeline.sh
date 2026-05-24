#!/bin/bash

echo ""
echo "===== BBB AI AUTO PIPELINE ====="
echo ""

python3 ai_ranked_highlights.py

echo ""
echo "Generating highlight report..."
python3 ai_highlight_report.py

echo ""
echo "Generating stream titles..."
python3 ai_stream_titles.py

echo ""
echo "Generating content pack..."
python3 ai_content_pack.py

echo ""
echo "Done."
echo ""
