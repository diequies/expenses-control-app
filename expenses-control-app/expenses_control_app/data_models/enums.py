from enum import Enum


class TransactionType(Enum):
    """ Whether the money gets in or out """
    DEBIT = {'name': 'debit', 'sign': -1}
    CREDIT = {'name': 'credit', 'sign': 1}


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

class Currency(Enum):
    """ The currency """
    EUROS = 'euros'
    POUNDS = 'pounds'


class AccountType(Enum):
    """ Bank account type """
    PERSONAL = 'personal'
    JOINT = 'joint'
    CREDIT = 'credit'


class CategoryLevelTwo(Enum):
    """ Level 2 transaction classification """
    FOOD_AND_DRINK = {
        'name': 'food and drink',
        'parent_category': 'leisure',
        'child_categories': [],
        'int_value': 0
    }
    EVENTS = {
        'name': 'events',
        'parent_category': 'leisure',
        'child_categories': [],
        'int_value': 1
    }
    SUBSCRIPTIONS = {
        'name': 'subscriptions',
        'parent_category': 'leisure',
        'child_categories': [],
        'int_value': 2
    }
    TRAVEL = {
        'name': 'travel',
        'parent_category': 'leisure',
        'child_categories': [],
        'int_value': 3
    }
    ACCESSORIES = {
        'name': 'accessories',
        'parent_category': 'purchases',
        'child_categories': [],
        'int_value': 0
    }
    PERSONAL_CARE = {
        'name': 'personal care',
        'parent_category': 'purchases',
        'child_categories': [],
        'int_value': 1
    }
    HOME = {
        'name': 'home',
        'parent_category': 'purchases',
        'child_categories': [],
        'int_value': 2
    }
    PERSONAL_LEISURE = {
        'name': 'personal leisure',
        'parent_category': 'purchases',
        'child_categories': [],
        'int_value': 3
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
        'child_categories': [CategoryLevelTwo.ACCESSORIES,
                             CategoryLevelTwo.PERSONAL_CARE, CategoryLevelTwo.HOME,
                             CategoryLevelTwo.PERSONAL_LEISURE],
        'int_value': 0
    }
    EXPENSES = {
        'name': 'expenses',
        'child_categories': [],
        'int_value': 0
    }
