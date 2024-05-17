{
    "name": "Odoo Branding 17",
    "version": "17.0.0.0.1",
    "category": "",
    'summary': "Odoo Branding 17",
    'description': "Odoo Branding 17",
    "author": "xyz",
    "website": "",
    'license': '',
    "depends": [
        'base', 'point_of_sale', 'base_setup', 'web', 'mail', 'portal'],
    "data": [
        "security/ir.model.access.csv",
        "data/sh_configuraion_data.xml",
        "views/fevicon.xml",
        "views/menu_management_views.xml",
        "views/webclient_template.xml",
        "views/layout.xml",
        "views/mail_template_views.xml",
        "views/res_config_setting_views.xml",
    ],
    "assets": {
        'web.assets_backend': [
            'odoo17_branding/static/src/js/customize_user.js',
            'odoo17_branding/static/src/js/dialog.js',
            'odoo17_branding/static/src/js/error.js',
            'odoo17_branding/static/src/js/system_name.js',
            'odoo17_branding/static/src/js/avatar.js',
            'odoo17_branding/static/src/xml/mail_bot_sample.xml',
            'odoo17_branding/static/src/scss/style.scss',
        ],
        # "web.assets_backend": ["odoo17_branding/static/src/js/tour.js"],
        "point_of_sale._assets_pos": [
            "odoo17_branding/static/src/xml/pos_debranding.xml",
        ],
    },
    "installable": True,
}
