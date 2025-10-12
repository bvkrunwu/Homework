from functools import wraps
from typing import Any, Callable, Dict, Optional, Tuple, Union


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
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
