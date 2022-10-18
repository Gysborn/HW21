from typing import Dict

from abstract_class import Storage
from exeptions import AmountNotIntError, StorageNotFoundError, BadRequestError


class Request:
    def __init__(self, req: str, storages: Dict[str, Storage]):
        self.storages = storages
        split_request = req.strip().lower().split(' ')
        if len(split_request) != 7:
            raise BadRequestError

        self.amount = split_request[1]
        self.product = split_request[2]
        self.from_ = split_request[4]
        self.to = split_request[6]

    def request_handler(self) -> tuple:
        if not self.amount.isdigit():
            raise AmountNotIntError
        if self.from_ not in self.storages:
            raise StorageNotFoundError
        if self.to not in self.storages:
            raise StorageNotFoundError
        self.amount = int(self.amount)

        return (self.product, self.amount, self.storages[self.from_], self.storages[self.to])



