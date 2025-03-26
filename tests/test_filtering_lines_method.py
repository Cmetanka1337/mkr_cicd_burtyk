import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main

@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "test_input.txt"
    content = "Hello world\nPython is great\nKeyword here\nAnother line\n"
    file_path.write_text(content, encoding="utf-8")
    return file_path

def test_file_not_found(capsys):
    main.filter_file_by_keyword("non_existent_file.txt", "keyword")


    captured = capsys.readouterr()
    assert "File 'non_existent_file.txt' not found" in captured.out


def test_no_matching_lines(sample_file, tmp_path, capsys):
    output_file = tmp_path / "filtered.txt"
    main.filter_file_by_keyword(sample_file, "not_in_file")

    assert not output_file.exists()

    captured = capsys.readouterr()
    assert "No matching lines found" in captured.out


def test_matching_lines(sample_file, tmp_path, capsys):
    output_file = tmp_path / "filtered.txt"
    main.filter_file_by_keyword(sample_file, "Keyword", tmp_path)

    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8").strip()
    assert content == "Keyword here"

    captured = capsys.readouterr()
    assert f"Filtered lines written to 'filtered.txt' in {tmp_path}" in captured.out