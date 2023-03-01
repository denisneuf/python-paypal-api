from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils
)


class PartnerReferrals(Client):

    @PaypalEndpoint('/v2/customer/partner-referrals', method='POST')
    def post_create_partner_referrals(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/customer/partner-referrals/{}', method='GET')
    def get_referral_data(self, partnerReferralId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(partnerReferralId), params=kwargs, headers=headers)