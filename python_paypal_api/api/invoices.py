from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils
)


class Invoices(Client):


    @PaypalEndpoint('/v2/invoicing/generate-next-invoice-number', method='POST')
    def post_generate_next_invoice_number(self, **kwargs) -> ApiResponse: 
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices', method='GET')
    def get_list_invoices(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices', method='POST')
    def post_draft_invoice(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}', method='DELETE')
    def post_delete_invoice(self, invoiceId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}', method='PUT')
    def put_update_invoice(self, invoiceId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}', method='GET')
    def get_invoice(self, invoiceId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}/cancel', method='POST')
    def post_cancel_invoice(self, invoiceId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}/generate-qr-code', method='POST')
    def post_generate_qr_code(self, invoiceId:str, **kwargs) -> ApiResponse: 
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}/payments', method='POST')
    def post_record_payment_invoice(self, invoiceId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}/payments/{}', method='DELETE')
    def delete_external_payment_invoice(self, invoiceId:str, transactionId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId, transactionId), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}/refunds', method='POST')
    def post_record_refund_invoice(self, invoiceId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}/refunds/{}', method='DELETE')
    def delete_external_refund_invoice(self, invoiceId:str, refundId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId, refundId), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}/remind', method='POST')
    def post_invoice_remind(self, invoiceId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/invoices/{}/send', method='POST')
    def post_send_invoice(self, invoiceId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(invoiceId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/search-invoices', method='POST')
    def post_search_invoices(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/templates', method='GET')
    def get_list_templates(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)

    @PaypalEndpoint('/v2/invoicing/templates', method='POST')
    def post_create_template(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/templates/{}', method='DELETE')
    def delete_template(self, templateId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(templateId), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/templates/{}', method='PUT')
    def put_update_template(self, templateId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(templateId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/invoicing/templates/{}', method='GET')
    def get_template(self, templateId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(templateId), params=kwargs, headers=headers)
