# LOST.DIR Recover

This script restores file extensions and distributes files to separate directories

## Usage example

```
./lost_dir_recover_fleep.py -s SOURCE_DIR -d OUT_DIR
```

It can be used not only to restore the extension in LOST.DIR, this script is suitable for any files with a lost extension

---

# Восстановление расширений файлов из LOST.DIR

Данный скрипт восстанавливает расширения файлов, которые были потеряны в следствии сбоя питания (зачастую), восстановлены вашей системой и теперь лежат мертвым грузом без расширений.

## Использование

### Установка зависимостей

```
pip3 install -r requirements.txt
```

### Запуск

```
./lost_dir_recover_fleep.py -s SOURCE_DIR -d OUT_DIR
```

## P.s.

Т.к. данный скрипт не использует никаких компилируемых зависимостей (кроме конечно же самого python и его компонентов) - он может быть запущен прямо на вашем смартфоне с помощью [Termux](https://termux.dev/)

- Устанавлиаем Termux
- Устанавливаем python3 и git

```
pkg install python git
```

- Скачиваем LOST.DIR Recover

```
git clone https://github.com/ar1ocker/LOST.DIR-recover/
```
- Переходим в папку со скриптом
```
cd LOST_DIR_recover_fleep
```

- Устанавливаем зависимости

```
pip3 install -r requirements.txt
```

- Разрешаем Termux доступ к файлам на накопителе

```
termux-setup-storage
```

- Запускаем скрипт 

```
python3 lost_dir_recover_fleep.py -s ~/storage/shared/LOST.DIR -d ~/storage/shared/outdir
```

- Забираем файлы из папки, указанной после параметра -d
