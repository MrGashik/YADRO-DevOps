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

## Телеком

### Структура

```bash
Telecom/
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
    ├── Chapter 3 - Automating The Process Using Ansible
    │   └── ansible
    │       ├── inventories
    │       │   └── hosts
    │       └── playbooks
    │           ├── deploy_script.yml
    │           └── roles
    │               ├── check-script
    │               │   ├── meta
    │               │   │   └── main.yml
    │               │   ├── tasks
    │               │   │   └── main.yml
    │               │   └── vars
    │               │       └── main.yml
    │               ├── install-docker
    │               │   ├── meta
    │               │   │   └── main.yml
    │               │   └── tasks
    │               │       └── main.yml
    │               └── start-container
    │                   ├── meta
    │                   │   └── main.yml
    │                   ├── tasks
    │                   │   └── main.yml
    │                   ├── templates
    │                   │   ├── Dockerfile.j2
    │                   │   └── scripts
    │                   │       └── http_requests.py.j2
    │                   └── vars
    │                       └── main.yml
    └── create_venv.sh

45 directories, 32 files
```