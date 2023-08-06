# CAPCTL

CAP 유저 관리를 위한 CLI 툴

기존 app, dev 등의 기능은 telepresence -> telepresence2 로 변경 및 cap 1.3.1 기능 업데이트에 따라
현재는 user 기능을 제외하고 주석처리 되어있습니다.
(/capctl/main.py 참조)

## 현재 최신버전 (2022.06.14)
capctl 0.0.6

## Prerequisite
Python >= 3.6 설치   
## Install
```
pip install -r requirements.txt
pip install -e ./
```

## Quick Start 
### **user**  
1. **ls (Get user list)**
    ```
    > capctl user list
    ```

1. **add (Create user)**
    ```
    > capctl user add \
    --email shhong3@dudaji.com \
    --password shhong3 \
    --username shhong3
    ```
1. **delete (Delete user (also leave in all projects))**
    ```
    # ex) Delete "shhong3@dudaji.com"
    > capctl user delete --email shhong3@dudaji.com
    ```
1. **password (Change password)**
    ```
    > capctl user password admin@kubeflow.org 'asdf!!'
    ```
### **project**  
1. **ls (Get project list)**
    ```
    > capctl project ls
    ```

1. **add (Create project)**
    ```
    # ex) Create "test-project"
    > capctl project add \
    --email shhong3@dudaji.com \
    --project_name test-project 
    ```

1. **join (Join project)**
    ```
    # ex) Join "test-project"
    > capctl project join \
    --email shhong3@dudaji.com \
    --project_name test-project
    ```

1. **leave (Leave project)**
    ```
    # ex) Leave "test-project" (member: shhong3@dudaji.com)
    > capctl project join \
    --email shhong3@dudaji.com \
    --project_name test-project
    ```

1. **delete (Delete project (all members except the owner must be removed from the project))**
    ```
    > capctl project delete \
    --project_name test-project
    ```
