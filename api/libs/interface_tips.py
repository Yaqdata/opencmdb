from enum import Enum


class InterfaceTips(Enum):
    # [10000: 10100)
    INVALID_REQUEST = (400, 10000, '不合法的请求')
    INVALID_TOKEN = (401, 10001, '无效的token')

    # [10100: 10200)
    DATA_NOT_EXISTED = (404, 10100, '数据不存在')
    USER_NOT_EXISTED_OR_WRONG_PASSWORD = (401, 10101, '用户名/密码错误')
