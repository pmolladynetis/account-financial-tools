def migrate(cr, version):
    # Remove obsolete view that references payment_method_description field
    # which no longer exists in Odoo 19
    cr.execute("""
        UPDATE ir_ui_view 
        SET arch_db = '{"en_US": "<data/>", "es_AR": "<data/>"}'::jsonb
        WHERE name IN ('account.payment.tree', 'account.payment.tree.personalization')
        AND arch_db::text LIKE '%payment_method_description%'
    """)
