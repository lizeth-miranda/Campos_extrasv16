# -*- coding: utf-8 -*-
{
    'name': 'Campos Extrasv16',
    'version': '16.1',
    'author': 'Demsa Industrial',
    'website': '',
    'depends': ['base', 'purchase_requisition', 'account', 'stock', 'account_multipayment_general'],
    'data': [
        # security
        # data
        'data/payment20.xml',
        # demo
        # reports
        'reports/reporte_resguardo.xml',
        'reports/resguardo.xml',
        'reports/reporte_free_resguardo.xml',
        'reports/free_resguardo.xml',
        # groups
        "groups/compra_validar_botones.xml",
        "groups/inventario_validar_botones.xml",
        "groups/facturas_validar_botones.xml",
        "groups/boton_autorizar.xml",
        "groups/calidad_orden_Compra.xml",
        "groups/usuarios_confirmar.xml",
        "groups/usuarios_validar.xml",
        "groups/boton_almacen.xml",
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
        'views/res_partner_view.xml',
        'wizards/multi_payments_general.xml',

    ],
    'license': 'LGPL-3',
}
