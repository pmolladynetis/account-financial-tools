def migrate(cr, version):
    """
    Update account.journal_comp_rule domain_force
    even if the rule is marked as noupdate.
    """
    cr.execute("""
        UPDATE ir_rule
        SET domain_force = '[
            "|\",
            (\"company_id\", \"in\", company_ids),
            \"&\",
            (\"company_id\", \"parent_of\", company_ids),
            (\"shared_to_branches\", \"=\", True)
        ]'
        WHERE id = (
            SELECT res_id FROM ir_model_data 
            WHERE module = 'account' AND name = 'journal_comp_rule'
        )
    """)
