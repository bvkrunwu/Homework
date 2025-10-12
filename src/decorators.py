from functools import wraps
from typing import Any, Callable, Dict, Optional, Tuple, Union


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования выполнения функций.

    Parameters:
        filename (Optional[str]): Имя файла для сохранения логов. По умолчанию None.
                                 Если задан, логи будут сохраняться в указанный файл.
                                 Если не задан, логи будут выводиться в консоль.

    Returns:
        Callable[[Callable[..., Any]], Callable[..., Any]]: Декорированная функция.

    Description:
        Данный декоратор добавляет функциональность логирования к целевой функции.
        При успешном выполнении функции в лог добавляется запись вида '{имя_функции} ok'.
        При возникновении исключения в лог добавляется запись с информацией об ошибке
        и переданными аргументах функции.

        Логирование производится либо в указанный файл (если задан параметр filename),
        либо в стандартный поток вывода (консоль).

        Исключения, возникающие при выполнении декорированной функции, перехватываются,
        регистрируются, а затем повторно возбуждаются для дальнейшей обработки.

        Использование functools.wraps обеспечивает сохранение метаданных оригинальной функции.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Union[Any, None]:
            try:
                # Запуск функции
                result = func(*args, **kwargs)

                # Формирования успешного лога
                success_message = f"{func.__name__} ok"

                if filename is not None:
                    # Запись в файл
                    with open(filename, "a") as f:
                        f.write(success_message + "\n")
                else:
                    # Вывод консоль
                    print(success_message)

                return result

            except Exception as e:
                # Обработка ошибки
                inputs_str = f"Inputs: {args}, {kwargs}"
                err_message = f"{func.__name__} error: {type(e).__name__}. {inputs_str}"

                if filename is not None:
                    # Запись в файл
                    with open(filename, "a") as f:
                        f.write(err_message + "\n")
                else:
                    # Вывод ошибки в консоль
                    print(err_message)

                raise

        return wrapper

    return decorator
