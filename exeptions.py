class BaseError(Exception):
    message = 'error'


class AmountNotIntError(BaseError):
    message = "Колличество не является числом"


class StorageNotFoundError(BaseError):
    message = "Такого склада не существует"


class MissingProductError(BaseError):
    message = "Такого товара не существует"


class RequiredQuantityError(BaseError):
    message = "Необходимое колличество отсутствует"


class NotEnoughSpaceError(BaseError):
    message = "Недостаточно места"


class BadRequestError(BaseError):
    message = "Не корректный запрос"
