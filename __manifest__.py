# -*- coding: utf-8 -*-
{
    'name': 'Campos Extrasv16',
    'version': '16.5',
    'author': 'Demsa Industrial',
    'website': '',
    'depends': ['base', 'purchase_requisition', 'account', 'stock'],
    'data': [
        # security
        # data
        # demo
        # reports
        # 'reports/report.xml',
        # 'reports/report_stock.xml',
        # groups
        "groups/compra_validar_botones.xml",
        "groups/inventario_validar_botones.xml",
        "groups/facturas_validar_botones.xml",
        "groups/boton_autorizar.xml",
        "groups/calidad_orden_Compra.xml",
        # views
        # 'views/purchase_order.xml',
        'views/stock_picking.xml',
        'views/stock_picking_type.xml',
        "views/purchase_requisition.xml",
        'views/account_move.xml',
        # 'views/hr_employee.xml',
        'views/sale_order.xml',
        'views/hr_expense.xml',
        'views/product_template.xml',


    ],
    'license': 'LGPL-3',
}
