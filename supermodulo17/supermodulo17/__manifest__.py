# -*- coding: utf-8 -*-
{
    'name': "supermodulo17",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
    'account_asset_management',
'account_banking_mandate',
'account_banking_pain_base',
'account_banking_sepa_credit_transfer',
'account_banking_sepa_direct_debit',
'account_due_list',
'account_edi_ubl_cii',
'account_financial_report',
'account_invoice_line_report',
'account_invoice_refund_link',
'account_lock_date_update',
'account_move_name_sequence',
'account_move_template',
'account_payment_mode',
'account_payment_order',
'account_payment_partner',
'account_payment_purchase_stock',
'account_payment_purchase',
'account_payment_sale',
'account_payment_term',
'account_payment',
'account_qr_code_sepa',
'account_reconcile_model_oca',
'account_reconcile_oca',
'account_statement_base',
'account_statement_import_base',
'account_statement_import_file_reconcile_oca',
'account_statement_import_file',
'account_tax_balance',
'account_usability',
'account',
'analytic',
'auth_password_policy_portal',
'auth_password_policy_signup',
'auth_password_policy',
'auth_signup',
'auth_totp_mail',
'auth_totp_portal',
'auth_totp',
'barcodes_gs1_nomenclature',
'barcodes',
'base_address_extended',
'base_bank_from_iban',
'base_iban',
'base_import_module',
'base_import',
'base_install_request',
'base_location_geonames_import',
'base_location',
'base_partner_sequence',
'base_search_custom_field_filter',
'base_setup',
'base_sparse_field',
'base_technical_features',
'base_vat',
'base',
'board',
'bus',
'calendar_sms',
'calendar',
'contacts',
'contract',
'crm_iap_enrich',
'crm_iap_mine',
'crm_sms',
'crm',
'date_range_account',
'date_range',
'digest',
'document_knowledge',
'document_page',
'document_url',
'google_gmail',
'hr_attendance',
'hr_expense',
'hr_holidays_attendance',
'hr_holidays',
'hr_hourly_cost',
'hr_org_chart',
'hr_skills',
'hr_timesheet_attendance',
'hr_timesheet',
'hr',
'http_routing',
'iap_crm',
'iap_mail',
'iap',
'l10n_es_account_asset',
'l10n_es_account_banking_sepa_fsdd',
'l10n_es_account_statement_import_n43',
'l10n_es_aeat_mod111',
'l10n_es_aeat_mod115',
'l10n_es_aeat_mod303',
'l10n_es_aeat_mod347',
'l10n_es_aeat_mod349',
'l10n_es_aeat_mod390',
'l10n_es_aeat',
'l10n_es_atc',
'l10n_es_cnae',
'l10n_es_edi_facturae_adm_centers',
'l10n_es_edi_facturae_invoice_period',
'l10n_es_edi_facturae',
'l10n_es_mis_report',
'l10n_es_partner_mercantil',
'l10n_es_partner',
'l10n_es_toponyms',
'l10n_es_vat_book',
'l10n_es',
'l10n_eu_nace',
'link_tracker',
'login_user_detail',
'mail_bot_hr',
'mail_bot',
'mail',
'mass_mailing_crm',
'mass_mailing_sale',
'mass_mailing_themes',
'mass_mailing',
'mis_builder',
'mrp_account',
'mrp',
'onboarding',
'partner_industry_secondary',
'partner_manual_rank',
'payment',
'phone_validation',
'portal_rating',
'portal',
'privacy_lookup',
'product_margin',
'product',
'project_account',
'project_hr_expense',
'project_mrp',
'project_purchase',
'project_sale_expense',
'project_sms',
'project_timesheet_holidays',
'project_todo',
'project',
'purchase_mrp',
'purchase_stock',
'purchase',
'rating',
'report_xlsx_helper',
'report_xlsx',
'resource',
'sale_async_emails',
'sale_crm',
'sale_expense',
'sale_management',
'sale_mrp',
'sale_pdf_quote_builder',
'sale_product_configurator',
'sale_project_stock',
'sale_project',
'sale_purchase_stock',
'sale_purchase',
'sale_service',
'sale_sms',
'sale_stock',
'sale_timesheet',
'sale',
'sales_team',
'server_action_mass_edit',
'show_db_name',
'sms',
'snailmail_account',
'snailmail',
'social_media',
'spreadsheet_account',
'spreadsheet_dashboard_account',
'spreadsheet_dashboard_hr_expense',
'spreadsheet_dashboard_hr_timesheet',
'spreadsheet_dashboard_purchase_stock',
'spreadsheet_dashboard_purchase',
'spreadsheet_dashboard_sale_timesheet',
'spreadsheet_dashboard_sale',
'spreadsheet_dashboard_stock_account',
'spreadsheet_dashboard',
'spreadsheet',
'stock_account',
'stock_sms',
'stock',
'uom',
'utm',
'web_editor',
'web_hierarchy',
'web_no_bubble',
'web_responsive',
'web_tour',
'web_unsplash',
'web',
'disable_odoo_online',
'remove_odoo_enterprise',
'auto_backup',
    
      
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

