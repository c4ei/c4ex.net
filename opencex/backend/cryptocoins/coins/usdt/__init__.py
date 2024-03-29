from core.currency import TokenParams
from cryptocoins.utils.register import register_token

USDT = 4
CODE = 'USDT'
DECIMALS = 2
BLOCKCHAINS = {
    'ETH': TokenParams(
        symbol=CODE,
        contract_address='0xdAC17F958D2ee523a2206206994597C13D831ec7',
        decimal_places=6,
    ),
    'BNB': TokenParams(
        symbol=CODE,
        contract_address='0x55d398326f99059fF775485246999027B3197955',
        decimal_places=18,
    ),
    'TRX': TokenParams(
        symbol=CODE,
        contract_address='TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t',
        decimal_places=6,
        origin_energy_limit=10000000,
        consume_user_resource_percent=30,
    ),
    'MATIC': TokenParams(
        symbol=CODE,
        contract_address='0xc2132D05D31c914a87C6611C10748AEb04B58e8F',
        decimal_places=6,
    ),
    'AAH': TokenParams(
        symbol=CODE,
        contract_address='0x3adBF8fa04c21517D8E50908305D0413D2A44300',
        decimal_places=18,
    ),
    'KLAY': TokenParams(
        symbol=CODE,
        contract_address='0xE022f24EDd0558F22ECbd19c8Ad140a5F59B9a67',
        decimal_places=18,
    ),
    'C4EI': TokenParams(
        symbol=CODE,
        contract_address='0xf10E02Ce41b28e52AD015eaE3A83e040D4Aee3A8',
        decimal_places=18,
    )
}
USDT_CURRENCY = register_token(USDT, CODE, BLOCKCHAINS)
