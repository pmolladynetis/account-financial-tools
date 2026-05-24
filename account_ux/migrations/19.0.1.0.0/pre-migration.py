def migrate(cr, version):
    # Remove obsolete view that references payment_method_description field
    # which no longer exists in Odoo 19
    cr.execute("""
        UPDATE ir_ui_view 
        SET arch_db = '{"en_US": "<data/>", "es_AR": "<data/>"}'::jsonb
        WHERE name IN ('account.payment.tree', 'account.payment.tree.personalization')
        AND arch_db::text LIKE '%payment_method_description%'
    """)

    # Remove views with settled_line_ids field that no longer exists in v19
    cr.execute("""
        UPDATE ir_ui_view 
        SET arch_db = '{"en_US": "<data/>", "es_AR": "<data/>"}'::jsonb
        WHERE arch_db::text LIKE '%settled_line_ids%'
    """)
