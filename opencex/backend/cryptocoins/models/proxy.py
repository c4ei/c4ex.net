from core.models.inouts.withdrawal import WithdrawalRequest as BaseWithdrawalRequest


class BTCWithdrawalApprove(BaseWithdrawalRequest):
    class Meta:
        proxy = True


class ETHWithdrawalApprove(BaseWithdrawalRequest):
    class Meta:
        proxy = True


class TRXWithdrawalApprove(BaseWithdrawalRequest):
    class Meta:
        proxy = True


class BNBWithdrawalApprove(BaseWithdrawalRequest):
    class Meta:
        proxy = True


class MaticWithdrawalApprove(BaseWithdrawalRequest):
    class Meta:
        proxy = True

class AahWithdrawalApprove(BaseWithdrawalRequest):
    class Meta:
        proxy = True

class KlayWithdrawalApprove(BaseWithdrawalRequest):
    class Meta:
        proxy = True

class C4eiWithdrawalApprove(BaseWithdrawalRequest):
    class Meta:
        proxy = True
