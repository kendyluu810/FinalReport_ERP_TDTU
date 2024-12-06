{
    "name": "Make To Stock Custom Process",
    "version": "1.0",
    "author": "Double H",
    "category": "Inventory",
    'depends': ['base', 'mrp', 'purchase', 'sale', 'stock', 'point_of_sale'],
    "license": "AGPL-3",
    "data":[
        "views/menu_item.xml",
        "views/product_view.xml",
        "views/bom_view.xml",
        "views/purchase_order_view.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}