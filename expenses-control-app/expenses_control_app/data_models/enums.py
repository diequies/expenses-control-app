from enum import Enum


class TransactionSign(Enum):
    """ Whether the money gets in or out """
    DEBIT = {'name': 'debit', 'sign': -1}
    CREDIT = {'name': 'credit', 'sign': 1}

    @classmethod
    def get_transaction_sign_from_string(cls, string: str):
        for transaction_sign in TransactionSign:
            if transaction_sign.value.get('name').lower() == string.lower():
                return transaction_sign

        return TransactionSign.DEBIT


class TransactionType(Enum):
    """ The type of transaction """
    CONTACTLESS = {
        'name': 'contactless',
        'lloyds': [],
        'nationwide': ['contactless payment'],
        'revolut': [],
        'monzo': []
    }
    CARD_PAYMENT = {
        'name': 'card payment',
        'lloyds': ['deb'],
        'nationwide': ['visa purchase'],
        'revolut': ['card_payment'],
        'monzo': ['card payment']
    }
    BANK_TRANSFERENCE = {
        'name': 'bank transference',
        'lloyds': ['fpi', 'fpo'],
        'nationwide': ['bank credit', 'transfer', 'visa credit', 'payment'],
        'revolut': ['transfer'],
        'monzo': ['monzo-to-monzo']
    }
    DIRECT_DEBIT = {
        'name': 'direct debit',
        'lloyds': ['dd'],
        'nationwide': ['direct debit'],
        'revolut': [],
        'monzo': []
    }
    WITHDRAWAL = {
        'name': 'withdrawal',
        'lloyds': [],
        'nationwide': ['withdrawal'],
        'revolut': ['atm'],
        'monzo': []
    }
    STANDING_ORDER = {
        'name': 'standing order',
        'lloyds': ['pay', 'so'],
        'nationwide': ['standing order'],
        'revolut': [],
        'monzo': ['so']
    }
    TOP_UP = {
        'name': 'top up',
        'lloyds': [],
        'nationwide': [],
        'revolut': ['topup'],
        'monzo': ['faster payment']
    }
    CURRENCY_EXCHANGE = {
        'name': 'currency exchange',
        'lloyds': [],
        'nationwide': [],
        'revolut': ['exchange'],
        'monzo': []
    }
    OTHER = {
        'name': 'other',
        'lloyds': [],
        'nationwide': [],
        'revolut': [],
        'monzo': []
    }

    @classmethod
    def get_transaction_type_from_string(cls, string: str):
        for transaction_type in TransactionType:
            if transaction_type.value.get('name').lower() == string.lower():
                return transaction_type

        return TransactionType.OTHER


class AccountUser(Enum):
    """ The owner of the account """
    DIEGO = 'diego'
    MARIA = 'maria'
    JOINT = 'joint'

    @classmethod
    def get_account_user_from_string(cls, string: str):
        for account_user in AccountUser:
            if account_user.value.lower() == string.lower():
                return account_user

        return AccountUser.JOINT


class Bank(Enum):
    """ The bank of the transaction """
    LLOYDS = 'lloyds'
    NATIONWIDE = 'nationwide'
    REVOLUT = 'revolut'
    MONZO = 'monzo'
    OPENBANK = 'openbank'

    @classmethod
    def get_account_bank_string(cls, string: str):
        for bank_name in Bank:
            if bank_name.value.lower() == string.lower():
                return bank_name

        return Bank.NATIONWIDE


class Currency(Enum):
    """ The currency """
    EUROS = {
        'name': 'euros',
        'short_name': 'EUR',
        'symbol': '€'
    }
    POUNDS = {
        'name': 'pounds',
        'short_name': 'GBP',
        'symbol': '£'
    }
    HUNGARIAN_FLORIN = {
        'name': 'hungarian florin',
        'short_name': 'HUF',
        'symbol': 'Ft'
    }
    MEXICAN_PESO = {
        'name': 'mexican peso',
        'short_name': 'MXN',
        'symbol': '$'
    }
    POLISH_ZLOTY = {
        'name': 'polish zloty',
        'short_name': 'PLN',
        'symbol': 'zł'
    }
    AMERICAN_DOLLAR = {
        'name': 'american dollar',
        'short_name': 'USD',
        'symbol': '$'
    }

    @classmethod
    def get_currency_from_string(cls, string: str):
        for currency_name in Currency:
            if currency_name.value.get('name').lower() == string.lower():
                return currency_name

        return Currency.POUNDS


class AccountType(Enum):
    """ Bank account type """
    DEBIT = 'debit'
    CREDIT = 'credit'

    @classmethod
    def get_account_type_from_string(cls, string: str):
        for account_type in AccountType:
            if account_type.value.lower() == string.lower():
                return account_type

        return AccountType.DEBIT


class CategoryLevelThree(Enum):
    """ Level 3 transaction classification """
    WATER = {
        'name': 'water',
        'parent_category': 'utilities',
        'int_value': 0,
        'keywords': []
    }
    RENT = {
        'name': 'rent',
        'parent_category': 'utilities',
        'int_value': 1,
        'keywords': []
    }
    COUNCIL_TAX = {
        'name': 'council tax',
        'parent_category': 'utilities',
        'int_value': 2,
        'keywords': []
    }
    ENERGY = {
        'name': 'energy',
        'parent_category': 'utilities',
        'int_value': 3,
        'keywords': []
    }
    INTERNET = {
        'name': 'internet',
        'parent_category': 'utilities',
        'int_value': 4,
        'keywords': []
    }
    PHONE = {
        'name': 'phone',
        'parent_category': 'utilities',
        'int_value': 5,
        'keywords': ['giffgaff']
    }
    BANK_FEES = {
        'name': 'bank fees',
        'parent_category': 'personal expenses',
        'int_value': 0,
        'keywords': ['trans fee', 'club lloyds fee', 'club lloyds waived']
    }
    GYM = {
        'name': 'gym',
        'parent_category': 'personal expenses',
        'int_value': 1,
        'keywords': []
    }
    SUPERMARKET = {
        'name': 'supermarket',
        'parent_category': 'personal expenses',
        'int_value': 2,
        'keywords': ['sainsburys', 'co-op', 'tesco']
    }
    TRANSPORT = {
        'name': 'transport',
        'parent_category': 'personal expenses',
        'int_value': 3,
        'keywords': []
    }
    OTHER_EXPENSES = {
        'name': 'other expenses',
        'parent_category': 'personal expenses',
        'int_value': 4,
        'keywords': ['moonpig', 'fullertons']
    }
    OTHER_TAXES = {
        'name': 'other taxes',
        'parent_category': 'personal expenses',
        'int_value': 5,
        'keywords': ['hmrc']
    }
    RESTAURANT = {
        'name': 'restaurant',
        'parent_category': 'food and drink',
        'int_value': 0,
        'keywords': ['deliveroo', 'barrafina']
    }
    PUB = {
        'name': 'pub',
        'parent_category': 'food and drink',
        'int_value': 1,
        'keywords': []
    }
    CAFE = {
        'name': 'cafe',
        'parent_category': 'food and drink',
        'int_value': 2,
        'keywords': ['costa coffee', 'riccis']
    }
    CINEMA = {
        'name': 'cinema',
        'parent_category': 'events',
        'int_value': 0,
        'keywords': []
    }
    MUSIC_EVENT = {
        'name': 'music event',
        'parent_category': 'events',
        'int_value': 1,
        'keywords': []
    }
    SHOW = {
        'name': 'show',
        'parent_category': 'events',
        'int_value': 2,
        'keywords': []
    }
    THEATRE = {
        'name': 'theatre',
        'parent_category': 'events',
        'int_value': 3,
        'keywords': []
    }
    WEDDING = {
        'name': 'wedding',
        'parent_category': 'events',
        'int_value': 4,
        'keywords': []
    }
    TV_SUBSCRIPTION = {
        'name': 'tv subscription',
        'parent_category': 'subscriptions',
        'int_value': 0,
        'keywords': []
    }
    MUSIC_SUBSCRIPTION = {
        'name': 'music subscription',
        'parent_category': 'subscriptions',
        'int_value': 1,
        'keywords': []
    }
    NEWS_SUBSCRIPTION = {
        'name': 'news subscription',
        'parent_category': 'subscriptions',
        'int_value': 2,
        'keywords': []
    }
    HOSPITALITY = {
        'name': 'hospitality',
        'parent_category': 'travel',
        'int_value': 0,
        'keywords': []
    }
    TRAIN = {
        'name': 'train',
        'parent_category': 'travel',
        'int_value': 1,
        'keywords': []
    }
    PLANE = {
        'name': 'plane',
        'parent_category': 'travel',
        'int_value': 2,
        'keywords': ['easyjet', 'ryanair']
    }
    LOCAL_TRANSPORT = {
        'name': 'local transport',
        'parent_category': 'travel',
        'int_value': 3,
        'keywords': ['justpark', 'ringgo parking', 'dart-charge', 'arriva']
    }
    FOOD = {
        'name': 'food',
        'parent_category': 'travel',
        'int_value': 4,
        'keywords': []
    }
    ACTIVITIES = {
        'name': 'activities',
        'parent_category': 'travel',
        'int_value': 5,
        'keywords': []
    }
    ACCESSORIES = {
        'name': 'accessories',
        'parent_category': 'personal care',
        'int_value': 0,
        'keywords': []
    }
    BEAUTY = {
        'name': 'beauty',
        'parent_category': 'personal care',
        'int_value': 1,
        'keywords': []
    }
    CLOTHES = {
        'name': 'clothes',
        'parent_category': 'personal care',
        'int_value': 2,
        'keywords': ['decathlon']
    }
    BOOKS = {
        'name': 'books',
        'parent_category': 'personal care',
        'int_value': 3,
        'keywords': ['abebooks']
    }
    LEARNING = {
        'name': 'learning',
        'parent_category': 'personal care',
        'int_value': 4,
        'keywords': ['udemy']
    }
    FURNITURE = {
        'name': 'furniture',
        'parent_category': 'home',
        'int_value': 0,
        'keywords': []
    }
    VARIOUS_HOME_STUFF = {
        'name': 'various home stuff',
        'parent_category': 'home',
        'int_value': 1,
        'keywords': ['amznmktplace']
    }
    BALANCE = {
        'name': 'balance',
        'parent_category': 'balance',
        'int_value': 0,
        'keywords': ['diego revolut']
    }
    SALARY = {
        'name': 'salary',
        'parent_category': 'balance',
        'int_value': 1,
        'keywords': ['echobox']
    }

    @classmethod
    def get_category_three_from_string(cls, string: str):
        for category_three in CategoryLevelThree:
            if category_three.value.get('name').lower() == string.lower():
                return category_three

        return CategoryLevelThree.BALANCE


class CategoryLevelTwo(Enum):
    """ Level 2 transaction classification """
    FOOD_AND_DRINK = {
        'name': 'food and drink',
        'parent_category': 'leisure',
        'child_categories': [CategoryLevelThree.RESTAURANT, CategoryLevelThree.PUB,
                             CategoryLevelThree.CAFE],
        'int_value': 0
    }
    EVENTS = {
        'name': 'events',
        'parent_category': 'leisure',
        'child_categories': [CategoryLevelThree.MUSIC_EVENT, CategoryLevelThree.CINEMA,
                             CategoryLevelThree.SHOW, CategoryLevelThree.THEATRE],
        'int_value': 1
    }
    SUBSCRIPTIONS = {
        'name': 'subscriptions',
        'parent_category': 'leisure',
        'child_categories': [CategoryLevelThree.TV_SUBSCRIPTION,
                             CategoryLevelThree.MUSIC_SUBSCRIPTION,
                             CategoryLevelThree.NEWS_SUBSCRIPTION],
        'int_value': 2
    }
    TRAVEL = {
        'name': 'travel',
        'parent_category': 'leisure',
        'child_categories': [CategoryLevelThree.HOSPITALITY, CategoryLevelThree.TRAIN,
                             CategoryLevelThree.PLANE,
                             CategoryLevelThree.LOCAL_TRANSPORT,
                             CategoryLevelThree.FOOD, CategoryLevelThree.ACTIVITIES],
        'int_value': 3
    }
    PERSONAL_CARE = {
        'name': 'personal care',
        'parent_category': 'purchases',
        'child_categories': [CategoryLevelThree.BEAUTY, CategoryLevelThree.CLOTHES,
                             CategoryLevelThree.BOOKS, CategoryLevelThree.ACCESSORIES],
        'int_value': 0
    }
    HOME = {
        'name': 'home',
        'parent_category': 'purchases',
        'child_categories': [CategoryLevelThree.FURNITURE,
                             CategoryLevelThree.VARIOUS_HOME_STUFF],
        'int_value': 1
    }
    UTILITIES = {
        'name': 'utilities',
        'parent_category': 'expenses',
        'child_categories': [CategoryLevelThree.WATER, CategoryLevelThree.INTERNET,
                             CategoryLevelThree.COUNCIL_TAX, CategoryLevelThree.PHONE,
                             CategoryLevelThree.ENERGY, CategoryLevelThree.RENT],
        'int_value': 0
    }
    PERSONAL_EXPENSES = {
        'name': 'personal expenses',
        'parent_category': 'expenses',
        'child_categories': [CategoryLevelThree.BANK_FEES, CategoryLevelThree.TRANSPORT,
                             CategoryLevelThree.GYM, CategoryLevelThree.SUPERMARKET],
        'int_value': 1
    }
    BALANCE = {
        'name': 'balance',
        'parent_category': 'balance',
        'child_categories': [CategoryLevelThree.BALANCE],
        'int_value': 0
    }

    @classmethod
    def get_category_two_from_string(cls, string: str):
        for category_two in CategoryLevelTwo:
            if category_two.value.get('name').lower() == string.lower():
                return category_two

        return CategoryLevelTwo.BALANCE


class CategoryLevelOne(Enum):
    """ Level 1 transaction classification """
    LEISURE = {
        'name': 'leisure',
        'child_categories': [CategoryLevelTwo.FOOD_AND_DRINK, CategoryLevelTwo.EVENTS,
                             CategoryLevelTwo.SUBSCRIPTIONS, CategoryLevelTwo.TRAVEL],
        'int_value': 0
    }
    PURCHASES = {
        'name': 'purchases',
        'child_categories': [CategoryLevelTwo.PERSONAL_CARE, CategoryLevelTwo.HOME],
        'int_value': 1
    }
    EXPENSES = {
        'name': 'expenses',
        'child_categories': [CategoryLevelTwo.UTILITIES,
                             CategoryLevelTwo.PERSONAL_EXPENSES],
        'int_value': 2
    }
    BALANCE = {
        'name': 'balance',
        'child_categories': [CategoryLevelTwo.BALANCE],
        'int_value': 0
    }

    @classmethod
    def get_category_one_from_string(cls, string: str):
        for category_one in CategoryLevelOne:
            if category_one.value.get('name').lower() == string.lower():
                return category_one

        return CategoryLevelOne.BALANCE
