from enum import Enum


class TransactionSign(Enum):
    """ Whether the money gets in or out """
    DEBIT = {'name': 'debit', 'sign': -1}
    CREDIT = {'name': 'credit', 'sign': 1}


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
        'lloyds': ['pay'],
        'nationwide': ['standing order'],
        'revolut': [],
        'monzo': ['SO']
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


class AccountUser(Enum):
    """ The owner of the account """
    DIEGO = 'diego'
    MARIA = 'maria'
    JOINT = 'joint'


class Bank(Enum):
    """ The bank of the transaction """
    LLOYDS = 'lloyds'
    NATIONWIDE = 'nationwide'
    REVOLUT = 'revolut'
    MONZO = 'monzo'
    OPENBANK = 'openbank'


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


class AccountType(Enum):
    """ Bank account type """
    DEBIT = 'debit'
    CREDIT = 'credit'


class CategoryLevelThree(Enum):
    """ Level 3 transaction classification """
    WATER = {
        'name': 'water',
        'parent_category': 'utilities',
        'int_value': 0
    }
    RENT = {
        'name': 'rent',
        'parent_category': 'utilities',
        'int_value': 1
    }
    COUNCIL_TAX = {
        'name': 'council tax',
        'parent_category': 'utilities',
        'int_value': 2
    }
    ENERGY = {
        'name': 'energy',
        'parent_category': 'utilities',
        'int_value': 3
    }
    INTERNET = {
        'name': 'internet',
        'parent_category': 'utilities',
        'int_value': 4
    }
    PHONE = {
        'name': 'phone',
        'parent_category': 'utilities',
        'int_value': 5
    }
    BANK_FEES = {
        'name': 'bank fees',
        'parent_category': 'personal expenses',
        'int_value': 0
    }
    GYM = {
        'name': 'gym',
        'parent_category': 'personal expenses',
        'int_value': 1
    }
    SUPERMARKET = {
        'name': 'supermarket',
        'parent_category': 'personal expenses',
        'int_value': 2
    }
    TRANSPORT = {
        'name': 'transport',
        'parent_category': 'personal expenses',
        'int_value': 3
    }
    RESTAURANT = {
        'name': 'restaurant',
        'parent_category': 'food and drink',
        'int_value': 0
    }
    PUB = {
        'name': 'pub',
        'parent_category': 'food and drink',
        'int_value': 1
    }
    CAFE = {
        'name': 'cafe',
        'parent_category': 'food and drink',
        'int_value': 2
    }
    CINEMA = {
        'name': 'cinema',
        'parent_category': 'events',
        'int_value': 0
    }
    MUSIC_EVENT = {
        'name': 'music event',
        'parent_category': 'events',
        'int_value': 1
    }
    SHOW = {
        'name': 'show',
        'parent_category': 'events',
        'int_value': 2
    }
    THEATRE = {
        'name': 'theatre',
        'parent_category': 'events',
        'int_value': 3
    }
    WEDDING = {
        'name': 'wedding',
        'parent_category': 'events',
        'int_value': 4
    }
    TV_SUBSCRIPTION = {
        'name': 'tv subscription',
        'parent_category': 'subscriptions',
        'int_value': 0
    }
    MUSIC_SUBSCRIPTION = {
        'name': 'music subscription',
        'parent_category': 'subscriptions',
        'int_value': 1
    }
    NEWS_SUBSCRIPTION = {
        'name': 'news subscription',
        'parent_category': 'subscriptions',
        'int_value': 2
    }
    HOSPITALITY = {
        'name': 'hospitality',
        'parent_category': 'travel',
        'int_value': 0
    }
    TRAIN = {
        'name': 'train',
        'parent_category': 'travel',
        'int_value': 1
    }
    PLANE = {
        'name': 'plane',
        'parent_category': 'travel',
        'int_value': 2
    }
    LOCAL_TRANSPORT = {
        'name': 'local transport',
        'parent_category': 'travel',
        'int_value': 3
    }
    FOOD = {
        'name': 'food',
        'parent_category': 'travel',
        'int_value': 4
    }
    ACTIVITIES = {
        'name': 'activities',
        'parent_category': 'travel',
        'int_value': 5
    }
    ACCESSORIES = {
        'name': 'accessories',
        'parent_category': 'personal care',
        'int_value': 0
    }
    BEAUTY = {
        'name': 'beauty',
        'parent_category': 'personal care',
        'int_value': 1
    }
    CLOTHES = {
        'name': 'clothes',
        'parent_category': 'personal care',
        'int_value': 2
    }
    BOOKS = {
        'name': 'books',
        'parent_category': 'personal care',
        'int_value': 3
    }
    FURNITURE = {
        'name': 'furniture',
        'parent_category': 'home',
        'int_value': 0
    }
    VARIOUS_HOME_STUFF = {
        'name': 'various home stuff',
        'parent_category': 'home',
        'int_value': 1
    }
    BALANCE = {
        'name': 'balance',
        'parent_category': 'balance',
        'int_value': 0
    }


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
