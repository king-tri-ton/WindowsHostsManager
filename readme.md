# WindowsHostsManager

WindowsHostsManager — это утилита для управления файлом `hosts` в операционной системе Windows. Программа позволяет добавлять, удалять, просматривать записи, создавать резервные копии и восстанавливать файл `hosts`.

## Требования

- Windows с правами администратора
- Python 3.x

## Установка

1. Клонируйте репозиторий или скачайте файл `app.py`.
2. Убедитесь, что у вас установлен Python 3.x.

## Запуск

Для запуска программы выполните следующую команду в терминале или командной строке:

```bash
python app.py
```

**Важно:** Программа требует прав администратора, так как файл `hosts` находится в системной директории.

## Команды

- `add <IP> <hostname>` — Добавить запись в файл `hosts`. Например: `add 127.0.0.1 example.com`
- `remove <hostname>` — Удалить запись по имени хоста. Например: `remove example.com`
- `list` — Показать все текущие записи в файле `hosts`.
- `backup` — Создать резервную копию файла `hosts`.
- `restore` — Восстановить файл `hosts` из резервной копии.
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

- Создать резервную копию:
  ```bash
  Enter command: backup
  ```

- Восстановить из резервной копии:
  ```bash
  Enter command: restore
  ```

- Очистить экран:
  ```bash
  Enter command: clear
  ```

## Сборка исполняемого файла

Для создания исполняемого файла используйте `pyinstaller`:

```bash
pyinstaller --onefile --name="whm" --add-data "whm.ico;." --icon=whm.ico app.py
```

## Скачать готовый exe файл

Вы можете скачать готовый исполняемый файл в разделе [релизы](https://github.com/king-tri-ton/WindowsHostsManager/releases) и проверить статус сборки на странице: [GitHub Actions](https://github.com/king-tri-ton/WindowsHostsManager/actions/workflows/build_and_scan.yml).

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).