from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class DataVisualizer:
    """
    Класс для визуализации данных из pandas DataFrame.

    Attributes:
        df (pd.DataFrame): DataFrame с данными для визуализации.
        title (str): Заголовок графика.
        xlabel (str): Подпись оси X графика.
        ylabel (str): Подпись оси Y графика.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Инициализация визуализатора данных.

        Args:
            df (pd.DataFrame): DataFrame с данными для визуализации.
        """
        self.df = df
        self.title = "Data Visualization"
        self.xlabel = "Index"
        self.ylabel = "Values"

    def __str__(self) -> str:
        """Возвращает строковое представление объекта DataVisualizer."""
        return f"DataVisualizer(df={self.df}, title={self.title}, \
                                xlabel={self.xlabel}, ylabel={self.ylabel})"

    def __repr__(self) -> str:
        return (
            f"DataVisualizer(df=pd.DataFrame(...), "
            f"title='{self.title}', xlabel='{self.xlabel}', ylabel='{self.ylabel}')"
        )

    def plot_data(self) -> None:
        """Отображает данные DataFrame в виде графика."""
        self.df.plot(title=self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.show()

    # def plot_hist(self) -> None:
    #     """Отображает данные DataFrame в виде гистограммы."""
    #     self.df.hist(title=self.title)
    #     plt.xlabel(self.xlabel)
    #     plt.ylabel(self.ylabel)
    #     plt.legend()
    #     plt.show()
    def plot_bar(self, x: str, y: str) -> None:
        """Отображает данные DataFrame в виде столбчатой диаграммы."""
        self.df.plot.bar(x=x, y=y, title=self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.show()

    def plot_scatter(self, x: str, y: str) -> None:
        """Отображает данные DataFrame в виде точечной диаграммы."""
        self.df.plot.scatter(x=x, y=y, title=self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.show()

    def plot_box(self, column: str) -> None:
        """Отображает данные DataFrame в виде коробочной диаграммы."""
        self.df[column].plot.box(title=self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.show()


class ExcelDataManager:
    """
    Класс для управления данными Excel, включая сохранение и загрузку.

    Attributes:
        excel_file_path (Path): Путь к файлу Excel.
        columns (List[str]): Список названий столбцов для DataFrame.
    """

    def __init__(self, excel_file_path: Path):
        """
        Инициализация менеджера данных Excel.

        Args:
            excel_file_path (Path): Путь к файлу Excel.
        """
        self.excel_file_path = excel_file_path
        self.columns = ["A", "B", "C"]
        self.df = pd.DataFrame()  # Инициализация атрибута df

    def __str__(self) -> str:
        """Возвращает строковое представление объекта ExcelDataManager."""
        return f"ExcelDataManager(excel_file_path={self.excel_file_path}, columns={self.columns})"

    def __repr__(self) -> str:
        return (
            f"ExcelDataManager(excel_file_path=Path('{self.excel_file_path}'), "
            f"columns={self.columns})"
        )

    def make_random_data(self, num_rows: int = 10) -> None:
        """
        Генерирует случайные данные и сохраняет их в Excel файл.

        Args:
            num_rows (int): Количество строк случайных данных.
        """
        shape = (num_rows, len(self.columns))
        self.df = pd.DataFrame(np.random.rand(*shape), columns=self.columns)

    def save_random_data_to_excel(self) -> None:
        """
        Генерирует случайные данные и сохраняет их в Excel файл.

        Args:
            num_rows (int): Количество строк случайных данных.
        """
        self.df.to_excel(self.excel_file_path, index=False)

    def load_data_from_excel(self) -> pd.DataFrame:
        """Загружает данные из Excel файла в DataFrame."""
        return pd.read_excel(self.excel_file_path)

def main() -> None:

    """
    Основная функция для демонстрации сохранения случайных данных в Excel и их визуализации.
    """
    # Создание пути к директории и файлу Excel
    excel_dir_name = "excel_files"
    excel_dir = Path(__file__).parent / excel_dir_name
    excel_file_name = "np_random_data.xlsx"
    excel_file_path = Path(excel_dir / excel_file_name)

    data_manager = ExcelDataManager(excel_file_path)

    # Изменение структуры данных
    columns = ["A", "B", "C", "D", "E"]
    rows = 10
    data_manager.columns = columns

    # Сохранение и загрузка данных
    data_manager.make_random_data(rows)
    data_manager.save_random_data_to_excel()
    df_loaded = data_manager.load_data_from_excel()

    # Настройка и визуализация данных
    visualizer = DataVisualizer(df_loaded)
    visualizer.title = "Таблица случайных данных"
    visualizer.xlabel = "Индекс"
    visualizer.ylabel = "Значения"
    visualizer.plot_data()
    # visualizer.plot_hist()
    visualizer.plot_bar("A", "B")
    visualizer.plot_scatter("A", "B")
    visualizer.plot_box("B")


if __name__ == "__main__":
    main()
