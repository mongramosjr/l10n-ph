# -*- encoding: utf-8 -*-
##############################################################################
#
#    Basement720, PH - Accounting
#    Copyright © 2016, Dominador B. Ramos Jr. <mongramosjr@gmail.com>
#    This file is part of PH - Accounting and is released under
#    the BSD 3-Clause License: https://opensource.org/licenses/BSD-3-Clause
#
##############################################################################

{
    'name': 'PH - Accounting',
    'version': '2016.03',
    'category': 'Localization',
    'description': """
This is the latest PH OpenERP localisation necessary to run OpenERP accounting for PH with:
=================================================================================================
    - a generic chart of accounts
    - BIR-ready tax structure
    - a few other adaptations""",
    'author': 'Mong Ramos Jr. <mongramosjr@gmail.com>',
    'website': 'https://www.basement720.com/',
    'depends': ['account'],
    'data': [
        'data/res_country_data.xml',
        'data/res.country.state.csv',
        
        'data/account_chart_template.xml',
        'data/account_account_template.xml',

        'data/set_account_on_chart_template.xml',

        'data/account_tax_template.xml',

        'data/account_chart_template.yml',
    ],
    'demo' : [],
    'installable': 'True',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
