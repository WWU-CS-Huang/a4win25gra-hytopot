#!/bin/bash

# Detect which file exists and is non-empty
files=("main.c" "main.py" "Main.java")
selected_file=""
count=0

for file in "${files[@]}"; do
    if [[ -s "$file" ]]; then
        selected_file="$file"
        ((count++))
    fi
done

# Ensure only one non-empty file exists
if [[ $count -ne 1 ]]; then
    echo "Error: Exactly one non-empty source file must exist." >&2
    exit 1
fi

# Compile and run based on file type
case "$selected_file" in
    "main.c")
        gcc -o main main.c || { echo "Compilation failed." >&2; exit 1; }
        exec ./main
        ;;
    "main.py")
        exec python3 main.py
        ;;
    "Main.java")
        javac Main.java || { echo "Compilation failed." >&2; exit 1; }
        exec java Main
        ;;
    *)
        echo "Error: No valid source file found." >&2
        exit 1
        ;;
esac
