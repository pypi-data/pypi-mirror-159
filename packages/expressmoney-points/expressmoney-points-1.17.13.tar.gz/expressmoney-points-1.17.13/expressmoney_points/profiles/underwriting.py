__all__ = ('UnderwritingTaskPoint', 'BankCardProcessPoint')
from expressmoney.api import *

SERVICE = 'profiles'


class UnderwritingTaskCreateContract(Contract):
    pass


class BankCardProcessCreateContract(Contract):
    bank_card_id = serializers.IntegerField(min_value=1)
    file = serializers.CharField(max_length=256)


class UnderwritingTaskID(ID):
    _service = SERVICE
    _app = 'underwriting'
    _view_set = 'underwriting_task'


class BankCardProcessID(ID):
    _service = SERVICE
    _app = 'underwriting'
    _view_set = 'bank_card_process'


class UnderwritingTaskPoint(CreatePointMixin, ContractPoint):
    _point_id = UnderwritingTaskID()
    _create_contract = UnderwritingTaskCreateContract


class BankCardProcessPoint(CreatePointMixin, ContractPoint):
    _point_id = BankCardProcessID()
    _create_contract = BankCardProcessCreateContract
