class MyError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return 'Creating My Eception'

try:
    raise MyError('My Error')
except MyError as e:
    print(e.__str__())