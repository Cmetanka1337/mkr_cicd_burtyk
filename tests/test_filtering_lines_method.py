import pytest
import sys
import os

# Додаємо шлях до директорії, де знаходиться main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main

def test_file_not_found(capsys):
    main.filter_file_by_keyword("non_existent_file.txt", "keyword")


    captured = capsys.readouterr()
    assert "File 'non_existent_file.txt' not found" in captured.out

