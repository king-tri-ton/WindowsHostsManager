# WindowsHostsManager

WindowsHostsManager — это утилита для управления файлом `hosts` в операционной системе Windows. Программа позволяет добавлять, удалять, просматривать и очищать записи в файле `hosts`, что может быть полезно для перенаправления доменных имен на определенные IP-адреса.

## Требования

- Windows с правами администратора
- Python 3.x

## Установка

1. Клонируйте репозиторий или скачайте файл `WindowsHostsManager.py`.
2. Убедитесь, что у вас установлен Python 3.x.

## Запуск

Для запуска программы выполните следующую команду в терминале или командной строке:

```bash
python WindowsHostsManager.py
```

**Важно:** Программа требует прав администратора, так как файл `hosts` находится в системной директории.

## Команды

- `add <IP> <hostname>` — Добавить запись в файл `hosts`. Например: `add 127.0.0.1 example.com`
- `remove <hostname>` — Удалить запись по имени хоста. Например: `remove example.com`
- `list` — Показать все текущие записи в файле `hosts`.
- `clear` — Очистить экран терминала.
- `help` — Показать список доступных команд.
- `exit` — Выйти из программы.

## Примеры использования

- Добавить запись:
  ```bash
  Enter command: add 127.0.0.1 example.com
  ```
  Вывод:
  ```
  Added: 127.0.0.1 example.com
  ```

- Удалить запись:
  ```bash
  Enter command: remove example.com
  ```
  Вывод:
  ```
  Removed entries for: example.com
  ```

- Показать все записи:
  ```bash
  Enter command: list
  ```
  Вывод:
  ```
  Current entries in hosts file:
  127.0.0.1 localhost
  127.0.0.1 example.com
  ```

- Очистить экран:
  ```bash
  Enter command: clear
  ```

## Примечания

- Программа предназначена для работы только на Windows.
- Убедитесь, что вы запускаете программу с правами администратора, чтобы избежать проблем с доступом к файлу `hosts`.

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).