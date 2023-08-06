__all__ = ('FillPoint',)

from expressmoney.api import *


SERVICE = 'profiles'
APP = 'antifraud'


class FillCreateContract(Contract):
    pass


class FillReadContract(Contract):
    created = serializers.DateTimeField()
    user_id = serializers.IntegerField(min_value=1)
    full_name = serializers.IntegerField()
    full_name_black_list = serializers.IntegerField()
    full_name_overdue = serializers.IntegerField()
    document = serializers.IntegerField()
    document_black_list = serializers.IntegerField()
    document_overdue = serializers.IntegerField()
    address = serializers.IntegerField()
    address_black_list = serializers.IntegerField()
    address_overdue = serializers.IntegerField()
    ip = serializers.IntegerField()
    ip_black_list = serializers.IntegerField()
    ip_overdue = serializers.IntegerField()
    fingerprint = serializers.IntegerField()
    fingerprint_black_list = serializers.IntegerField()
    fingerprint_overdue = serializers.IntegerField()
    ga = serializers.IntegerField()
    ga_black_list = serializers.IntegerField()
    ga_overdue = serializers.IntegerField()
    bank_card = serializers.IntegerField()
    bank_card_black_list = serializers.IntegerField()
    bank_card_overdue = serializers.IntegerField()
    ip_fingerprint = serializers.IntegerField()
    ip_fingerprint_black_list = serializers.IntegerField()
    ip_fingerprint_overdue = serializers.IntegerField()


class FillID(ID):
    _service = SERVICE
    _app = APP
    _view_set = 'fill'


class FillPoint(ListPointMixin, CreatePointMixin, ContractPoint):
    _point_id = FillID()
    _create_contract = FillCreateContract
    _read_contract = FillReadContract
