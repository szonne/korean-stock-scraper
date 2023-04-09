# korean-stock-scraper

### Dependencies
`pip-compile && pip-sync`

### API_KEY
https://opendart.fss.or.kr/ 에서 발급

### Export data
- `python main.py`
- `API_KEY`, 종목명 입력

### Add code formatter
1. Add config file

    ```yaml
    repos:
    -   repo: https://github.com/ambv/black
        rev: stable
        hooks:
        - id: black
          language_version: python3.8
    ```
2. Generate hooks

    `pre-commit install`

