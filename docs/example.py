from python_paypal_api.api import Identity, Catalog
from python_paypal_api.base import PaypalApiException
import logging


def py_list_products(**kwargs):

    logging.info("---------------------------------")
    logging.info("Catalog > list_products()")
    logging.info("---------------------------------")

    credentials = dict(
        client_id="your-client-id",
        client_secret="your-client-secret",
        client_mode="your-mode" # PRODUCTION OR SANDBOX(default)
    )

    try:

        result = Catalog(credentials=credentials, store_credentials=True, debug=True).list_products(
            **kwargs
        )
        document_dict = result.payload
        logging.info(result)

    except Exception as error:
        logging.info(error)


def py_get_userinfo():

    logging.info("---------------------------------")
    logging.info("Identity > py_get_userinfo")
    logging.info("---------------------------------")

    try:

        # result = Identity(account="production", store_credentials=True, debug=True).get_userinfo(
        result = Identity(store_credentials=True, debug=True).get_userinfo(
        )
        logging.info(result)
        t1_stop = perf_counter()

    except PaypalApiException as error:
        logging.error(error)

    except Exception as error:
        logging.info(error)

if __name__ == '__main__':

    logger = logging.getLogger("test")
    
    py_get_userinfo()
    
    py_list_products(
        total_required=True,
        page_size=1,
        page=2
    )
