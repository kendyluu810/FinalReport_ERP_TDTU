{
    'name': 'CRM and SRM System',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Integration of CRM and SRM functionalities in Odoo',
    'author': 'Double H',
    'depends': ['base', 'crm', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'views/purchase_order_view.xml',
        'views/crm_srm_menu.xml',
    ],
    "auto_install": False,
    'installable': True,
    'application': True,
}
