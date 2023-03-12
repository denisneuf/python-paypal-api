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
    Use the /trackers resource to create and manage tracking information for PayPal transactions.
    """

    @PaypalEndpoint('/v1/shipping/trackers/{}', method='PUT')
    def put_tracking(self, id: str, **kwargs) -> ApiResponse:
        r"""
        :dax-operation-get:`PUT` :dax-operation-path:`/v1/shipping/trackers/{id}`

        .. _Update or cancel tracking information: https://developer.paypal.com/docs/tracking/integrate/#update-or-cancel-tracking-information

        Updates or cancels the tracking information for a PayPal transaction, by ID. To cancel tracking information, call this method and set the status to CANCELLED. For more information, see `Update or cancel tracking information`_.

        \*\*\args:

            | **id** :dax-def-type:`string` :dax-def-note:`required`

                | The ID of the tracker in the ``transaction_id-tracking_number`` format.

        \*\*\kwargs:
        Request body

            | **status** :dax-def-type:`enum` :dax-def-note:`required`

                | The status of the item shipment. For allowed values, see Shipping Statuses.

                | The possible values are:

                    - ``CANCELLED``. The shipment was cancelled and the tracking number no longer applies.
                    - ``DELIVERED``. The item was already delivered when the tracking number was uploaded.
                    - ``LOCAL_PICKUP``. Either the buyer physically picked up the item or the seller delivered the item in person without involving any couriers or postal companies.
                    - ``ON_HOLD``. The item is on hold. Its shipment was temporarily stopped due to bad weather, a strike, customs, or another reason.
                    - ``SHIPPED``. The item was shipped and is on the way.
                    - ``SHIPMENT_CREATED``. The shipment was created.
                    - ``DROPPED_OFF``. The shipment was dropped off.
                    - ``IN_TRANSIT``. The shipment is in transit on its way to the buyer.
                    - ``RETURNED``. The shipment was returned.
                    - ``LABEL_PRINTED``. The label was printed for the shipment.
                    - ``ERROR``. An error occurred with the shipment.
                    - ``UNCONFIRMED``. The shipment is unconfirmed.
                    - ``PICKUP_FAILED``. Pick-up failed for the shipment.
                    - ``DELIVERY_DELAYED``. The delivery was delayed for the shipment.
                    - ``DELIVERY_SCHEDULED``. The delivery was scheduled for the shipment.
                    - ``DELIVERY_FAILED``. The delivery failed for the shipment.
                    - ``INRETURN``. The shipment is being returned.
                    - ``IN_PROCESS``. The shipment is in process.
                    - ``NEW``. The shipment is new.
                    - ``VOID``. If the shipment is cancelled for any reason, its state is void.
                    - ``PROCESSED``. The shipment was processed.
                    - ``NOT_SHIPPED``. The shipment was not shipped.

            | **transaction_id** :dax-def-type:`string` :dax-def-note:`required`

                | The PayPal transaction ID.

            | **carrier** :dax-def-type:`enum` :dax-def-note:`required`

                | The carrier for the shipment. Some carriers have a global version as well as local subsidiaries. The subsidiaries are repeated over many countries and might also have an entry in the global list. Choose the carrier for your country. If the carrier is not available for your country, choose the global version of the carrier. If your carrier name is not in the list, set carrier_other_name to OTHER. For allowed values, see Carriers.

                | The possible values are:

                    - ``ACOMMERCE``. `aCommerce`_
                    - ``PHL_2GO``. 2GO Philippines
                    - ``AU_DHL_EXPRESS``. DHL Express Australia.
                    - ``BEL_DHL``. DHL Belgium.
                    - ``DE_DHL_DEUTSHCE_POST_INTL_SHIPMENTS``. Deutsche Post DHL Post International Germany
                    - ``IE_AN_POST_REGISTERED``. Post Registered Ireland
                    - ``AU_AU_POST``. `Australian Postal Corporation`_
                    - ``SPEEDEXCOURIER``. Speedex Courier.
                    - ``UK_ROYALMAIL_SPECIAL``. Royal Mail Special Delivery UK
                    - ``FR_COLIS``. Colis France.
                    - ``VNPOST_EMS``. Post EMS Vietnam.
                    - ``NL_FEDEX``. Federal Express Netherlands
                    - ``CN_EMS``. EMS China.
                    - ``IT_POSTE_ITALIANE``. Poste Italiane.
                    - ``HK_DHL_ECOMMERCE``. DHL eCommerce Hong Kong.
                    - ``ARAMEX``. Aramex.
                    - ``AU_OTHER``. Other - Australia.
                    - ``TW_CHUNGHWA_POST``. Chunghwa POST Taiwan
                    - ``DPEX``. `DPEX Worldwide`_
                    - ``POST_SERBIA``. `Pošta Srbije`_
                    - ``PL_POCZTEX``. Pocztex
                    - ``CNEXPS``. CN Express China.
                    - ``DIRECTLOG``. Directlog.
                    - ``ES_CORREOS_DE_ESPANA``. Correos de Espana
                    - ``BE_KIALA``. Kiala Point Belgium
                    - ``ALPHAFAST``. Alphafast.
                    - ``UKR_POSHTA``. `Ukrposhta - Ukraine's National Post`_
                    - ``CN_FEDEX``. Federal Express China
                    - ``BUYLOGIC``. `Buylogic`_
                    - ``IT_DHL_ECOMMERCE``. DHL eCommerce Italy.
                    - ``NINJAVAN_MY``. Ninjavan Malaysia.
                    - ``JPN_YAMATO``. Yamato Japan.
                    - ``POSTNORD_LOGISTICS``. Post Nord Logistics.
                    - ``US_DHL_GLOBALFORWARDING``. DHL Global Forwarding US.
                    - ``IT_SGT``. SGT Corriere Espresso Italy.
                    - ``NINJAVAN_PHILIPPINES``. Ninja Van Philippines.
                    - ``EKART``. Ekart.
                    - ``IDN_WAHANA``. Wahana Indonesia.
                    - ``FR_GLS``. `General Logistics Systems (GLS) France`_
                    - ``IDN_POS_INT``. Pos Indonesia International.
                    - ``DE_HERMES``. Hermes Germany.
                    - ``PRT_CHRONOPOST``. Chronopost Portugal.
                    - ``MYS_MYS_POST``. `Pos Malaysia`_
                    - ``WEBINTERPRET``. WebInterpret.
                    - ``BG_BULGARIAN_POST``. `Bulgarian Post`_
                    - ``NL_TPG``. TPG Post Netherlands
                    - ``CA_CANPAR``. Canpar Courier Canada
                    - ``MYS_AIRPAK``. Airpak Malaysia.
                    - ``MEX_SENDA``. Senda Mexico.
                    - ``LANDMARK_GLOBAL``. Landmark Global.
                    - ``UK_NIGHTLINE``. Nightline UK.
                    - ``JP_UPS``. United Parcel Service Japan
                    - ``UK_DHL``. DHL UK.
                    - ``SG_SG_POST``. Singapore Post.
                    - ``PHL_AIRSPEED``. Airspeed Philippines.
                    - ``DHL``. DHL Express.
                    - ``KR_KOREA_POST``. Korea Post
                    - ``JP_KURO_NEKO_YAMATO_UNYUU``. Kuro Neko Yamato Unyuu Japan
                    - ``IE_AN_POST_SWIFTPOST``. Swift Post Ireland
                    - ``CUCKOOEXPRESS``. Cuckoo Express.
                    - ``FR_OTHER``. Other - France.
                    - ``FASTRAK_TH``. Fastrak Thailand.
                    - ``AU_DHL_ECOMMERCE``. DHL eCommerce Australia.
                    - ``DE_UPS``. United Parcel Service Germany
                    - ``ESHOPWORLD``. EShopWorld.
                    - ``INTERNATIONAL_BRIDGE``. International Bridge.
                    - ``FR_COLIPOSTE``. Coliposte France
                    - ``AU_AUSTRIAN_POST``. Austrian Post.
                    - ``IND_DELHIVERY``. `Delhivery India`_
                    - ``DE_TNT``. TNT Germany.
                    - ``GLOBAL_DHL``. DHL Global.
                    - ``US_DHL_PARCEL``. DHL Parcel US.
                    - ``NL_UPS``. United Parcel Service Netherlands
                    - ``GB_APC``. `APC Overnight UK`_
                    - ``IDN_TIKI``. Tiki Indonesia.
                    - ``HERMES``. Hermes.
                    - ``ESP_NACEX``. `Nacex Spain`_
                    - ``NL_TNT``. TNT Netherlands.
                    - ``DE_FEDEX``. Federal Express Germany
                    - ``OTHER``. Other.
                    - ``BONDSCOURIERS``. Bonds Couriers.
                    - ``IT_DHL_GLOBALFORWARDING``. DHL Global Forwarding Italy.
                    - ``IDN_LION_PARCEL``. Lion Parcel Indonesia.
                    - ``UK_YODEL``. `Yodel UK`_
                    - ``IT_DHL_EXPRESS``. DHL Express Italy.
                    - ``PL_DHL_GLOBALFORWARDING``. `DHL Global Forwarding Poland`_
                    - ``DPD_POLAND``. DPD Poland.
                    - ``AU_AUSTRALIA_POST_EXPRESS_POST_PLATINUM``. Australia Post Express Post Platinum
                    - ``ES_TNT``. TNT Spain.
                    - ``CN_DHL_EXPRESS``. DHL Express Canada.
                    - ``DE_DPD``. DPD Germany.
                    - ``DE_DPD_DELISTRACK``. DPD Delistrack Germany
                    - ``CN_DHL_ECOMMERCE``. DHL eCommerce China.
                    - ``JP_TNT``. TNT Japan.
                    - ``PRT_CTT``. `CTT Expresso Portugal`_
                    - ``UK_INTERLINK_EXPRESS``. Interlink Express UK.
                    - ``NLD_POSTNL``. `PostNL Netherlands`_
                    - ``CA_DHL_ECOMMERCE``. DHL eCommerce Canada.
                    - ``SWIFTAIR``. Swift Air.
                    - ``NOR_POSTEN``. `Posten Norge`_
                    - ``MEX_REDPACK``. Redpack Mexico.
                    - ``PL_MASTERLINK``. Masterlink Poland
                    - ``PL_TNT``. TNT Express Poland
                    - ``NIM_EXPRESS``. `Nim Express`_
                    - ``PL_UPS``. United Parcel Service Poland
                    - ``UKR_NOVA``. `Nova Poshta`_
                    - ``QUANTIUM``. Quantium.
                    - ``SENDLE``. Sendle.
                    - ``SG_PARCELPOST``. Parcel Post Singapore.
                    - ``SG_NINJAVAN``. Ninjavan Singapore.
                    - ``BQC_EXPRESS``. BQC Express.
                    - ``RPD2MAN``. RPD2man Deliveries
                    - ``THA_KERRY``. Kerry Thailand.
                    - ``MEX_AEROFLASH``. Aeroflash Mexico.
                    - ``SPREADEL``. Spreadel.
                    - ``ESP_REDUR``. `Redur Spain`_
                    - ``JP_JAPANPOST``. Japan Post
                    - ``ARE_EMIRATES_POST``. `Emirates Post Group`_
                    - ``CN_CHINA_POST_EMS``. China Post EMS Express Mail Service
                    - ``UK_DHL_GLOBALFORWARDING``. DHL Global Forwarding UK.
                    - ``CN_SF_EXPRESS``. SF Express China.
                    - ``UK_FEDEX``. Federal Express UK
                    - ``POL_POCZTA``. Poczta Poland.
                    - ``YANWEN``. `Yanwen Express`_
                    - ``KOR_CJ``. CJ Korea.
                    - ``DE_DEUTSCHE_POST_DHL_WITHIN_EUROPE_TRACKNET``. Deutsche Post DHL Tracknet Germany
                    - ``IND_XPRESSBEES``. XpressBees India.
                    - ``UK_TNT``. TNT UK.
                    - ``CJ_KOREA_THAI``. `CJ Logistics in Thailand`_
                    - ``CN_OTHER``. Other - China.
                    - ``IDN_POS``. Indonesia Post.
                    - ``ABC_MAIL``. ABC Mail.
                    - ``UK_UPS``. United Parcel Service UK
                    - ``CHINA_POST``. China Post.
                    - ``PL_DHL_EXPRESS``. DHL Express Poland.
                    - ``ESP_SPANISH_SEUR``. Spanish Seur Spain
                    - ``SG_ZALORA``. Zalora Singapore.
                    - ``MATKAHUOLTO``. Matkahuoloto.
                    - ``FR_LAPOSTE``. Laposte France.
                    - ``KANGAROO_MY``. Kangaroo Express Malaysia.
                    - ``ESP_CORREOS``. `Sociedad Estatal Correos y Telégrafos`_
                    - ``NL_KIALA``. KIALA Netherlands
                    - ``IND_BLUEDART``. `Blue Dart Express DHL`_
                    - ``TUR_PTT``. PTT Turkey.
                    - ``CA_CANNOT_PROVIDE_TRACKING``. Cannot provide tracking - Canada.
                    - ``JPN_SAGAWA``. Sagawa Japan.
                    - ``MYS_SKYNET``. Skynet Malaysia.
                    - ``IT_FERCAM``. Fercam Italy.
                    - ``UK_AIRBORNE_EXPRESS``. Airborne Express UK.
                    - ``CA_OTHER``. Other - Canada.
                    - ``DE_DEUTSHCE_POST_DHL_TRACK_TRACE_EXPRESS``. Deutsche Post DHL Track Trace Express Germany
                    - ``CORREOS_DE_MEXICO``. `Mex Post Correos de Mexico`_
                    - ``FR_DHL_GLOBALFORWARDING``. DHL Global Forwarding France.
                    - ``GLOBAL_SKYNET``. Skynet Global.
                    - ``AU_DHL_GLOBALFORWARDING``. DHL Global Forwarding Australia.
                    - ``DE_DHL_GLOBALFORWARDING``. DHL Global Forwarding Germany.
                    - ``SFC_LOGISTICS``. `SFC Logistics`_
                    - ``US_GLOBEGISTICS``. Globeistics US.
                    - ``CA_DHL_GLOBALFORWARDING``. DHL Global Forwarding Canada.
                    - ``OMNIPARCEL``. Omni Parcel.
                    - ``PHL_AIR21``. Air21 Philippines
                    - ``CBL_LOGISTICA``. `CBL Logística`_
                    - ``FR_MONDIAL``. Mondial France.
                    - ``DE_DHL_ECOMMERCE``. DHL eCommerce Germany.
                    - ``ADICIONAL``. Adicional.
                    - ``CH_SWISS_POST_PRIORITY``. Swiss Post Priority
                    - ``NL_INTANGIBLE_DIGITAL_SERVICES``. Intangible Digital Services
                    - ``DE_ASENDIA``. Asendia Germany.
                    - ``NL_ABC_MAIL``. ABC Mail Netherlands
                    - ``UK_DELTEC``. Deltec UK.
                    - ``ONE_WORLD``. One World.
                    - ``AIRBORNE_EXPRESS``. Airborne Express.
                    - ``ES_OTHER``. Other - Spain.
                    - ``US_DHL_ECOMMERCE``. `DHL eCommerce US`_
                    - ``US_ENSENDA``. Ensenda US.
                    - ``CPACKET``. Cpacket.
                    - ``AXL``. `AXL Express & Logistics`_
                    - ``IND_REDEXPRESS``. Red Express India.
                    - ``NL_LOCAL_PICKUP``. Local PickUp Netherlands
                    - ``UK_ROYALMAIL_AIRSURE``. Royal Mail AirSure UK
                    - ``FR_TNT``. TNT France.
                    - ``USPS``. `United States Postal Service (USPS)`_
                    - ``RINCOS``. Rincos.
                    - ``B2CEUROPE``. B2C Europe
                    - ``PHL_LBC``. LBC Philippines.
                    - ``SG_TAQBIN``. TA-Q-BIN Parcel Singapore.
                    - ``GR_ELTA``. Elta Greece.
                    - ``WINIT``. WinIt.
                    - ``NLD_DHL``. DHL Netherlands.
                    - ``FR_GEODIS``. Geodis France.
                    - ``DE_DHL_PACKET``. DHL Packet Germany.
                    - ``ARG_OCA``. `OCA Argentia`_
                    - ``JP_DHL``. DHL Japan.
                    - ``RUSSIAN_POST``. Russian Post.
                    - ``TW_TAIWAN_POST``. `Chunghwa Post`_
                    - ``UPS``. `United Parcel Service of America, Inc.`_
                    - ``BE_BPOST``. Bpost Belgium
                    - ``JP_SAGAWA_KYUU_BIN``. Sagawa Kyuu Bin Japan
                    - ``NATIONWIDE_MY``. Nationwide Malaysia.
                    - ``TNT``. TNT Portugal.
                    - ``COURIERS_PLEASE``. Couriers Please.
                    - ``DMM_NETWORK``. DMM Network.
                    - ``TOLL``. `Toll`_
                    - ``NONE``. None
                    - ``IDN_FIRST_LOGISTICS``. First Logistics Indonesia.
                    - ``BH_POSTA``. `BH POŠTA`_
                    - ``SENDIT``. SendIt.
                    - ``US_DHL_EXPRESS``. DHL Express US.
                    - ``FEDEX``. FedEx.
                    - ``SWE_POSTNORD``. `PostNord Sverige`_
                    - ``PHL_XEND_EXPRESS``. Xend Express Philippines.
                    - ``POSTI``. Posti.
                    - ``CA_CANADA_POST``. `Canada Post`_
                    - ``PL_FEXEX``. Fexex Poland
                    - ``CN_EC``. EC China.
                    - ``HK_TAQBIN``. TA-Q-BIN Parcel Hong Kong.
                    - ``UK_AN_POST``. `AddressPay UK`_
                    - ``WISELOADS``. Wiseloads.
                    - ``PRT_SEUR``. `Seur Portugal`_
                    - ``US_ONTRAC``. Ontrac US.
                    - ``THA_THAILAND_POST``. Thailand Post.
                    - ``DPE_EXPRESS``. DPE Express.
                    - ``UK_DHL_EXPRESS``. DHL Express UK.
                    - ``NL_DHL``. DHL Netherlands
                    - ``HK_FLYT_EXPRESS``. Flyt Express Hong Kong
                    - ``UK_HERMESWORLD``. Hermesworld UK.
                    - ``IT_REGISTER_MAIL``. Registered Mail Italy.
                    - ``ARG_CORREO``. `Correo Argentino`_
                    - ``CA_LOOMIS``. Loomis Express Canada
                    - ``DTDC_AU``. DTDC Australia.
                    - ``DPD``. DPD Global.
                    - ``ASENDIA_HK``. Asendia Hong Kong.
                    - ``UK_ROYALMAIL_RECORDED``. Royal Mail Recorded UK
                    - ``PL_POCZTA_POLSKA``. Poczta Polska
                    - ``EU_IMX``. IMX EU
                    - ``IDN_PANDU``. Pandu Indonesia.
                    - ``MEX_ESTAFETA``. `Estafeta Mexico`_
                    - ``SREKOREA``. `SRE Korea`_
                    - ``CYP_CYPRUS_POST``. `Cyprus Post`_
                    - ``NZ_COURIER_POST``. `CourierPost New Zealand`_
                    - ``CN_EMPS``. EMPS China.
                    - ``AU_TNT``. TNT Australia.
                    - ``UK_CANNOT_PROVIDE_TRACKING``. Cannot provide tracking - UK.
                    - ``ES_DHL``. DHL Spain.
                    - ``CONTINENTAL``. Continental.
                    - ``IND_DTDC``. DTDC India.
                    - ``DE_GLS``. `General Logistics Systems (GLS) Germany`_
                    - ``NLD_GLS``. `General Logistics Systems (GLS) Netherlands`_
                    - ``UK_DPD``. DPD UK.
                    - ``IT_TNT``. `TNT Italy`_
                    - ``PL_DHL``. DHL Portugal.
                    - ``JP_NITTSU_PELICAN_BIN``. Nittsu Pelican Bin Japan
                    - ``THA_DYNAMIC_LOGISTICS``. Dynamic Logistics Thailand.
                    - ``IT_POSTE_ITALIA``. Poste Italia
                    - ``UK_ROYALMAIL_INTER_SIGNED``. Royal Mail International Signed UK
                    - ``HERMES_IT``. Hermes Italy.
                    - ``FR_BERT``. `Bert France`_
                    - ``IND_PROFESSIONAL_COURIERS``. Professional Couriers India.
                    - ``POL_SIODEMKA``. Siodemka Poland.
                    - ``IE_AN_POST_SDS_PRIORITY``. Post SDS Priority Ireland
                    - ``ADSONE``. `ADSone Cumulus`_
                    - ``BRA_CORREIOS``. Correios Brazil.
                    - ``UBI_LOGISTICS``. UBI Logistics.
                    - ``ES_CORREOS``. `Sociedad Estatal Correos y Telégrafos`_
                    - ``NGA_NIPOST``. `Nigerian Postal Service`_
                    - ``AUT_AUSTRIAN_POST``. Austrian Post.
                    - ``AU_FASTWAY``. Fastway Australia.
                    - ``AUS_TOLL``. Toll Australia.
                    - ``CA_CANPAR_COURIER``. Canpar Courier Canada.
                    - ``SWE_DIRECTLINK``. `Direct Link Sweden`_
                    - ``CZE_CESKA``. `Česká pošta`_
                    - ``ROYAL_MAIL``. Royal Mail.
                    - ``SG_SINGPOST``. SingPost Singapore
                    - ``IT_OTHER``. Other - Italy.
                    - ``ZA_FASTWAY``. `Fastway Couriers (South Africa)`_
                    - ``SEKOLOGISTICS``. Seko Logistics.
                    - ``CN_UPS``. CN_UPS
                    - ``HUNTER_EXPRESS``. Hunter Express.
                    - ``DE_DHL_PARCEL``. DHL Parcel Germany.
                    - ``NLD_TRANSMISSION``. Transmission Netherlands.
                    - ``CN_TNT``. TNT China.
                    - ``DE_DEUTSCHE``. Deutsche Post Germany.
                    - ``AIRSURE``. Airsure.
                    - ``UK_PARCELFORCE``. Parcelforce UK.
                    - ``SWE_DB``. `DB Schenker Sweden`_
                    - ``CN_CHINA_POST``. China Post
                    - ``PL_GLS``. General Logistics Systems Poland
                    - ``EU_BPOST``. `bpost`_
                    - ``RELAIS_COLIS``. `Relais Colis`_
                    - ``UK_DHL_PARCEL``. DHL Parcel UK.
                    - ``AUS_STARTRACK``. StarTrack Australia
                    - ``AU_TOLL_IPEC``. Toll IPEC Australia
                    - ``CORREOS_CHILE``. `CorreosChile`_
                    - ``CH_SWISS_POST_EXPRES``. Swiss Post Express
                    - ``MYS_TAQBIN``. TA-Q-BIN Parcel Malaysia.
                    - ``JET_SHIP``. Jetship.
                    - ``HK_DHL_EXPRESS``. DHL Express Hong Kong.
                    - ``IT_SDA``. `SDA Express Courier`_
                    - ``DE_DHL_DEUTSCHEPOST``. DHL Deutsche Post Germany.
                    - ``HK_DHL_GLOBALFORWARDING``. DHL Global Forwarding Hong Kong.
                    - ``PHL_RAF``. RAF Philippines.
                    - ``IT_GLS``. `General Logistics Systems (GLS) Italy`_
                    - ``PANTOS``. Pantos.
                    - ``KOR_ECARGO``. Ecargo Korea.
                    - ``AT_AUSTRIAN_POST_EMS``. EMS Express Mail Service Austria
                    - ``IT_BRT``. `BRT Corriere Espresso Italy`_
                    - ``CHE_SWISS_POST``. Swiss Post.
                    - ``FASTWAY_NZ``. Fastway New Zealand.
                    - ``IT_EBOOST_SDA``. IT_EBOOST_SDA
                    - ``ASENDIA_UK``. Asendia UK.
                    - ``RRDONNELLEY``. RR Donnelley.
                    - ``US_RL``. RL US.
                    - ``GR_GENIKI``. Geniki Greece.
                    - ``DE_DHL_EXPRESS``. DHL Express Germany.
                    - ``CA_GREYHOUND``. Greyhound Canada.
                    - ``UK_COLLECTPLUS``. `CollectPlus UK`_
                    - ``NINJAVAN_THAI``. Ninjavan Thailand.
                    - ``RABEN_GROUP``. Raben Group.
                    - ``CA_DHL_EXPRESS``. DHL Express Canada.
                    - ``GLOBAL_TNT``. TNT Global.
                    - ``IN_INDIAPOST``. India Post
                    - ``ITIS``.  ITIS International
                    - ``PHL_JAMEXPRESS``. JamExpress Philippines.
                    - ``PRT_INT_SEUR``. `Internationational Seur Portugal`_
                    - ``ESP_ASM``. `Parcel Monitor Spain`_
                    - ``NINJAVAN_ID``. Ninjavan Indonesia.
                    - ``JP_FEDEX``. Federal Express Japan
                    - ``FR_CHRONOPOST``. Chronopost France.
                    - ``FR_SUIVI``. Suivi FedEx France
                    - ``FR_TELIWAY``. Teliway France.
                    - ``JPN_JAPAN_POST``. `Japan Post`_
                    - ``HRV_HRVATSKA``. `Hrvatska Pošta`_
                    - ``AT_AUSTRIAN_POST_PAKET_PRIME``. Austrian Post Paket Prime
                    - ``DE_OTHER``. Other - Germany.
                    - ``HK_HONGKONG_POST``. Hong Kong Post.
                    - ``GRC_ACS``. ACS Greece.
                    - ``HUN_MAGYAR``. `Magyar Posta`_
                    - ``FR_DHL_PARCEL``. DHL Parcel France.
                    - ``UK_OTHER``. Other - UK.
                    - ``LWE_HK``. LWE Hong Kong.
                    - ``EFS``. `Enterprise Freight Systems (EFS)`_
                    - ``PL_DHL_PARCEL``. DHL Parcel Poland.
                    - ``PARCELFORCE``. Parcel Force.
                    - ``AU_AUSTRALIA_POST_EMS``. Australia Post EMS
                    - ``US_ASCENDIA``. Ascendia US.
                    - ``ROU_POSTA``. `Poșta Română`_
                    - ``NZ_NZ_POST``. `New Zealand Post Limited (NZ)`_
                    - ``RPX``. RPX International.
                    - ``POSTUR_IS``. Postur.
                    - ``IE_AN_POST_SDS_EMS``. Post SDS EMS Express Mail Service Ireland
                    - ``UK_UK_MAIL``. `UK Mail`_
                    - ``UK_FASTWAY``. Fastway UK.
                    - ``CORREOS_DE_COSTA_RICA``. `Correos de Costa Rica`_
                    - ``MYS_CITYLINK``. Citylink Malaysia.
                    - ``PUROLATOR``. Purolator.
                    - ``IND_DOTZOT``. `DotZot India`_
                    - ``NG_COURIERPLUS``. `Courier Plus Nigeria`_
                    - ``HK_FOUR_PX_EXPRESS``. 4PX Express Hong Kong
                    - ``ROCKETPARCEL``. `Rocket Parcel International`_
                    - ``CN_DHL_GLOBALFORWARDING``. DHL Global Forwarding China.
                    - ``EPARCEL_KR``. EParcel Korea.
                    - ``INPOST_PACZKOMATY``. InPost Paczkomaty.
                    - ``KOR_KOREA_POST``. Korea Post.
                    - ``CA_PUROLATOR``. Purolator Canada
                    - ``APR_72``. APR 72.
                    - ``FR_DHL_EXPRESS``. DHL Express France.
                    - ``IDN_JNE``. JNE Indonesia.
                    - ``AU_AUSTRALIA_POST_EPARCEL``. Australia Post Eparcel
                    - ``GLOBAL_ESTES``. Estes Global.
                    - ``LTU_LIETUVOS``. Lietuvos paštas Lithuania.
                    - ``THECOURIERGUY``. `The Courier Guy`_
                    - ``BE_CHRONOPOST``. Chronopost Belgium.
                    - ``VNM_VIETNAM_POST``. Vietnam Post.
                    - ``AU_STAR_TRACK_EXPRESS``. StarTrack Express Australia
                    - ``RAM``. `JP RAM Shipping`_


            | **carrier_name_other** :dax-def-type:`string`

                | The name of the carrier for the shipment. Provide this value only if the carrier parameter is ``OTHER``.

            | **last_updated_time** :dax-def-type:`string`

                | The date and time when the tracking information was last updated, in `Internet date and time format`_.

                | :dax-def-meta:`Minimum length:` ``20``.

                | :dax-def-meta:`Maximum length:` ``64``.

                | :dax-def-meta:`Pattern:` ``^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$``.

            | **links** :dax-def-type:`array` (contains the `link_description`_ object)

                | An array of request-related `HATEOAS links`_.

            | **notify_buyer** :dax-def-type:`boolean`

                | If ``true``, sends an email notification to the buyer of the PayPal transaction. The email contains the tracking information that was uploaded through the API.

            | **postage_payment_id** :dax-def-type:`string`

                | The postage payment ID.

            | **quantity** :dax-def-type:`integer`

                | The quantity of items shipped.

            | **shipment_date** :dax-def-type:`string`

                | The date when the shipment occurred, in `Internet date and time format`_.

                | :dax-def-meta:`Minimum length:` ``20``.

                | :dax-def-meta:`Maximum length:` ``64``.

                | :dax-def-meta:`Pattern:` ``^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$``.


            | **tracking_number** :dax-def-type:`string`

                | The tracking number for the shipment.

            | **tracking_number_type** :dax-def-type:`enum`

                | The type of tracking number.

                | The possible values are:

                    - ``CARRIER_PROVIDED``. A merchant-provided tracking number.
                    - ``E2E_PARTNER_PROVIDED``. A marketplace-provided tracking number.

            | **tracking_number_validated** :dax-def-type:`boolean`

                | Indicates whether the carrier validated the tracking number.




        """
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(id), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/shipping/trackers/{}', method='GET')
    def get_tracking(self, id: str, **kwargs) -> ApiResponse:
        r"""
        :dax-operation-get:`GET` :dax-operation-path:`/v1/shipping/trackers/{id}`

        Shows tracking information, by tracker ID, for a PayPal transaction.

        \*\*\args:

            | **id** :dax-def-type:`string` :dax-def-note:`required`

                | The ID of the tracker in the ``transaction_id-tracking_number`` format.
        """
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(id), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/shipping/trackers-batch', method='POST')
    def post_tracking(self, **kwargs) -> ApiResponse:
        r"""
        :dax-operation-get:`POST` :dax-operation-path:`/v1/shipping/trackers-batch`

        Adds tracking information, with or without tracking numbers, for multiple PayPal transactions. Accepts up to 20 tracking IDs. For more information, see `Add tracking information with tracking numbers`_ and `Add tracking information without tracking numbers`_.

        \*\*\kwargs:

            | **links** :dax-def-type:`array` (contains the `link_description`_ object)

                | An array of request-related `HATEOAS links`_.

            | **trackers** :dax-def-type:`array` (contains the `tracker`_ object)

        """
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

