import os
import sys
import typer
import shutil
import platform

app = typer.Typer()

# Определяем путь к hosts в зависимости от ОС
if os.name == "nt":
    HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
else:
    HOSTS_PATH = "/etc/hosts"

BACKUP_PATH = HOSTS_PATH + ".back"

def is_admin() -> bool:
    """Проверка прав администратора/суперпользователя"""
    if os.name == "nt":
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False
    else:
        return os.geteuid() == 0

def read_hosts():
    with open(HOSTS_PATH, "r", encoding="utf-8") as f:
        return f.readlines()

def write_hosts(lines):
    with open(HOSTS_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)

@app.command()
def add(ip: str, hostname: str):
    """Добавить новый хост"""
    lines = read_hosts()
    entry = f"{ip} {hostname}\n"
    if entry not in lines:
        lines.append(entry)
        write_hosts(lines)
        typer.echo(f"Added: {entry.strip()}")
    else:
        typer.echo(f"Entry already exists: {entry.strip()}")

@app.command()
def remove(hostname: str):
    """Удалить хост"""
    lines = read_hosts()
    new_lines = [line for line in lines if not line.strip().endswith(hostname)]
    write_hosts(new_lines)
    typer.echo(f"Removed entries for: {hostname}")

@app.command()
def edit(old_hostname: str, ip: str = None, new_hostname: str = None):
    """Редактировать существующий хост"""
    lines = read_hosts()
    updated_lines = []
    found = False
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2 and parts[1] == old_hostname:
            found = True
            new_ip = ip if ip else parts[0]
            new_host = new_hostname if new_hostname else parts[1]
            updated_lines.append(f"{new_ip} {new_host}\n")
        else:
            updated_lines.append(line)
    if found:
        write_hosts(updated_lines)
        typer.echo(f"Updated {old_hostname}")
    else:
        typer.echo(f"{old_hostname} not found")

@app.command()
def list():
    """Список всех хостов"""
    lines = read_hosts()
    for line in lines:
        typer.echo(line.strip())

@app.command()
def backup():
    """Создать резервную копию"""
    shutil.copy2(HOSTS_PATH, BACKUP_PATH)
    typer.echo(f"Backup created: {BACKUP_PATH}")

@app.command()
def restore():
    """Восстановить из резервной копии"""
    if os.path.exists(BACKUP_PATH):
        shutil.copy2(BACKUP_PATH, HOSTS_PATH)
        typer.echo(f"Hosts file restored from backup: {BACKUP_PATH}")
    else:
        typer.echo("No backup found")

if __name__ == "__main__":
    if not is_admin():
        system_name = platform.system()
        if system_name == "Windows":
            typer.echo("Запусти консоль от имени администратора.")
        else:
            typer.echo("Запусти команду с sudo (пример: sudo whm list).")
        raise typer.Exit()
    app()
