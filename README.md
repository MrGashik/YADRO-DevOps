# YADRO-DevOps

## Радиочастотные системы

### Структура

```bash
Radio Frequency Systems/
├── Task 1 - Linux Commands
│   ├── Chapter 1 - Hello
│   │   └── hello.sh
│   └── Chapter 2 - Log
│       └── log.sh
├── Task 2 - Bash or Python Script
│   ├── Chapter 1 - Easy
│   │   ├── search_path.py
│   │   ├── search_path.sh
│   │   └── server.config
│   └── Chapter 2 - Hard
│       ├── search.py
│       ├── search.sh
│       └── server.config
└── Task 3 - Docker
    ├── Dockerfile
    └── scripts
        ├── search_path.py
        ├── search_path.sh
        └── server.config

9 directories, 12 files
```

### Примечание

#### Вызов справки для команд из "Task 2 - Bash or Python Script. Chapter 2 - Hard"

```bash
./search.sh -h
Using: ./search.sh -f "<path_file>" -w "<word>"
flags:
        -f: Specifies the path to the file. Example: -f "/path/to/file/file.*"
        -w: Specifies search word. Example: -w "word"

./search.py -h
Using: ./search.py -f "<path_file>" -w "<word>"
flags:
        -f: Specifies the path to the file. Example: -f "/path/to/file/file.*"
        -w: Specifies search word. Example: -w "word"
```

## Телеком

### Структура

```bash
Telecom/
├── create_venv.sh
├── Variant 1 - Bash
│   ├── Chapter 1 - Working With The Script
│   │   └── http_requests.sh
│   ├── Chapter 2 - Working With Docker
│   │   ├── build_remove.sh
│   │   ├── Dockerfile
│   │   └── scripts
│   │       └── http_requests.sh
│   └── Chapter 3 - Automating The Process Using Ansible
│       └── ansible
│           ├── inventories
│           │   └── hosts
│           └── playbooks
│               ├── deploy_script.yml
│               └── roles
│                   ├── check-script
│                   │   ├── meta
│                   │   │   └── main.yml
│                   │   ├── tasks
│                   │   │   └── main.yml
│                   │   └── vars
│                   │       └── main.yml
│                   ├── install-docker
│                   │   ├── meta
│                   │   │   └── main.yml
│                   │   └── tasks
│                   │       └── main.yml
│                   └── start-container
│                       ├── meta
│                       │   └── main.yml
│                       ├── tasks
│                       │   └── main.yml
│                       ├── templates
│                       │   ├── Dockerfile.j2
│                       │   └── scripts
│                       │       └── http_requests.sh.j2
│                       └── vars
│                           └── main.yml
└── Variant 2 - Python
    ├── Chapter 1 - Working With The Script
    │   └── http_requests.py
    ├── Chapter 2 - Working With Docker
    │   ├── build_remove.sh
    │   ├── Dockerfile
    │   └── scripts
    │       └── http_requests.py
    └── Chapter 3 - Automating The Process Using Ansible
        └── ansible
            ├── inventories
            │   └── hosts
            └── playbooks
                ├── deploy_script.yml
                └── roles
                    ├── check-script
                    │   ├── meta
                    │   │   └── main.yml
                    │   ├── tasks
                    │   │   └── main.yml
                    │   └── vars
                    │       └── main.yml
                    ├── install-docker
                    │   ├── meta
                    │   │   └── main.yml
                    │   └── tasks
                    │       └── main.yml
                    └── start-container
                        ├── meta
                        │   └── main.yml
                        ├── tasks
                        │   └── main.yml
                        ├── templates
                        │   ├── Dockerfile.j2
                        │   └── scripts
                        │       └── http_requests.py.j2
                        └── vars
                            └── main.yml

45 directories, 33 files
```

### Примечание

#### Для всего варианта PYTHON и работы с Ansible в варианте BASH
1. Запускаем скрипт "create_venv.sh" для создания виртуального окружения и установки зависимостей (requests, ansible)
2. Активируем виртуальное окружение
```bash
source venv/bin/activate
```
3. Спокойно запускаем скрипты и playbooks
4. Деактивируем виртуальное окружение
```bash
deactivate
```

#### Для всех вариантов
1. Заменяем данные в файле host
```yaml
[vm]
vm1 ansible_ssh_host=192.168.169.133 ansible_ssh_user=mrgashik ansible_python_interpreter=/usr/bin/python3.13
```
- ```ansible_ssh_host``` - IP-адрес целевой машины
- ```ansible_ssh_user``` - имя пользователя, под которым Ansible подключается к целевому хосту по SSH.
- ```ansible_python_interpreter``` - путь к интерпретатору Python на целевом хосте.
2. Запускаем Ansible Playbooks (находясь в папке "ansible")
```bash
ansible-playbook -i inventories/hosts playbooks/deploy_script.yml
```