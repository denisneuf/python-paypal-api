from enum import Enum

class EndPoint(Enum):
    PRODUCTION = "api.paypal.com"
    SANDBOX = "api.sandbox.paypal.com"

class ProductType(str, Enum):
    PHYSICAL = 'PHYSICAL'
    DIGITAL = 'DIGITAL'
    SERVICE = 'SERVICE'

class CategoryType(str, Enum):
    AC_REFRIGERATION_REPAIR = 'AC_REFRIGERATION_REPAIR'
    ACADEMIC_SOFTWARE = 'ACADEMIC_SOFTWARE'
    ACCESSORIES = 'ACCESSORIES'
    ACCOUNTING = 'ACCOUNTING'
    ADULT = 'ADULT'
    ADVERTISING = 'ADVERTISING'
    AFFILIATED_AUTO_RENTAL = 'AFFILIATED_AUTO_RENTAL'
    AGENCIES = 'AGENCIES'
    AGGREGATORS = 'AGGREGATORS'
    AGRICULTURAL_COOPERATIVE_FOR_MAIL_ORDER = 'AGRICULTURAL_COOPERATIVE_FOR_MAIL_ORDER'
    AIR_CARRIERS_AIRLINES = 'AIR_CARRIERS_AIRLINES'
    AIRLINES = 'AIRLINES'
    AIRPORTS_FLYING_FIELDS = 'AIRPORTS_FLYING_FIELDS'
    ALCOHOLIC_BEVERAGES = 'ALCOHOLIC_BEVERAGES'
    AMUSEMENT_PARKS_CARNIVALS = 'AMUSEMENT_PARKS_CARNIVALS'
    ANIMATION = 'ANIMATION'
    ANTIQUES = 'ANTIQUES'
    APPLIANCES = 'APPLIANCES'
    AQUARIAMS_SEAQUARIUMS_DOLPHINARIUMS = 'AQUARIAMS_SEAQUARIUMS_DOLPHINARIUMS'
    ARCHITECTURAL_ENGINEERING_AND_SURVEYING_SERVICES = 'ARCHITECTURAL_ENGINEERING_AND_SURVEYING_SERVICES'
    ART_AND_CRAFT_SUPPLIES = 'ART_AND_CRAFT_SUPPLIES'
    ART_DEALERS_AND_GALLERIES = 'ART_DEALERS_AND_GALLERIES'
    ARTIFACTS_GRAVE_RELATED_AND_NATIVE_AMERICAN_CRAFTS = 'ARTIFACTS_GRAVE_RELATED_AND_NATIVE_AMERICAN_CRAFTS'
    ARTS_AND_CRAFTS = 'ARTS_AND_CRAFTS'
    ARTS_CRAFTS_AND_COLLECTIBLES = 'ARTS_CRAFTS_AND_COLLECTIBLES'
    AUDIO_BOOKS = 'AUDIO_BOOKS'
    AUTO_ASSOCIATIONS_CLUBS = 'AUTO_ASSOCIATIONS_CLUBS'
    AUTO_DEALER_USED_ONLY = 'AUTO_DEALER_USED_ONLY'
    AUTO_RENTALS = 'AUTO_RENTALS'
    AUTO_SERVICE = 'AUTO_SERVICE'
    AUTOMATED_FUEL_DISPENSERS = 'AUTOMATED_FUEL_DISPENSERS'
    AUTOMOBILE_ASSOCIATIONS = 'AUTOMOBILE_ASSOCIATIONS'
    AUTOMOTIVE = 'AUTOMOTIVE'
    AUTOMOTIVE_REPAIR_SHOPS_NON_DEALER = 'AUTOMOTIVE_REPAIR_SHOPS_NON_DEALER'
    AUTOMOTIVE_TOP_AND_BODY_SHOPS = 'AUTOMOTIVE_TOP_AND_BODY_SHOPS'
    AVIATION = 'AVIATION'
    BABIES_CLOTHING_AND_SUPPLIES = 'BABIES_CLOTHING_AND_SUPPLIES'
    BABY = 'BABY'
    BANDS_ORCHESTRAS_ENTERTAINERS = 'BANDS_ORCHESTRAS_ENTERTAINERS'
    BARBIES = 'BARBIES'
    BATH_AND_BODY = 'BATH_AND_BODY'
    BATTERIES = 'BATTERIES'
    BEAN_BABIES = 'BEAN_BABIES'
    BEAUTY = 'BEAUTY'
    BEAUTY_AND_FRAGRANCES = 'BEAUTY_AND_FRAGRANCES'
    BED_AND_BATH = 'BED_AND_BATH'
    BICYCLE_SHOPS_SALES_AND_SERVICE = 'BICYCLE_SHOPS_SALES_AND_SERVICE'
    BICYCLES_AND_ACCESSORIES = 'BICYCLES_AND_ACCESSORIES'
    BILLIARD_POOL_ESTABLISHMENTS = 'BILLIARD_POOL_ESTABLISHMENTS'
    BOAT_DEALERS = 'BOAT_DEALERS'
    BOAT_RENTALS_AND_LEASING = 'BOAT_RENTALS_AND_LEASING'
    BOATING_SAILING_AND_ACCESSORIES = 'BOATING_SAILING_AND_ACCESSORIES'
    BOOKS = 'BOOKS'
    BOOKS_AND_MAGAZINES = 'BOOKS_AND_MAGAZINES'
    BOOKS_MANUSCRIPTS = 'BOOKS_MANUSCRIPTS'
    BOOKS_PERIODICALS_AND_NEWSPAPERS = 'BOOKS_PERIODICALS_AND_NEWSPAPERS'
    BOWLING_ALLEYS = 'BOWLING_ALLEYS'
    BULLETIN_BOARD = 'BULLETIN_BOARD'
    BUS_LINE = 'BUS_LINE'
    BUS_LINES_CHARTERS_TOUR_BUSES = 'BUS_LINES_CHARTERS_TOUR_BUSES'
    BUSINESS = 'BUSINESS'
    BUSINESS_AND_SECRETARIAL_SCHOOLS = 'BUSINESS_AND_SECRETARIAL_SCHOOLS'
    BUYING_AND_SHOPPING_SERVICES_AND_CLUBS = 'BUYING_AND_SHOPPING_SERVICES_AND_CLUBS'
    CABLE_SATELLITE_AND_OTHER_PAY_TELEVISION_AND_RADIO_SERVICES = 'CABLE_SATELLITE_AND_OTHER_PAY_TELEVISION_AND_RADIO_SERVICES'
    CABLE_SATELLITE_AND_OTHER_PAY_TV_AND_RADIO = 'CABLE_SATELLITE_AND_OTHER_PAY_TV_AND_RADIO'
    CAMERA_AND_PHOTOGRAPHIC_SUPPLIES = 'CAMERA_AND_PHOTOGRAPHIC_SUPPLIES'
    CAMERAS = 'CAMERAS'
    CAMERAS_AND_PHOTOGRAPHY = 'CAMERAS_AND_PHOTOGRAPHY'
    CAMPER_RECREATIONAL_AND_UTILITY_TRAILER_DEALERS = 'CAMPER_RECREATIONAL_AND_UTILITY_TRAILER_DEALERS'
    CAMPING_AND_OUTDOORS = 'CAMPING_AND_OUTDOORS'
    CAMPING_AND_SURVIVAL = 'CAMPING_AND_SURVIVAL'
    CAR_AND_TRUCK_DEALERS = 'CAR_AND_TRUCK_DEALERS'
    CAR_AND_TRUCK_DEALERS_USED_ONLY = 'CAR_AND_TRUCK_DEALERS_USED_ONLY'
    CAR_AUDIO_AND_ELECTRONICS = 'CAR_AUDIO_AND_ELECTRONICS'
    CAR_RENTAL_AGENCY = 'CAR_RENTAL_AGENCY'
    CATALOG_MERCHANT = 'CATALOG_MERCHANT'
    CATALOG_RETAIL_MERCHANT = 'CATALOG_RETAIL_MERCHANT'
    CATERING_SERVICES = 'CATERING_SERVICES'
    CHARITY = 'CHARITY'
    CHECK_CASHIER = 'CHECK_CASHIER'
    CHILD_CARE_SERVICES = 'CHILD_CARE_SERVICES'
    CHILDREN_BOOKS = 'CHILDREN_BOOKS'
    CHIROPODISTS_PODIATRISTS = 'CHIROPODISTS_PODIATRISTS'
    CHIROPRACTORS = 'CHIROPRACTORS'
    CIGAR_STORES_AND_STANDS = 'CIGAR_STORES_AND_STANDS'
    CIVIC_SOCIAL_FRATERNAL_ASSOCIATIONS = 'CIVIC_SOCIAL_FRATERNAL_ASSOCIATIONS'
    CIVIL_SOCIAL_FRAT_ASSOCIATIONS = 'CIVIL_SOCIAL_FRAT_ASSOCIATIONS'
    CLOTHING = 'CLOTHING'
    CLOTHING_ACCESSORIES_AND_SHOES = 'CLOTHING_ACCESSORIES_AND_SHOES'
    CLOTHING_RENTAL = 'CLOTHING_RENTAL'
    COFFEE_AND_TEA = 'COFFEE_AND_TEA'
    COIN_OPERATED_BANKS_AND_CASINOS = 'COIN_OPERATED_BANKS_AND_CASINOS'
    COLLECTIBLES = 'COLLECTIBLES'
    COLLECTION_AGENCY = 'COLLECTION_AGENCY'
    COLLEGES_AND_UNIVERSITIES = 'COLLEGES_AND_UNIVERSITIES'
    COMMERCIAL_EQUIPMENT = 'COMMERCIAL_EQUIPMENT'
    COMMERCIAL_FOOTWEAR = 'COMMERCIAL_FOOTWEAR'
    COMMERCIAL_PHOTOGRAPHY = 'COMMERCIAL_PHOTOGRAPHY'
    COMMERCIAL_PHOTOGRAPHY_ART_AND_GRAPHICS = 'COMMERCIAL_PHOTOGRAPHY_ART_AND_GRAPHICS'
    COMMERCIAL_SPORTS_PROFESSIONA = 'COMMERCIAL_SPORTS_PROFESSIONA'
    COMMODITIES_AND_FUTURES_EXCHANGE = 'COMMODITIES_AND_FUTURES_EXCHANGE'
    COMPUTER_AND_DATA_PROCESSING_SERVICES = 'COMPUTER_AND_DATA_PROCESSING_SERVICES'
    COMPUTER_HARDWARE_AND_SOFTWARE = 'COMPUTER_HARDWARE_AND_SOFTWARE'
    COMPUTER_MAINTENANCE_REPAIR_AND_SERVICES_NOT_ELSEWHERE_CLAS = 'COMPUTER_MAINTENANCE_REPAIR_AND_SERVICES_NOT_ELSEWHERE_CLAS'
    CONSTRUCTION = 'CONSTRUCTION'
    CONSTRUCTION_MATERIALS_NOT_ELSEWHERE_CLASSIFIED = 'CONSTRUCTION_MATERIALS_NOT_ELSEWHERE_CLASSIFIED'
    CONSULTING_SERVICES = 'CONSULTING_SERVICES'
    CONSUMER_CREDIT_REPORTING_AGENCIES = 'CONSUMER_CREDIT_REPORTING_AGENCIES'
    CONVALESCENT_HOMES = 'CONVALESCENT_HOMES'
    COSMETIC_STORES = 'COSMETIC_STORES'
    COUNSELING_SERVICES_DEBT_MARRIAGE_PERSONAL = 'COUNSELING_SERVICES_DEBT_MARRIAGE_PERSONAL'
    COUNTERFEIT_CURRENCY_AND_STAMPS = 'COUNTERFEIT_CURRENCY_AND_STAMPS'
    COUNTERFEIT_ITEMS = 'COUNTERFEIT_ITEMS'
    COUNTRY_CLUBS = 'COUNTRY_CLUBS'
    COURIER_SERVICES = 'COURIER_SERVICES'
    COURIER_SERVICES_AIR_AND_GROUND_AND_FREIGHT_FORWARDERS = 'COURIER_SERVICES_AIR_AND_GROUND_AND_FREIGHT_FORWARDERS'
    COURT_COSTS_ALIMNY_CHILD_SUPT = 'COURT_COSTS_ALIMNY_CHILD_SUPT'
    COURT_COSTS_INCLUDING_ALIMONY_AND_CHILD_SUPPORT_COURTS_OF_LAW = 'COURT_COSTS_INCLUDING_ALIMONY_AND_CHILD_SUPPORT_COURTS_OF_LAW'
    CREDIT_CARDS = 'CREDIT_CARDS'
    CREDIT_UNION = 'CREDIT_UNION'
    CULTURE_AND_RELIGION = 'CULTURE_AND_RELIGION'
    DAIRY_PRODUCTS_STORES = 'DAIRY_PRODUCTS_STORES'
    DANCE_HALLS_STUDIOS_AND_SCHOOLS = 'DANCE_HALLS_STUDIOS_AND_SCHOOLS'
    DECORATIVE = 'DECORATIVE'
    DENTAL = 'DENTAL'
    DENTISTS_AND_ORTHODONTISTS = 'DENTISTS_AND_ORTHODONTISTS'
    DEPARTMENT_STORES = 'DEPARTMENT_STORES'
    DESKTOP_PCS = 'DESKTOP_PCS'
    DEVICES = 'DEVICES'
    DIECAST_TOYS_VEHICLES = 'DIECAST_TOYS_VEHICLES'
    DIGITAL_GAMES = 'DIGITAL_GAMES'
    DIGITAL_MEDIA_BOOKS_MOVIES_MUSIC = 'DIGITAL_MEDIA_BOOKS_MOVIES_MUSIC'
    DIRECT_MARKETING = 'DIRECT_MARKETING'
    DIRECT_MARKETING_CATALOG_MERCHANT = 'DIRECT_MARKETING_CATALOG_MERCHANT'
    DIRECT_MARKETING_INBOUND_TELE = 'DIRECT_MARKETING_INBOUND_TELE'
    DIRECT_MARKETING_OUTBOUND_TELE = 'DIRECT_MARKETING_OUTBOUND_TELE'
    DIRECT_MARKETING_SUBSCRIPTION = 'DIRECT_MARKETING_SUBSCRIPTION'
    DISCOUNT_STORES = 'DISCOUNT_STORES'
    DOOR_TO_DOOR_SALES = 'DOOR_TO_DOOR_SALES'
    DRAPERY_WINDOW_COVERING_AND_UPHOLSTERY = 'DRAPERY_WINDOW_COVERING_AND_UPHOLSTERY'
    DRINKING_PLACES = 'DRINKING_PLACES'
    DRUGSTORE = 'DRUGSTORE'
    DURABLE_GOODS = 'DURABLE_GOODS'
    ECOMMERCE_DEVELOPMENT = 'ECOMMERCE_DEVELOPMENT'
    ECOMMERCE_SERVICES = 'ECOMMERCE_SERVICES'
    EDUCATIONAL_AND_TEXTBOOKS = 'EDUCATIONAL_AND_TEXTBOOKS'
    ELECTRIC_RAZOR_STORES = 'ELECTRIC_RAZOR_STORES'
    ELECTRICAL_AND_SMALL_APPLIANCE_REPAIR = 'ELECTRICAL_AND_SMALL_APPLIANCE_REPAIR'
    ELECTRICAL_CONTRACTORS = 'ELECTRICAL_CONTRACTORS'
    ELECTRICAL_PARTS_AND_EQUIPMENT = 'ELECTRICAL_PARTS_AND_EQUIPMENT'
    ELECTRONIC_CASH = 'ELECTRONIC_CASH'
    ELEMENTARY_AND_SECONDARY_SCHOOLS = 'ELEMENTARY_AND_SECONDARY_SCHOOLS'
    EMPLOYMENT = 'EMPLOYMENT'
    ENTERTAINERS = 'ENTERTAINERS'
    ENTERTAINMENT_AND_MEDIA = 'ENTERTAINMENT_AND_MEDIA'
    EQUIP_TOOL_FURNITURE_AND_APPLIANCE_RENTAL_AND_LEASING = 'EQUIP_TOOL_FURNITURE_AND_APPLIANCE_RENTAL_AND_LEASING'
    ESCROW = 'ESCROW'
    EVENT_AND_WEDDING_PLANNING = 'EVENT_AND_WEDDING_PLANNING'
    EXERCISE_AND_FITNESS = 'EXERCISE_AND_FITNESS'
    EXERCISE_EQUIPMENT = 'EXERCISE_EQUIPMENT'
    EXTERMINATING_AND_DISINFECTING_SERVICES = 'EXTERMINATING_AND_DISINFECTING_SERVICES'
    FABRICS_AND_SEWING = 'FABRICS_AND_SEWING'
    FAMILY_CLOTHING_STORES = 'FAMILY_CLOTHING_STORES'
    FASHION_JEWELRY = 'FASHION_JEWELRY'
    FAST_FOOD_RESTAURANTS = 'FAST_FOOD_RESTAURANTS'
    FICTION_AND_NONFICTION = 'FICTION_AND_NONFICTION'
    FINANCE_COMPANY = 'FINANCE_COMPANY'
    FINANCIAL_AND_INVESTMENT_ADVICE = 'FINANCIAL_AND_INVESTMENT_ADVICE'
    FINANCIAL_INSTITUTIONS_MERCHANDISE_AND_SERVICES = 'FINANCIAL_INSTITUTIONS_MERCHANDISE_AND_SERVICES'
    FIREARM_ACCESSORIES = 'FIREARM_ACCESSORIES'
    FIREARMS_WEAPONS_AND_KNIVES = 'FIREARMS_WEAPONS_AND_KNIVES'
    FIREPLACE_AND_FIREPLACE_SCREENS = 'FIREPLACE_AND_FIREPLACE_SCREENS'
    FIREWORKS = 'FIREWORKS'
    FISHING = 'FISHING'
    FLORISTS = 'FLORISTS'
    FLOWERS = 'FLOWERS'
    FOOD_DRINK_AND_NUTRITION = 'FOOD_DRINK_AND_NUTRITION'
    FOOD_PRODUCTS = 'FOOD_PRODUCTS'
    FOOD_RETAIL_AND_SERVICE = 'FOOD_RETAIL_AND_SERVICE'
    FRAGRANCES_AND_PERFUMES = 'FRAGRANCES_AND_PERFUMES'
    FREEZER_AND_LOCKER_MEAT_PROVISIONERS = 'FREEZER_AND_LOCKER_MEAT_PROVISIONERS'
    FUEL_DEALERS_FUEL_OIL_WOOD_AND_COAL = 'FUEL_DEALERS_FUEL_OIL_WOOD_AND_COAL'
    FUEL_DEALERS_NON_AUTOMOTIVE = 'FUEL_DEALERS_NON_AUTOMOTIVE'
    FUNERAL_SERVICES_AND_CREMATORIES = 'FUNERAL_SERVICES_AND_CREMATORIES'
    FURNISHING_AND_DECORATING = 'FURNISHING_AND_DECORATING'
    FURNITURE = 'FURNITURE'
    FURRIERS_AND_FUR_SHOPS = 'FURRIERS_AND_FUR_SHOPS'
    GADGETS_AND_OTHER_ELECTRONICS = 'GADGETS_AND_OTHER_ELECTRONICS'
    GAMBLING = 'GAMBLING'
    GAME_SOFTWARE = 'GAME_SOFTWARE'
    GAMES = 'GAMES'
    GARDEN_SUPPLIES = 'GARDEN_SUPPLIES'
    GENERAL = 'GENERAL'
    GENERAL_CONTRACTORS = 'GENERAL_CONTRACTORS'
    GENERAL_GOVERNMENT = 'GENERAL_GOVERNMENT'
    GENERAL_SOFTWARE = 'GENERAL_SOFTWARE'
    GENERAL_TELECOM = 'GENERAL_TELECOM'
    GIFTS_AND_FLOWERS = 'GIFTS_AND_FLOWERS'
    GLASS_PAINT_AND_WALLPAPER_STORES = 'GLASS_PAINT_AND_WALLPAPER_STORES'
    GLASSWARE_CRYSTAL_STORES = 'GLASSWARE_CRYSTAL_STORES'
    GOVERNMENT = 'GOVERNMENT'
    GOVERNMENT_IDS_AND_LICENSES = 'GOVERNMENT_IDS_AND_LICENSES'
    GOVERNMENT_LICENSED_ON_LINE_CASINOS_ON_LINE_GAMBLING = 'GOVERNMENT_LICENSED_ON_LINE_CASINOS_ON_LINE_GAMBLING'
    GOVERNMENT_OWNED_LOTTERIES = 'GOVERNMENT_OWNED_LOTTERIES'
    GOVERNMENT_SERVICES = 'GOVERNMENT_SERVICES'
    GRAPHIC_AND_COMMERCIAL_DESIGN = 'GRAPHIC_AND_COMMERCIAL_DESIGN'
    GREETING_CARDS = 'GREETING_CARDS'
    GROCERY_STORES_AND_SUPERMARKETS = 'GROCERY_STORES_AND_SUPERMARKETS'
    HARDWARE_AND_TOOLS = 'HARDWARE_AND_TOOLS'
    HARDWARE_EQUIPMENT_AND_SUPPLIES = 'HARDWARE_EQUIPMENT_AND_SUPPLIES'
    HAZARDOUS_RESTRICTED_AND_PERISHABLE_ITEMS = 'HAZARDOUS_RESTRICTED_AND_PERISHABLE_ITEMS'
    HEALTH_AND_BEAUTY_SPAS = 'HEALTH_AND_BEAUTY_SPAS'
    HEALTH_AND_NUTRITION = 'HEALTH_AND_NUTRITION'
    HEALTH_AND_PERSONAL_CARE = 'HEALTH_AND_PERSONAL_CARE'
    HEARING_AIDS_SALES_AND_SUPPLIES = 'HEARING_AIDS_SALES_AND_SUPPLIES'
    HEATING_PLUMBING_AC = 'HEATING_PLUMBING_AC'
    HIGH_RISK_MERCHANT = 'HIGH_RISK_MERCHANT'
    HIRING_SERVICES = 'HIRING_SERVICES'
    HOBBIES_TOYS_AND_GAMES = 'HOBBIES_TOYS_AND_GAMES'
    HOME_AND_GARDEN = 'HOME_AND_GARDEN'
    HOME_AUDIO = 'HOME_AUDIO'
    HOME_DECOR = 'HOME_DECOR'
    HOME_ELECTRONICS = 'HOME_ELECTRONICS'
    HOSPITALS = 'HOSPITALS'
    HOTELS_MOTELS_INNS_RESORTS = 'HOTELS_MOTELS_INNS_RESORTS'
    HOUSEWARES = 'HOUSEWARES'
    HUMAN_PARTS_AND_REMAINS = 'HUMAN_PARTS_AND_REMAINS'
    HUMOROUS_GIFTS_AND_NOVELTIES = 'HUMOROUS_GIFTS_AND_NOVELTIES'
    HUNTING = 'HUNTING'
    IDS_LICENSES_AND_PASSPORTS = 'IDS_LICENSES_AND_PASSPORTS'
    ILLEGAL_DRUGS_AND_PARAPHERNALIA = 'ILLEGAL_DRUGS_AND_PARAPHERNALIA'
    INDUSTRIAL = 'INDUSTRIAL'
    INDUSTRIAL_AND_MANUFACTURING_SUPPLIES = 'INDUSTRIAL_AND_MANUFACTURING_SUPPLIES'
    INSURANCE_AUTO_AND_HOME = 'INSURANCE_AUTO_AND_HOME'
    INSURANCE_DIRECT = 'INSURANCE_DIRECT'
    INSURANCE_LIFE_AND_ANNUITY = 'INSURANCE_LIFE_AND_ANNUITY'
    INSURANCE_SALES_UNDERWRITING = 'INSURANCE_SALES_UNDERWRITING'
    INSURANCE_UNDERWRITING_PREMIUMS = 'INSURANCE_UNDERWRITING_PREMIUMS'
    INTERNET_AND_NETWORK_SERVICES = 'INTERNET_AND_NETWORK_SERVICES'
    INTRA_COMPANY_PURCHASES = 'INTRA_COMPANY_PURCHASES'
    LABORATORIES_DENTAL_MEDICAL = 'LABORATORIES_DENTAL_MEDICAL'
    LANDSCAPING = 'LANDSCAPING'
    LANDSCAPING_AND_HORTICULTURAL_SERVICES = 'LANDSCAPING_AND_HORTICULTURAL_SERVICES'
    LAUNDRY_CLEANING_SERVICES = 'LAUNDRY_CLEANING_SERVICES'
    LEGAL = 'LEGAL'
    LEGAL_SERVICES_AND_ATTORNEYS = 'LEGAL_SERVICES_AND_ATTORNEYS'
    LOCAL_DELIVERY_SERVICE = 'LOCAL_DELIVERY_SERVICE'
    LOCKSMITH = 'LOCKSMITH'
    LODGING_AND_ACCOMMODATIONS = 'LODGING_AND_ACCOMMODATIONS'
    LOTTERY_AND_CONTESTS = 'LOTTERY_AND_CONTESTS'
    LUGGAGE_AND_LEATHER_GOODS = 'LUGGAGE_AND_LEATHER_GOODS'
    LUMBER_AND_BUILDING_MATERIALS = 'LUMBER_AND_BUILDING_MATERIALS'
    MAGAZINES = 'MAGAZINES'
    MAINTENANCE_AND_REPAIR_SERVICES = 'MAINTENANCE_AND_REPAIR_SERVICES'
    MAKEUP_AND_COSMETICS = 'MAKEUP_AND_COSMETICS'
    MANUAL_CASH_DISBURSEMENTS = 'MANUAL_CASH_DISBURSEMENTS'
    MASSAGE_PARLORS = 'MASSAGE_PARLORS'
    MEDICAL = 'MEDICAL'
    MEDICAL_AND_PHARMACEUTICAL = 'MEDICAL_AND_PHARMACEUTICAL'
    MEDICAL_CARE = 'MEDICAL_CARE'
    MEDICAL_EQUIPMENT_AND_SUPPLIES = 'MEDICAL_EQUIPMENT_AND_SUPPLIES'
    MEDICAL_SERVICES = 'MEDICAL_SERVICES'
    MEETING_PLANNERS = 'MEETING_PLANNERS'
    MEMBERSHIP_CLUBS_AND_ORGANIZATIONS = 'MEMBERSHIP_CLUBS_AND_ORGANIZATIONS'
    MEMBERSHIP_COUNTRY_CLUBS_GOLF = 'MEMBERSHIP_COUNTRY_CLUBS_GOLF'
    MEMORABILIA = 'MEMORABILIA'
    MEN_AND_BOY_CLOTHING_AND_ACCESSORY_STORES = 'MEN_AND_BOY_CLOTHING_AND_ACCESSORY_STORES'
    MEN_CLOTHING = 'MEN_CLOTHING'
    MERCHANDISE = 'MERCHANDISE'
    METAPHYSICAL = 'METAPHYSICAL'
    MILITARIA = 'MILITARIA'
    MILITARY_AND_CIVIL_SERVICE_UNIFORMS = 'MILITARY_AND_CIVIL_SERVICE_UNIFORMS'
    MISC_AUTOMOTIVE_AIRCRAFT_AND_FARM_EQUIPMENT_DEALERS = 'MISC._AUTOMOTIVE_AIRCRAFT_AND_FARM_EQUIPMENT_DEALERS'
    MISC_GENERAL_MERCHANDISE = 'MISC._GENERAL_MERCHANDISE'
    MISCELLANEOUS_GENERAL_SERVICES = 'MISCELLANEOUS_GENERAL_SERVICES'
    MISCELLANEOUS_REPAIR_SHOPS_AND_RELATED_SERVICES = 'MISCELLANEOUS_REPAIR_SHOPS_AND_RELATED_SERVICES'
    MODEL_KITS = 'MODEL_KITS'
    MONEY_TRANSFER_MEMBER_FINANCIAL_INSTITUTION = 'MONEY_TRANSFER_MEMBER_FINANCIAL_INSTITUTION'
    MONEY_TRANSFER_MERCHANT = 'MONEY_TRANSFER_MERCHANT'
    MOTION_PICTURE_THEATERS = 'MOTION_PICTURE_THEATERS'
    MOTOR_FREIGHT_CARRIERS_AND_TRUCKING = 'MOTOR_FREIGHT_CARRIERS_AND_TRUCKING'
    MOTOR_HOME_AND_RECREATIONAL_VEHICLE_RENTAL = 'MOTOR_HOME_AND_RECREATIONAL_VEHICLE_RENTAL'
    MOTOR_HOMES_DEALERS = 'MOTOR_HOMES_DEALERS'
    MOTOR_VEHICLE_SUPPLIES_AND_NEW_PARTS = 'MOTOR_VEHICLE_SUPPLIES_AND_NEW_PARTS'
    MOTORCYCLE_DEALERS = 'MOTORCYCLE_DEALERS'
    MOTORCYCLES = 'MOTORCYCLES'
    MOVIE = 'MOVIE'
    MOVIE_TICKETS = 'MOVIE_TICKETS'
    MOVING_AND_STORAGE = 'MOVING_AND_STORAGE'
    MULTI_LEVEL_MARKETING = 'MULTI_LEVEL_MARKETING'
    MUSIC_CDS_CASSETTES_AND_ALBUMS = 'MUSIC_CDS_CASSETTES_AND_ALBUMS'
    MUSIC_STORE_INSTRUMENTS_AND_SHEET_MUSIC = 'MUSIC_STORE_INSTRUMENTS_AND_SHEET_MUSIC'
    NETWORKING = 'NETWORKING'
    NEW_AGE = 'NEW_AGE'
    NEW_PARTS_AND_SUPPLIES_MOTOR_VEHICLE = 'NEW_PARTS_AND_SUPPLIES_MOTOR_VEHICLE'
    NEWS_DEALERS_AND_NEWSTANDS = 'NEWS_DEALERS_AND_NEWSTANDS'
    NON_DURABLE_GOODS = 'NON_DURABLE_GOODS'
    NON_FICTION = 'NON_FICTION'
    NON_PROFIT_POLITICAL_AND_RELIGION = 'NON_PROFIT_POLITICAL_AND_RELIGION'
    NONPROFIT = 'NONPROFIT'
    NOVELTIES = 'NOVELTIES'
    OEM_SOFTWARE = 'OEM_SOFTWARE'
    OFFICE_SUPPLIES_AND_EQUIPMENT = 'OFFICE_SUPPLIES_AND_EQUIPMENT'
    ONLINE_DATING = 'ONLINE_DATING'
    ONLINE_GAMING = 'ONLINE_GAMING'
    ONLINE_GAMING_CURRENCY = 'ONLINE_GAMING_CURRENCY'
    ONLINE_SERVICES = 'ONLINE_SERVICES'
    OOUTBOUND_TELEMARKETING_MERCH = 'OOUTBOUND_TELEMARKETING_MERCH'
    OPHTHALMOLOGISTS_OPTOMETRIST = 'OPHTHALMOLOGISTS_OPTOMETRIST'
    OPTICIANS_AND_DISPENSING = 'OPTICIANS_AND_DISPENSING'
    ORTHOPEDIC_GOODS_PROSTHETICS = 'ORTHOPEDIC_GOODS_PROSTHETICS'
    OSTEOPATHS = 'OSTEOPATHS'
    OTHER = 'OTHER'
    PACKAGE_TOUR_OPERATORS = 'PACKAGE_TOUR_OPERATORS'
    PAINTBALL = 'PAINTBALL'
    PAINTS_VARNISHES_AND_SUPPLIES = 'PAINTS_VARNISHES_AND_SUPPLIES'
    PARKING_LOTS_AND_GARAGES = 'PARKING_LOTS_AND_GARAGES'
    PARTS_AND_ACCESSORIES = 'PARTS_AND_ACCESSORIES'
    PAWN_SHOPS = 'PAWN_SHOPS'
    PAYCHECK_LENDER_OR_CASH_ADVANCE = 'PAYCHECK_LENDER_OR_CASH_ADVANCE'
    PERIPHERALS = 'PERIPHERALS'
    PERSONALIZED_GIFTS = 'PERSONALIZED_GIFTS'
    PET_SHOPS_PET_FOOD_AND_SUPPLIES = 'PET_SHOPS_PET_FOOD_AND_SUPPLIES'
    PETROLEUM_AND_PETROLEUM_PRODUCTS = 'PETROLEUM_AND_PETROLEUM_PRODUCTS'
    PETS_AND_ANIMALS = 'PETS_AND_ANIMALS'
    PHOTOFINISHING_LABORATORIES_PHOTO_DEVELOPING = 'PHOTOFINISHING_LABORATORIES_PHOTO_DEVELOPING'
    PHOTOGRAPHIC_STUDIOS_PORTRAITS = 'PHOTOGRAPHIC_STUDIOS_PORTRAITS'
    PHOTOGRAPHY = 'PHOTOGRAPHY'
    PHYSICAL_GOOD = 'PHYSICAL_GOOD'
    PICTURE_VIDEO_PRODUCTION = 'PICTURE_VIDEO_PRODUCTION'
    PIECE_GOODS_NOTIONS_AND_OTHER_DRY_GOODS = 'PIECE_GOODS_NOTIONS_AND_OTHER_DRY_GOODS'
    PLANTS_AND_SEEDS = 'PLANTS_AND_SEEDS'
    PLUMBING_AND_HEATING_EQUIPMENTS_AND_SUPPLIES = 'PLUMBING_AND_HEATING_EQUIPMENTS_AND_SUPPLIES'
    POLICE_RELATED_ITEMS = 'POLICE_RELATED_ITEMS'
    POLITICAL_ORGANIZATIONS = 'POLITICAL_ORGANIZATIONS'
    POSTAL_SERVICES_GOVERNMENT_ONLY = 'POSTAL_SERVICES_GOVERNMENT_ONLY'
    POSTERS = 'POSTERS'
    PREPAID_AND_STORED_VALUE_CARDS = 'PREPAID_AND_STORED_VALUE_CARDS'
    PRESCRIPTION_DRUGS = 'PRESCRIPTION_DRUGS'
    PROMOTIONAL_ITEMS = 'PROMOTIONAL_ITEMS'
    PUBLIC_WAREHOUSING_AND_STORAGE = 'PUBLIC_WAREHOUSING_AND_STORAGE'
    PUBLISHING_AND_PRINTING = 'PUBLISHING_AND_PRINTING'
    PUBLISHING_SERVICES = 'PUBLISHING_SERVICES'
    RADAR_DECTORS = 'RADAR_DECTORS'
    RADIO_TELEVISION_AND_STEREO_REPAIR = 'RADIO_TELEVISION_AND_STEREO_REPAIR'
    REAL_ESTATE = 'REAL_ESTATE'
    REAL_ESTATE_AGENT = 'REAL_ESTATE_AGENT'
    REAL_ESTATE_AGENTS_AND_MANAGERS_RENTALS = 'REAL_ESTATE_AGENTS_AND_MANAGERS_RENTALS'
    RELIGION_AND_SPIRITUALITY_FOR_PROFIT = 'RELIGION_AND_SPIRITUALITY_FOR_PROFIT'
    RELIGIOUS = 'RELIGIOUS'
    RELIGIOUS_ORGANIZATIONS = 'RELIGIOUS_ORGANIZATIONS'
    REMITTANCE = 'REMITTANCE'
    RENTAL_PROPERTY_MANAGEMENT = 'RENTAL_PROPERTY_MANAGEMENT'
    RESIDENTIAL = 'RESIDENTIAL'
    RETAIL = 'RETAIL'
    RETAIL_FINE_JEWELRY_AND_WATCHES = 'RETAIL_FINE_JEWELRY_AND_WATCHES'
    REUPHOLSTERY_AND_FURNITURE_REPAIR = 'REUPHOLSTERY_AND_FURNITURE_REPAIR'
    RINGS = 'RINGS'
    ROOFING_SIDING_SHEET_METAL = 'ROOFING_SIDING_SHEET_METAL'
    RUGS_AND_CARPETS = 'RUGS_AND_CARPETS'
    SCHOOLS_AND_COLLEGES = 'SCHOOLS_AND_COLLEGES'
    SCIENCE_FICTION = 'SCIENCE_FICTION'
    SCRAPBOOKING = 'SCRAPBOOKING'
    SCULPTURES = 'SCULPTURES'
    SECURITIES_BROKERS_AND_DEALERS = 'SECURITIES_BROKERS_AND_DEALERS'
    SECURITY_AND_SURVEILLANCE = 'SECURITY_AND_SURVEILLANCE'
    SECURITY_AND_SURVEILLANCE_EQUIPMENT = 'SECURITY_AND_SURVEILLANCE_EQUIPMENT'
    SECURITY_BROKERS_AND_DEALERS = 'SECURITY_BROKERS_AND_DEALERS'
    SEMINARS = 'SEMINARS'
    SERVICE_STATIONS = 'SERVICE_STATIONS'
    SERVICES = 'SERVICES'
    SEWING_NEEDLEWORK_FABRIC_AND_PIECE_GOODS_STORES = 'SEWING_NEEDLEWORK_FABRIC_AND_PIECE_GOODS_STORES'
    SHIPPING_AND_PACKING = 'SHIPPING_AND_PACKING'
    SHOE_REPAIR_HAT_CLEANING = 'SHOE_REPAIR_HAT_CLEANING'
    SHOE_STORES = 'SHOE_STORES'
    SHOES = 'SHOES'
    SNOWMOBILE_DEALERS = 'SNOWMOBILE_DEALERS'
    SOFTWARE = 'SOFTWARE'
    SPECIALTY_AND_MISC_FOOD_STORES = 'SPECIALTY_AND_MISC._FOOD_STORES'
    SPECIALTY_CLEANING_POLISHING_AND_SANITATION_PREPARATIONS = 'SPECIALTY_CLEANING_POLISHING_AND_SANITATION_PREPARATIONS'
    SPECIALTY_OR_RARE_PETS = 'SPECIALTY_OR_RARE_PETS'
    SPORT_GAMES_AND_TOYS = 'SPORT_GAMES_AND_TOYS'
    SPORTING_AND_RECREATIONAL_CAMPS = 'SPORTING_AND_RECREATIONAL_CAMPS'
    SPORTING_GOODS = 'SPORTING_GOODS'
    SPORTS_AND_OUTDOORS = 'SPORTS_AND_OUTDOORS'
    SPORTS_AND_RECREATION = 'SPORTS_AND_RECREATION'
    STAMP_AND_COIN = 'STAMP_AND_COIN'
    STATIONARY_PRINTING_AND_WRITING_PAPER = 'STATIONARY_PRINTING_AND_WRITING_PAPER'
    STENOGRAPHIC_AND_SECRETARIAL_SUPPORT_SERVICES = 'STENOGRAPHIC_AND_SECRETARIAL_SUPPORT_SERVICES'
    STOCKS_BONDS_SECURITIES_AND_RELATED_CERTIFICATES = 'STOCKS_BONDS_SECURITIES_AND_RELATED_CERTIFICATES'
    STORED_VALUE_CARDS = 'STORED_VALUE_CARDS'
    SUPPLIES = 'SUPPLIES'
    SUPPLIES_AND_TOYS = 'SUPPLIES_AND_TOYS'
    SURVEILLANCE_EQUIPMENT = 'SURVEILLANCE_EQUIPMENT'
    SWIMMING_POOLS_AND_SPAS = 'SWIMMING_POOLS_AND_SPAS'
    SWIMMING_POOLS_SALES_SUPPLIES_SERVICES = 'SWIMMING_POOLS_SALES_SUPPLIES_SERVICES'
    TAILORS_AND_ALTERATIONS = 'TAILORS_AND_ALTERATIONS'
    TAX_PAYMENTS = 'TAX_PAYMENTS'
    TAX_PAYMENTS_GOVERNMENT_AGENCIES = 'TAX_PAYMENTS_GOVERNMENT_AGENCIES'
    TAXICABS_AND_LIMOUSINES = 'TAXICABS_AND_LIMOUSINES'
    TELECOMMUNICATION_SERVICES = 'TELECOMMUNICATION_SERVICES'
    TELEPHONE_CARDS = 'TELEPHONE_CARDS'
    TELEPHONE_EQUIPMENT = 'TELEPHONE_EQUIPMENT'
    TELEPHONE_SERVICES = 'TELEPHONE_SERVICES'
    THEATER = 'THEATER'
    TIRE_RETREADING_AND_REPAIR = 'TIRE_RETREADING_AND_REPAIR'
    TOLL_OR_BRIDGE_FEES = 'TOLL_OR_BRIDGE_FEES'
    TOOLS_AND_EQUIPMENT = 'TOOLS_AND_EQUIPMENT'
    TOURIST_ATTRACTIONS_AND_EXHIBITS = 'TOURIST_ATTRACTIONS_AND_EXHIBITS'
    TOWING_SERVICE = 'TOWING_SERVICE'
    TOYS_AND_GAMES = 'TOYS_AND_GAMES'
    TRADE_AND_VOCATIONAL_SCHOOLS = 'TRADE_AND_VOCATIONAL_SCHOOLS'
    TRADEMARK_INFRINGEMENT = 'TRADEMARK_INFRINGEMENT'
    TRAILER_PARKS_AND_CAMPGROUNDS = 'TRAILER_PARKS_AND_CAMPGROUNDS'
    TRAINING_SERVICES = 'TRAINING_SERVICES'
    TRANSPORTATION_SERVICES = 'TRANSPORTATION_SERVICES'
    TRAVEL = 'TRAVEL'
    TRUCK_AND_UTILITY_TRAILER_RENTALS = 'TRUCK_AND_UTILITY_TRAILER_RENTALS'
    TRUCK_STOP = 'TRUCK_STOP'
    TYPESETTING_PLATE_MAKING_AND_RELATED_SERVICES = 'TYPESETTING_PLATE_MAKING_AND_RELATED_SERVICES'
    USED_MERCHANDISE_AND_SECONDHAND_STORES = 'USED_MERCHANDISE_AND_SECONDHAND_STORES'
    USED_PARTS_MOTOR_VEHICLE = 'USED_PARTS_MOTOR_VEHICLE'
    UTILITIES = 'UTILITIES'
    UTILITIES_ELECTRIC_GAS_WATER_SANITARY = 'UTILITIES_ELECTRIC_GAS_WATER_SANITARY'
    VARIETY_STORES = 'VARIETY_STORES'
    VEHICLE_SALES = 'VEHICLE_SALES'
    VEHICLE_SERVICE_AND_ACCESSORIES = 'VEHICLE_SERVICE_AND_ACCESSORIES'
    VIDEO_EQUIPMENT = 'VIDEO_EQUIPMENT'
    VIDEO_GAME_ARCADES_ESTABLISH = 'VIDEO_GAME_ARCADES_ESTABLISH'
    VIDEO_GAMES_AND_SYSTEMS = 'VIDEO_GAMES_AND_SYSTEMS'
    VIDEO_TAPE_RENTAL_STORES = 'VIDEO_TAPE_RENTAL_STORES'
    VINTAGE_AND_COLLECTIBLE_VEHICLES = 'VINTAGE_AND_COLLECTIBLE_VEHICLES'
    VINTAGE_AND_COLLECTIBLES = 'VINTAGE_AND_COLLECTIBLES'
    VITAMINS_AND_SUPPLEMENTS = 'VITAMINS_AND_SUPPLEMENTS'
    VOCATIONAL_AND_TRADE_SCHOOLS = 'VOCATIONAL_AND_TRADE_SCHOOLS'
    WATCH_CLOCK_AND_JEWELRY_REPAIR = 'WATCH_CLOCK_AND_JEWELRY_REPAIR'
    WEB_HOSTING_AND_DESIGN = 'WEB_HOSTING_AND_DESIGN'
    WELDING_REPAIR = 'WELDING_REPAIR'
    WHOLESALE_CLUBS = 'WHOLESALE_CLUBS'
    WHOLESALE_FLORIST_SUPPLIERS = 'WHOLESALE_FLORIST_SUPPLIERS'
    WHOLESALE_PRESCRIPTION_DRUGS = 'WHOLESALE_PRESCRIPTION_DRUGS'
    WILDLIFE_PRODUCTS = 'WILDLIFE_PRODUCTS'
    WIRE_TRANSFER = 'WIRE_TRANSFER'
    WIRE_TRANSFER_AND_MONEY_ORDER = 'WIRE_TRANSFER_AND_MONEY_ORDER'
    WOMEN_ACCESSORY_SPECIALITY = 'WOMEN_ACCESSORY_SPECIALITY'
    WOMEN_CLOTHING = 'WOMEN_CLOTHING'

class ShipmentStatus(str, Enum):
    CANCELLED = 'CANCELLED'
    DELIVERED = 'DELIVERED'
    LOCAL_PICKUP = 'LOCAL_PICKUP'
    ON_HOLD = 'ON_HOLD'
    SHIPPED = 'SHIPPED'
    SHIPMENT_CREATED = 'SHIPMENT_CREATED'
    DROPPED_OFF = 'DROPPED_OFF'
    IN_TRANSIT = 'IN_TRANSIT'
    RETURNED = 'RETURNED'
    LABEL_PRINTED = 'LABEL_PRINTED'
    ERROR = 'ERROR'
    UNCONFIRMED = 'UNCONFIRMED'
    PICKUP_FAILED = 'PICKUP_FAILED'
    DELIVERY_DELAYED = 'DELIVERY_DELAYED'
    DELIVERY_SCHEDULED = 'DELIVERY_SCHEDULED'
    DELIVERY_FAILED = 'DELIVERY_FAILED'
    INRETURN = 'INRETURN'
    IN_PROCESS = 'IN_PROCESS'
    NEW = 'NEW'
    VOID = 'VOID'
    PROCESSED = 'PROCESSED'
    NOT_SHIPPED = 'NOT_SHIPPED'

class Carrier(str, Enum):
    ACOMMERCE = 'ACOMMERCE'
    PHL_2GO = 'PHL_2GO'
    AU_DHL_EXPRESS = 'AU_DHL_EXPRESS'
    BEL_DHL = 'BEL_DHL'
    DE_DHL_DEUTSHCE_POST_INTL_SHIPMENTS = 'DE_DHL_DEUTSHCE_POST_INTL_SHIPMENTS'
    IE_AN_POST_REGISTERED = 'IE_AN_POST_REGISTERED'
    AU_AU_POST = 'AU_AU_POST'
    SPEEDEXCOURIER = 'SPEEDEXCOURIER'
    UK_ROYALMAIL_SPECIAL = 'UK_ROYALMAIL_SPECIAL'
    FR_COLIS = 'FR_COLIS'
    VNPOST_EMS = 'VNPOST_EMS'
    NL_FEDEX = 'NL_FEDEX'
    CN_EMS = 'CN_EMS'
    IT_POSTE_ITALIANE = 'IT_POSTE_ITALIANE'
    HK_DHL_ECOMMERCE = 'HK_DHL_ECOMMERCE'
    ARAMEX = 'ARAMEX'
    AU_OTHER = 'AU_OTHER'
    TW_CHUNGHWA_POST = 'TW_CHUNGHWA_POST'
    DPEX = 'DPEX'
    POST_SERBIA = 'POST_SERBIA'
    PL_POCZTEX = 'PL_POCZTEX'
    CNEXPS = 'CNEXPS'
    DIRECTLOG = 'DIRECTLOG'
    ES_CORREOS_DE_ESPANA = 'ES_CORREOS_DE_ESPANA'
    BE_KIALA = 'BE_KIALA'
    ALPHAFAST = 'ALPHAFAST'
    UKR_POSHTA = 'UKR_POSHTA'
    CN_FEDEX = 'CN_FEDEX'
    BUYLOGIC = 'BUYLOGIC'
    IT_DHL_ECOMMERCE = 'IT_DHL_ECOMMERCE'
    NINJAVAN_MY = 'NINJAVAN_MY'
    JPN_YAMATO = 'JPN_YAMATO'
    POSTNORD_LOGISTICS = 'POSTNORD_LOGISTICS'
    US_DHL_GLOBALFORWARDING = 'US_DHL_GLOBALFORWARDING'
    IT_SGT = 'IT_SGT'
    NINJAVAN_PHILIPPINES = 'NINJAVAN_PHILIPPINES'
    EKART = 'EKART'
    IDN_WAHANA = 'IDN_WAHANA'
    FR_GLS = 'FR_GLS'
    IDN_POS_INT = 'IDN_POS_INT'
    DE_HERMES = 'DE_HERMES'
    PRT_CHRONOPOST = 'PRT_CHRONOPOST'
    MYS_MYS_POST = 'MYS_MYS_POST'
    WEBINTERPRET = 'WEBINTERPRET'
    BG_BULGARIAN_POST = 'BG_BULGARIAN_POST'
    NL_TPG = 'NL_TPG'
    CA_CANPAR = 'CA_CANPAR'
    MYS_AIRPAK = 'MYS_AIRPAK'
    MEX_SENDA = 'MEX_SENDA'
    LANDMARK_GLOBAL = 'LANDMARK_GLOBAL'
    UK_NIGHTLINE = 'UK_NIGHTLINE'
    JP_UPS = 'JP_UPS'
    UK_DHL = 'UK_DHL'
    SG_SG_POST = 'SG_SG_POST'
    PHL_AIRSPEED = 'PHL_AIRSPEED'
    DHL = 'DHL'
    KR_KOREA_POST = 'KR_KOREA_POST'
    JP_KURO_NEKO_YAMATO_UNYUU = 'JP_KURO_NEKO_YAMATO_UNYUU'
    IE_AN_POST_SWIFTPOST = 'IE_AN_POST_SWIFTPOST'
    CUCKOOEXPRESS = 'CUCKOOEXPRESS'
    FR_OTHER = 'FR_OTHER'
    FASTRAK_TH = 'FASTRAK_TH'
    AU_DHL_ECOMMERCE = 'AU_DHL_ECOMMERCE'
    DE_UPS = 'DE_UPS'
    ESHOPWORLD = 'ESHOPWORLD'
    INTERNATIONAL_BRIDGE = 'INTERNATIONAL_BRIDGE'
    FR_COLIPOSTE = 'FR_COLIPOSTE'
    AU_AUSTRIAN_POST = 'AU_AUSTRIAN_POST'
    IND_DELHIVERY = 'IND_DELHIVERY'
    DE_TNT = 'DE_TNT'
    GLOBAL_DHL = 'GLOBAL_DHL'
    US_DHL_PARCEL = 'US_DHL_PARCEL'
    NL_UPS = 'NL_UPS'
    GB_APC = 'GB_APC'
    IDN_TIKI = 'IDN_TIKI'
    HERMES = 'HERMES'
    ESP_NACEX = 'ESP_NACEX'
    NL_TNT = 'NL_TNT'
    DE_FEDEX = 'DE_FEDEX'
    OTHER = 'OTHER'
    BONDSCOURIERS = 'BONDSCOURIERS'
    IT_DHL_GLOBALFORWARDING = 'IT_DHL_GLOBALFORWARDING'
    IDN_LION_PARCEL = 'IDN_LION_PARCEL'
    UK_YODEL = 'UK_YODEL'
    IT_DHL_EXPRESS = 'IT_DHL_EXPRESS'
    PL_DHL_GLOBALFORWARDING = 'PL_DHL_GLOBALFORWARDING'
    DPD_POLAND = 'DPD_POLAND'
    AU_AUSTRALIA_POST_EXPRESS_POST_PLATINUM = 'AU_AUSTRALIA_POST_EXPRESS_POST_PLATINUM'
    ES_TNT = 'ES_TNT'
    CN_DHL_EXPRESS = 'CN_DHL_EXPRESS'
    DE_DPD = 'DE_DPD'
    DE_DPD_DELISTRACK = 'DE_DPD_DELISTRACK'
    CN_DHL_ECOMMERCE = 'CN_DHL_ECOMMERCE'
    JP_TNT = 'JP_TNT'
    PRT_CTT = 'PRT_CTT'
    UK_INTERLINK_EXPRESS = 'UK_INTERLINK_EXPRESS'
    NLD_POSTNL = 'NLD_POSTNL'
    CA_DHL_ECOMMERCE = 'CA_DHL_ECOMMERCE'
    SWIFTAIR = 'SWIFTAIR'
    NOR_POSTEN = 'NOR_POSTEN'
    MEX_REDPACK = 'MEX_REDPACK'
    PL_MASTERLINK = 'PL_MASTERLINK'
    PL_TNT = 'PL_TNT'
    NIM_EXPRESS = 'NIM_EXPRESS'
    PL_UPS = 'PL_UPS'
    UKR_NOVA = 'UKR_NOVA'
    QUANTIUM = 'QUANTIUM'
    SENDLE = 'SENDLE'
    SG_PARCELPOST = 'SG_PARCELPOST'
    SG_NINJAVAN = 'SG_NINJAVAN'
    BQC_EXPRESS = 'BQC_EXPRESS'
    RPD2MAN = 'RPD2MAN'
    THA_KERRY = 'THA_KERRY'
    MEX_AEROFLASH = 'MEX_AEROFLASH'
    SPREADEL = 'SPREADEL'
    ESP_REDUR = 'ESP_REDUR'
    JP_JAPANPOST = 'JP_JAPANPOST'
    ARE_EMIRATES_POST = 'ARE_EMIRATES_POST'
    CN_CHINA_POST_EMS = 'CN_CHINA_POST_EMS'
    UK_DHL_GLOBALFORWARDING = 'UK_DHL_GLOBALFORWARDING'
    CN_SF_EXPRESS = 'CN_SF_EXPRESS'
    UK_FEDEX = 'UK_FEDEX'
    POL_POCZTA = 'POL_POCZTA'
    YANWEN = 'YANWEN'
    KOR_CJ = 'KOR_CJ'
    DE_DEUTSCHE_POST_DHL_WITHIN_EUROPE_TRACKNET = 'DE_DEUTSCHE_POST_DHL_WITHIN_EUROPE_TRACKNET'
    IND_XPRESSBEES = 'IND_XPRESSBEES'
    UK_TNT = 'UK_TNT'
    CJ_KOREA_THAI = 'CJ_KOREA_THAI'
    CN_OTHER = 'CN_OTHER'
    IDN_POS = 'IDN_POS'
    ABC_MAIL = 'ABC_MAIL'
    UK_UPS = 'UK_UPS'
    CHINA_POST = 'CHINA_POST'
    PL_DHL_EXPRESS = 'PL_DHL_EXPRESS'
    ESP_SPANISH_SEUR = 'ESP_SPANISH_SEUR'
    SG_ZALORA = 'SG_ZALORA'
    MATKAHUOLTO = 'MATKAHUOLTO'
    FR_LAPOSTE = 'FR_LAPOSTE'
    KANGAROO_MY = 'KANGAROO_MY'
    ESP_CORREOS = 'ESP_CORREOS'
    NL_KIALA = 'NL_KIALA'
    IND_BLUEDART = 'IND_BLUEDART'
    TUR_PTT = 'TUR_PTT'
    CA_CANNOT_PROVIDE_TRACKING = 'CA_CANNOT_PROVIDE_TRACKING'
    JPN_SAGAWA = 'JPN_SAGAWA'
    MYS_SKYNET = 'MYS_SKYNET'
    IT_FERCAM = 'IT_FERCAM'
    UK_AIRBORNE_EXPRESS = 'UK_AIRBORNE_EXPRESS'
    CA_OTHER = 'CA_OTHER'
    DE_DEUTSHCE_POST_DHL_TRACK_TRACE_EXPRESS = 'DE_DEUTSHCE_POST_DHL_TRACK_TRACE_EXPRESS'
    CORREOS_DE_MEXICO = 'CORREOS_DE_MEXICO'
    FR_DHL_GLOBALFORWARDING = 'FR_DHL_GLOBALFORWARDING'
    GLOBAL_SKYNET = 'GLOBAL_SKYNET'
    AU_DHL_GLOBALFORWARDING = 'AU_DHL_GLOBALFORWARDING'
    DE_DHL_GLOBALFORWARDING = 'DE_DHL_GLOBALFORWARDING'
    SFC_LOGISTICS = 'SFC_LOGISTICS'
    US_GLOBEGISTICS = 'US_GLOBEGISTICS'
    CA_DHL_GLOBALFORWARDING = 'CA_DHL_GLOBALFORWARDING'
    OMNIPARCEL = 'OMNIPARCEL'
    PHL_AIR21 = 'PHL_AIR21'
    CBL_LOGISTICA = 'CBL_LOGISTICA'
    FR_MONDIAL = 'FR_MONDIAL'
    DE_DHL_ECOMMERCE = 'DE_DHL_ECOMMERCE'
    ADICIONAL = 'ADICIONAL'
    CH_SWISS_POST_PRIORITY = 'CH_SWISS_POST_PRIORITY'
    NL_INTANGIBLE_DIGITAL_SERVICES = 'NL_INTANGIBLE_DIGITAL_SERVICES'
    DE_ASENDIA = 'DE_ASENDIA'
    NL_ABC_MAIL = 'NL_ABC_MAIL'
    UK_DELTEC = 'UK_DELTEC'
    ONE_WORLD = 'ONE_WORLD'
    AIRBORNE_EXPRESS = 'AIRBORNE_EXPRESS'
    ES_OTHER = 'ES_OTHER'
    US_DHL_ECOMMERCE = 'US_DHL_ECOMMERCE'
    US_ENSENDA = 'US_ENSENDA'
    CPACKET = 'CPACKET'
    AXL = 'AXL'
    IND_REDEXPRESS = 'IND_REDEXPRESS'
    NL_LOCAL_PICKUP = 'NL_LOCAL_PICKUP'
    UK_ROYALMAIL_AIRSURE = 'UK_ROYALMAIL_AIRSURE'
    FR_TNT = 'FR_TNT'
    USPS = 'USPS'
    RINCOS = 'RINCOS'
    B2CEUROPE = 'B2CEUROPE'
    PHL_LBC = 'PHL_LBC'
    SG_TAQBIN = 'SG_TAQBIN'
    GR_ELTA = 'GR_ELTA'
    WINIT = 'WINIT'
    NLD_DHL = 'NLD_DHL'
    FR_GEODIS = 'FR_GEODIS'
    DE_DHL_PACKET = 'DE_DHL_PACKET'
    ARG_OCA = 'ARG_OCA'
    JP_DHL = 'JP_DHL'
    RUSSIAN_POST = 'RUSSIAN_POST'
    TW_TAIWAN_POST = 'TW_TAIWAN_POST'
    UPS = 'UPS'
    BE_BPOST = 'BE_BPOST'
    JP_SAGAWA_KYUU_BIN = 'JP_SAGAWA_KYUU_BIN'
    NATIONWIDE_MY = 'NATIONWIDE_MY'
    TNT = 'TNT'
    COURIERS_PLEASE = 'COURIERS_PLEASE'
    DMM_NETWORK = 'DMM_NETWORK'
    TOLL = 'TOLL'
    NONE = 'NONE'
    IDN_FIRST_LOGISTICS = 'IDN_FIRST_LOGISTICS'
    BH_POSTA = 'BH_POSTA'
    SENDIT = 'SENDIT'
    US_DHL_EXPRESS = 'US_DHL_EXPRESS'
    FEDEX = 'FEDEX'
    SWE_POSTNORD = 'SWE_POSTNORD'
    PHL_XEND_EXPRESS = 'PHL_XEND_EXPRESS'
    POSTI = 'POSTI'
    CA_CANADA_POST = 'CA_CANADA_POST'
    PL_FEXEX = 'PL_FEXEX'
    CN_EC = 'CN_EC'
    HK_TAQBIN = 'HK_TAQBIN'
    UK_AN_POST = 'UK_AN_POST'
    WISELOADS = 'WISELOADS'
    PRT_SEUR = 'PRT_SEUR'
    US_ONTRAC = 'US_ONTRAC'
    THA_THAILAND_POST = 'THA_THAILAND_POST'
    DPE_EXPRESS = 'DPE_EXPRESS'
    UK_DHL_EXPRESS = 'UK_DHL_EXPRESS'
    NL_DHL = 'NL_DHL'
    HK_FLYT_EXPRESS = 'HK_FLYT_EXPRESS'
    UK_HERMESWORLD = 'UK_HERMESWORLD'
    IT_REGISTER_MAIL = 'IT_REGISTER_MAIL'
    ARG_CORREO = 'ARG_CORREO'
    CA_LOOMIS = 'CA_LOOMIS'
    DTDC_AU = 'DTDC_AU'
    DPD = 'DPD'
    ASENDIA_HK = 'ASENDIA_HK'
    UK_ROYALMAIL_RECORDED = 'UK_ROYALMAIL_RECORDED'
    PL_POCZTA_POLSKA = 'PL_POCZTA_POLSKA'
    EU_IMX = 'EU_IMX'
    IDN_PANDU = 'IDN_PANDU'
    MEX_ESTAFETA = 'MEX_ESTAFETA'
    SREKOREA = 'SREKOREA'
    CYP_CYPRUS_POST = 'CYP_CYPRUS_POST'
    NZ_COURIER_POST = 'NZ_COURIER_POST'
    CN_EMPS = 'CN_EMPS'
    AU_TNT = 'AU_TNT'
    UK_CANNOT_PROVIDE_TRACKING = 'UK_CANNOT_PROVIDE_TRACKING'
    ES_DHL = 'ES_DHL'
    CONTINENTAL = 'CONTINENTAL'
    IND_DTDC = 'IND_DTDC'
    DE_GLS = 'DE_GLS'
    NLD_GLS = 'NLD_GLS'
    UK_DPD = 'UK_DPD'
    IT_TNT = 'IT_TNT'
    PL_DHL = 'PL_DHL'
    JP_NITTSU_PELICAN_BIN = 'JP_NITTSU_PELICAN_BIN'
    THA_DYNAMIC_LOGISTICS = 'THA_DYNAMIC_LOGISTICS'
    IT_POSTE_ITALIA = 'IT_POSTE_ITALIA'
    UK_ROYALMAIL_INTER_SIGNED = 'UK_ROYALMAIL_INTER_SIGNED'
    HERMES_IT = 'HERMES_IT'
    FR_BERT = 'FR_BERT'
    IND_PROFESSIONAL_COURIERS = 'IND_PROFESSIONAL_COURIERS'
    POL_SIODEMKA = 'POL_SIODEMKA'
    IE_AN_POST_SDS_PRIORITY = 'IE_AN_POST_SDS_PRIORITY'
    ADSONE = 'ADSONE'
    BRA_CORREIOS = 'BRA_CORREIOS'
    UBI_LOGISTICS = 'UBI_LOGISTICS'
    ES_CORREOS = 'ES_CORREOS'
    NGA_NIPOST = 'NGA_NIPOST'
    AUT_AUSTRIAN_POST = 'AUT_AUSTRIAN_POST'
    AU_FASTWAY = 'AU_FASTWAY'
    AUS_TOLL = 'AUS_TOLL'
    CA_CANPAR_COURIER = 'CA_CANPAR_COURIER'
    SWE_DIRECTLINK = 'SWE_DIRECTLINK'
    CZE_CESKA = 'CZE_CESKA'
    ROYAL_MAIL = 'ROYAL_MAIL'
    SG_SINGPOST = 'SG_SINGPOST'
    IT_OTHER = 'IT_OTHER'
    ZA_FASTWAY = 'ZA_FASTWAY'
    SEKOLOGISTICS = 'SEKOLOGISTICS'
    CN_UPS = 'CN_UPS'
    HUNTER_EXPRESS = 'HUNTER_EXPRESS'
    DE_DHL_PARCEL = 'DE_DHL_PARCEL'
    NLD_TRANSMISSION = 'NLD_TRANSMISSION'
    CN_TNT = 'CN_TNT'
    DE_DEUTSCHE = 'DE_DEUTSCHE'
    AIRSURE = 'AIRSURE'
    UK_PARCELFORCE = 'UK_PARCELFORCE'
    SWE_DB = 'SWE_DB'
    CN_CHINA_POST = 'CN_CHINA_POST'
    PL_GLS = 'PL_GLS'
    EU_BPOST = 'EU_BPOST'
    RELAIS_COLIS = 'RELAIS_COLIS'
    UK_DHL_PARCEL = 'UK_DHL_PARCEL'
    AUS_STARTRACK = 'AUS_STARTRACK'
    AU_TOLL_IPEC = 'AU_TOLL_IPEC'
    CORREOS_CHILE = 'CORREOS_CHILE'
    CH_SWISS_POST_EXPRES = 'CH_SWISS_POST_EXPRES'
    MYS_TAQBIN = 'MYS_TAQBIN'
    JET_SHIP = 'JET_SHIP'
    HK_DHL_EXPRESS = 'HK_DHL_EXPRESS'
    IT_SDA = 'IT_SDA'
    DE_DHL_DEUTSCHEPOST = 'DE_DHL_DEUTSCHEPOST'
    HK_DHL_GLOBALFORWARDING = 'HK_DHL_GLOBALFORWARDING'
    PHL_RAF = 'PHL_RAF'
    IT_GLS = 'IT_GLS'
    PANTOS = 'PANTOS'
    KOR_ECARGO = 'KOR_ECARGO'
    AT_AUSTRIAN_POST_EMS = 'AT_AUSTRIAN_POST_EMS'
    IT_BRT = 'IT_BRT'
    CHE_SWISS_POST = 'CHE_SWISS_POST'
    FASTWAY_NZ = 'FASTWAY_NZ'
    IT_EBOOST_SDA = 'IT_EBOOST_SDA'
    ASENDIA_UK = 'ASENDIA_UK'
    RRDONNELLEY = 'RRDONNELLEY'
    US_RL = 'US_RL'
    GR_GENIKI = 'GR_GENIKI'
    DE_DHL_EXPRESS = 'DE_DHL_EXPRESS'
    CA_GREYHOUND = 'CA_GREYHOUND'
    UK_COLLECTPLUS = 'UK_COLLECTPLUS'
    NINJAVAN_THAI = 'NINJAVAN_THAI'
    RABEN_GROUP = 'RABEN_GROUP'
    CA_DHL_EXPRESS = 'CA_DHL_EXPRESS'
    GLOBAL_TNT = 'GLOBAL_TNT'
    IN_INDIAPOST = 'IN_INDIAPOST'
    ITIS = 'ITIS'
    PHL_JAMEXPRESS = 'PHL_JAMEXPRESS'
    PRT_INT_SEUR = 'PRT_INT_SEUR'
    ESP_ASM = 'ESP_ASM'
    NINJAVAN_ID = 'NINJAVAN_ID'
    JP_FEDEX = 'JP_FEDEX'
    FR_CHRONOPOST = 'FR_CHRONOPOST'
    FR_SUIVI = 'FR_SUIVI'
    FR_TELIWAY = 'FR_TELIWAY'
    JPN_JAPAN_POST = 'JPN_JAPAN_POST'
    HRV_HRVATSKA = 'HRV_HRVATSKA'
    AT_AUSTRIAN_POST_PAKET_PRIME = 'AT_AUSTRIAN_POST_PAKET_PRIME'
    DE_OTHER = 'DE_OTHER'
    HK_HONGKONG_POST = 'HK_HONGKONG_POST'
    GRC_ACS = 'GRC_ACS'
    HUN_MAGYAR = 'HUN_MAGYAR'
    FR_DHL_PARCEL = 'FR_DHL_PARCEL'
    UK_OTHER = 'UK_OTHER'
    LWE_HK = 'LWE_HK'
    EFS = 'EFS'
    PL_DHL_PARCEL = 'PL_DHL_PARCEL'
    PARCELFORCE = 'PARCELFORCE'
    AU_AUSTRALIA_POST_EMS = 'AU_AUSTRALIA_POST_EMS'
    US_ASCENDIA = 'US_ASCENDIA'
    ROU_POSTA = 'ROU_POSTA'
    NZ_NZ_POST = 'NZ_NZ_POST'
    RPX = 'RPX'
    POSTUR_IS = 'POSTUR_IS'
    IE_AN_POST_SDS_EMS = 'IE_AN_POST_SDS_EMS'
    UK_UK_MAIL = 'UK_UK_MAIL'
    UK_FASTWAY = 'UK_FASTWAY'
    CORREOS_DE_COSTA_RICA = 'CORREOS_DE_COSTA_RICA'
    MYS_CITYLINK = 'MYS_CITYLINK'
    PUROLATOR = 'PUROLATOR'
    IND_DOTZOT = 'IND_DOTZOT'
    NG_COURIERPLUS = 'NG_COURIERPLUS'
    HK_FOUR_PX_EXPRESS = 'HK_FOUR_PX_EXPRESS'
    ROCKETPARCEL = 'ROCKETPARCEL'
    CN_DHL_GLOBALFORWARDING = 'CN_DHL_GLOBALFORWARDING'
    EPARCEL_KR = 'EPARCEL_KR'
    INPOST_PACZKOMATY = 'INPOST_PACZKOMATY'
    KOR_KOREA_POST = 'KOR_KOREA_POST'
    CA_PUROLATOR = 'CA_PUROLATOR'
    APR_72 = 'APR_72'
    FR_DHL_EXPRESS = 'FR_DHL_EXPRESS'
    IDN_JNE = 'IDN_JNE'
    AU_AUSTRALIA_POST_EPARCEL = 'AU_AUSTRALIA_POST_EPARCEL'
    GLOBAL_ESTES = 'GLOBAL_ESTES'
    LTU_LIETUVOS = 'LTU_LIETUVOS'
    THECOURIERGUY = 'THECOURIERGUY'
    BE_CHRONOPOST = 'BE_CHRONOPOST'
    VNM_VIETNAM_POST = 'VNM_VIETNAM_POST'
    AU_STAR_TRACK_EXPRESS = 'AU_STAR_TRACK_EXPRESS'
    RAM = 'RAM'

class TrackingNumberType(str, Enum):
    CARRIER_PROVIDED = 'CARRIER_PROVIDED'
    E2E_PARTNER_PROVIDED = 'E2E_PARTNER_PROVIDED'