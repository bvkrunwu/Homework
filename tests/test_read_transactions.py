from pathlib import Path
from unittest.mock import Mock, patch

from src.read_transactions import read_csv_transactions, read_excel_transactions

# Вспомогательные данные для тестов
TEST_DATA_CSV = [
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
]

TEST_DATA_EXCEL = TEST_DATA_CSV[:3]  # Сокращённая версия для Excel


# Функциональные тесты для read_csv_transactions
def test_read_csv_with_default_path():
    with patch("pandas.read_csv") as mock_read_csv:
        mock_df = Mock()
        mock_df.to_dict.return_value = TEST_DATA_CSV
        mock_read_csv.return_value = mock_df

        result = read_csv_transactions()
        assert result == TEST_DATA_CSV
        expected_path = str(Path(__file__).resolve().parents[1] / "data" / "transactions.csv")
        mock_read_csv.assert_called_once_with(expected_path, sep=";", encoding="utf-8")


def test_read_csv_with_custom_path():
    custom_path = "/custom/path/to/file.csv"
    with patch("pandas.read_csv") as mock_read_csv:
        mock_df = Mock()
        mock_df.to_dict.return_value = TEST_DATA_CSV
        mock_read_csv.return_value = mock_df

        result = read_csv_transactions(custom_path)
        assert result == TEST_DATA_CSV
        mock_read_csv.assert_called_once_with(custom_path, sep=";", encoding="utf-8")


def test_read_csv_error_handling():
    with patch("pandas.read_csv", side_effect=Exception("Test exception")):
        result = read_csv_transactions()
        assert result == []


# Функциональные тесты для read_excel_transactions
def test_read_excel_with_default_path():
    with patch("pandas.read_excel") as mock_read_excel:
        mock_df = Mock()
        mock_df.to_dict.return_value = TEST_DATA_EXCEL
        mock_read_excel.return_value = mock_df

        result = read_excel_transactions()
        assert result == TEST_DATA_EXCEL
        expected_path = str(Path(__file__).resolve().parents[1] / "data" / "transactions_excel.xlsx")
        mock_read_excel.assert_called_once_with(expected_path)


def test_read_excel_with_custom_path():
    custom_path = "/custom/path/to/file.xlsx"
    with patch("pandas.read_excel") as mock_read_excel:
        mock_df = Mock()
        mock_df.to_dict.return_value = TEST_DATA_EXCEL
        mock_read_excel.return_value = mock_df

        result = read_excel_transactions(custom_path)
        assert result == TEST_DATA_EXCEL
        mock_read_excel.assert_called_once_with(custom_path)


def test_read_excel_error_handling():
    with patch("pandas.read_excel", side_effect=Exception("Test exception")):
        result = read_excel_transactions()
        assert result == []
