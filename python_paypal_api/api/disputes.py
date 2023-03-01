from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils
)

import logging

class Disputes(Client):


    @PaypalEndpoint('/v1/customer/disputes', method='GET')
    def list_disputes(self, **kwargs) -> ApiResponse: 	
    	return self._request(kwargs.pop('path'), params=kwargs)

    @PaypalEndpoint('/v1/customer/disputes/{}', method='GET')
    def get_dispute(self, disputeId, **kwargs) -> ApiResponse:
        contentType = "application/json"
        headers = {'Content-Type': contentType}
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(disputeId), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/customer/disputes/{}/accept-offer', method='POST')
    def accept_offer_dispute(self, disputeId, **kwargs) -> ApiResponse:
        return self._request(fPaypalEndpointParams(kwargs.pop('path')).fill(disputeId), params=kwargs, data=kwargs.pop('body'))

    @PaypalEndpoint('/v1/customer/disputes/{}/make-offer', method='POST')
    def make_offer_dispute(self, disputeId, **kwargs) -> ApiResponse:
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(disputeId), params=kwargs, data=kwargs.pop('body'))

    @PaypalEndpoint('/v1/customer/disputes/{}/escalate', method='POST')
    def escalate_dispute(self, disputeId, **kwargs) -> ApiResponse:
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(disputeId), params=kwargs, data=kwargs.pop('body'))

    @PaypalEndpoint('/v1/customer/disputes/{}/send-message', method='POST')
    def send_message(self, disputeId, **kwargs) -> ApiResponse:
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(disputeId), params=kwargs, data=kwargs.pop('body'))

    @PaypalEndpoint('/v1/customer/disputes/{}/provide-evidence', method='POST')
    def provide_evidence(self, disputeId, file, content_type='application/pdf', **kwargs) -> ApiResponse:
        
        fields={
        'input': (None, Utils.convert_body(kwargs.pop('body'), False), 'application/json'),
        'file1': ("sample2.pdf", open(file, 'rb'), 'application/pdf') # could be ignored the application but not the name .pdf
        }

        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(disputeId), params=kwargs, files=fields)

    # Important: This method is for sandbox use only.
    @PaypalEndpoint('/v1/customer/disputes/{}/require-evidence', method='POST')
    def update_dispute(self, disputeId, **kwargs) -> ApiResponse:
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(disputeId), params=kwargs, data=kwargs.pop('body'))
    
    # Important: This method is for sandbox use only.
    @PaypalEndpoint('/v1/customer/disputes/{}/adjudicate', method='POST')
    def adjudicate(self, disputeId, **kwargs) -> ApiResponse:
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(disputeId), params=kwargs, data=kwargs.pop('body'))
