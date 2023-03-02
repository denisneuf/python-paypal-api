from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils
)

import logging

class Tracking(Client):
    r"""
    Merchants can use the PayPal Add Tracking API to manage tracking information. Merchants can add tracking numbers and associated information to PayPal. After adding these details to PayPal, merchants can:
    Update tracking details.
    Show tracking details.
    Cancel tracking numbers.
    """

    @PaypalEndpoint('/v1/shipping/trackers/{}', method='PUT')
    def put_traking(self, id: str, **kwargs) -> ApiResponse:
        r"""
        Updates or cancels the tracking information for a PayPal transaction, by ID. To cancel tracking information, call this method and set the status to CANCELLED.

        path **id**:string | Required. The ID of the tracker in the transaction_id-tracking_number format.

        Request body

            | **status** (enum): [required]
            | **transaction_id** (string): [required]
            | **carrier** (enum): [required]
            | **carrier_name_other** (string): [optional]
            | **last_updated_time** (string): [optional]
            | **links** (array): [optional]
            | **notify_buyer** (boolean): [optional]
            | **postage_payment_id** (string): [optional]
            | **quantity** (integer): [optional]
            | **shipment_date** (string): [optional]
            | **tracking_number** (string): [optional]
            | **tracking_number_type** (enum): [optional]
            | **tracking_number_validated** (boolean): [optional]




        """
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(id), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v1/shipping/trackers-batch', method='POST')
    def post_traking(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/shipping/trackers/{}', method='GET')
    def get_traking(self, id: str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(id), params=kwargs, headers=headers)    

