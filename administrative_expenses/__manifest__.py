{
    'name': 'Administrative expenses',

    'summary': """
        This module add one line in subscription lines when payment is letter than
        due date""",

    'description': """
        Add new line in subscription line ids
    """,

    'version': '13.0.1.0',

    'author': "Nybble group",

    'contributors': ['Luis Felipe Paternina'],

    'website': "",

    'category': 'Sale',

    'depends': [

        'account_accountant',
        'sale_management',
        'sale_subscription',
        'contacts',

    ],

    'data': [
       
        'data/account.tax.csv',
        'data/product.template.csv',
        'views/account_move.xml',
                   
    ],
    'installable': True
}
